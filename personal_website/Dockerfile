FROM node:14 AS base

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH
COPY package.json package-lock.json tsconfig.json /app/

RUN npm ci

COPY . ./

RUN npm run-script build

FROM nginx:latest

EXPOSE 80
COPY --from=base /app/build /usr/share/nginx/html
