FROM node:14 AS base

WORKDIR /app

FROM base AS build

COPY package.json package-lock.json /app/

RUN npm ci

COPY . .

RUN npm build

EXPOSE 3000

CMD [ "npm", "start" ]
