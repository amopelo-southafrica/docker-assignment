FROM python:3.12-slim

WORKDIR /app

COPY finance_calculators.py .

CMD ["python", "finance_calculators.py"]
