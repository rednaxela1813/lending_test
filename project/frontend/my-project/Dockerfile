# Базовый образ для сборки
FROM node:22.13.1 as builder

# Устанавливаем рабочую директорию
WORKDIR /usr/src/app

# Добавляем директорию node_modules в PATH
ENV PATH="/usr/src/app/node_modules/.bin:$PATH"

# Подключаем переменные окружения VITE
ARG VITE_BACKEND_URL
ENV VITE_BACKEND_URL=$VITE_BACKEND_URL

# Копируем файлы зависимостей
COPY package*.json ./

# Чистим кэш и устанавливаем зависимости
RUN npm cache clean --force
RUN npm install --legacy-peer-deps

# Копируем весь код проекта
COPY . .

### --- Окружение для разработки ---
FROM builder as dev
EXPOSE 5173
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]

### --- Окружение для продакшена ---
FROM builder as prod
RUN npm run build
CMD ["npx", "vite", "preview", "--host"]
