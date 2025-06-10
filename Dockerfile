FROM python:3.11-alpine AS requirements-stage
WORKDIR /tmp

# Install poetry and the export plugin
RUN pip install poetry \
    && poetry self add poetry-plugin-export

COPY ./poetry.lock* ./pyproject.toml /tmp/

# Export requirements.txt using poetry export (now available)
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.11-alpine AS base
WORKDIR /code

COPY --from=requirements-stage /tmp/requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]