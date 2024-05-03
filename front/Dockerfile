FROM node:14

# Устанавливаем рабочую директорию внутри образа
WORKDIR /app

# Копируем файлы package.json и package-lock.json для установки зависимостей
COPY package*.json ./

# Устанавливаем зависимости проекта
RUN npm install

# Копируем все файлы проекта в текущую директорию образа
COPY . .

# Собираем проект
RUN npm run build

# Открываем порт, на котором будет работать приложение Vue.js
EXPOSE 8080

# Команда для запуска сервера Vue.js в production-режиме
CMD [ "npm", "run", "serve" ]