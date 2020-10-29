from django.http.request import QueryDict, MultiValueDict

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import Archive
from .main import predict
from .serializers import ArchiveSerializer
from .utils import get_auth0_user_id_from_request
from .permissions import IsCreator


class ArchiveList(APIView):
    def get(self, request, format=None):
        auth0_user_id = get_auth0_user_id_from_request(self.request)
        archives = Archive.objects.all().filter(created_by=auth0_user_id)
        serializer = ArchiveSerializer(archives, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        dict_data = dict(request.data)
        dict_data['result'] = predict(request.FILES['file'])
        dj_query_dict = QueryDict('', mutable=True)
        dj_query_dict.update(MultiValueDict(dict_data))
        auth0_user_id = get_auth0_user_id_from_request(self.request)
        serializer = ArchiveSerializer(data=dj_query_dict)
        if serializer.is_valid():
            serializer.save(created_by=auth0_user_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArchiveDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Archive.objects.all()
    serializer_class = ArchiveSerializer
    permission_classes = [IsAuthenticated,IsCreator]
    lookup_url_kwarg = 'archive_id'