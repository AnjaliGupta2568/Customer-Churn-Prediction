FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install fastapi uvicorn sentence-transformers faiss-cpu google-generativeai python-multipart

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]