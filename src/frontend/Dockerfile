FROM node:20-alpine

WORKDIR /app/

COPY package.json package-lock.json ./

COPY .env .

# Update npm to latest version
RUN npm install -g npm@latest

#Install dependencies
RUN npm install

ENTRYPOINT [ "npm", "start"]