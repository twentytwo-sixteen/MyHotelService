FROM python:3.11-slim

WORKDIR /app

COPY poetry.lock pyproject.toml ./
RUN pip install poetry && poetry config virtualenvs.create false && poetry install --no-root

COPY . .

CMD ["uvicorn", "src.hotel_booking.main:app", "--host", "0.0.0.0", "--port", "8000"]
