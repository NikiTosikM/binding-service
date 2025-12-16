FROM python:3.12-slim


WORKDIR /app

COPY pyproject.toml .

RUN pip install uv 
RUN uv venv; uv pip install pyproject.toml

COPY . .

CMD [ "uv", "run",  "src/main.py" ]