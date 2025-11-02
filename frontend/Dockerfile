# Frontend Dockerfile
FROM node:18

WORKDIR /frontend

COPY ./frontend /frontend

RUN npm install

EXPOSE 5173

CMD ["npm", "run", "dev", "--", "--host"]
