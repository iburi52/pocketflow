# The build image
FROM node:14.8-alpine as builder

RUN mkdir /app
WORKDIR /app

COPY frontend/package.json frontend/package-lock.json /app/frontend/
RUN npm install --prefix frontend

COPY . /app

RUN npm run build --prefix frontend -- --output-path=./dist/out

# The production image
FROM nginx:1.19.2-alpine

RUN rm -rf /usr/share/nginx/html/*
COPY --from=builder /app/frontend/dist/out /usr/share/nginx/html
COPY ./nginx/nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80


