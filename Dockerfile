FROM python:3.13-slim

WORKDIR /app

COPY requirement.txt .

RUN pip install --no-cache-dir \
    --index-url https://download.pytorch.org/whl/cpu \
    torch && \
    pip install --no-cache-dir -r requirement.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "backend/main.py", "--server.port", "8501", "--server.address", "0.0.0.0"