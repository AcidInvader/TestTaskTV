FROM node:16-alpine

WORKDIR /frontend

COPY package.json /frontend/package.json
RUN npm install
COPY . /frontend

EXPOSE 3000

CMD ["npm", "run","start", "build"]