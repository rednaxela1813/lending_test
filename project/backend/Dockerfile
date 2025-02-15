# Используем Python 3.12
FROM python:3.12

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем только файлы зависимостей (ускоряет сборку при изменении кода)
COPY requirements.txt ./

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальной код проекта
COPY . .

# Открываем порт 8000
EXPOSE 8000

# Запускаем сервер Django (можно заменить на gunicorn для продакшена)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
