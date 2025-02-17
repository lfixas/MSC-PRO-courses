FROM node:12-alpine

EXPOSE 80

WORKDIR /result

COPY . .

RUN npm install

CMD ["node", "server.js"]