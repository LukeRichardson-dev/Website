FROM node:14 AS base

WORKDIR /app

COPY package.json package-lock.json /app/

RUN npm ci

COPY . .

RUN npm run-script build

FROM nginx:latest

EXPOSE 80
COPY --from=base /app/build /usr/share/nginx/html
