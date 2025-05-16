FROM python:3.13.3-slim

WORKDIR /social-network

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN useradd -m -r test && chown -R test /social-network

USER test

EXPOSE 8080

ENTRYPOINT ["python", "-m"]
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
