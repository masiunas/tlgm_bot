# Используйте базовый образ Python
FROM python:3.9

# Установка переменной окружения PYTHONUNBUFFERED для предотвращения буферизации вывода
ENV PYTHONUNBUFFERED=1

# Установка рабочей директории в /app
WORKDIR /app

# Копирование файлов приложения в контейнер
COPY app /app

# Установка зависимостей из requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Команда для запуска вашего приложения
CMD ["python", "main.py"]
