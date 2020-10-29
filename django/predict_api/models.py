from django.db import models


class Archive(models.Model):
    created_by = models.CharField(max_length=200)
    file = models.FileField(blank=False, null=False)
    result = models.CharField(max_length=50)

    class Meta:
        db_table = 'archive'
        ordering = ['id']

    def __str__(self):
        return self.file.name