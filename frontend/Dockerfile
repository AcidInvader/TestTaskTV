FROM node:16-alpine

WORKDIR /frontend

COPY . /frontend
RUN npm install
COPY . /frontend

EXPOSE 3000

CMD ["npm", "start"]