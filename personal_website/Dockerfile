FROM node:14 AS base

WORKDIR /app

FROM base AS build

COPY package.json package-lock.json /app/

RUN npm ci
RUN npm build

COPY . .

EXPOSE 3000

CMD [ "npm", "start" ]
