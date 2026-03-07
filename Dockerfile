FROM python:3.13

WORKDIR /app

COPY . .

RUN pip install pytest

CMD ["pytest", "lesson_23/test_homeworks23.py", "-v"]