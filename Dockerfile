FROM python:3.8.17-slim

ENV PYTHONUNBUFFERED=TRUE

RUN pip --no-cache-dir install pipenv

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "./"]
RUN pipenv install --deploy --system && \
    rm -rf /root/.cache

# Copy contents of src folder
COPY ["./src/", "./src/"]

# Copy contents of data folder
COPY ["./data/", "./data/"]

# Copy model_gbc.pkl file
COPY ["./models/", "./models/"]

EXPOSE 9696

ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:9696", "serving_diabetes:app"] 