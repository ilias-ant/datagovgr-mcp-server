FROM python:3.12-slim

LABEL org.opencontainers.image.version="0.1.0"
LABEL org.opencontainers.image.authors="Ilias Antonopoulos"
LABEL org.opencontainers.image.description="builds data.gov.gr MCP server image"

# set work directory
WORKDIR /app

# install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# copy only dependency files first for better caching
COPY pyproject.toml uv.lock ./

# install pip build backend and project dependencies
RUN pip install --upgrade pip \
    && pip install pip-tools \
    && pip install .

# copy the rest of the application code
COPY src/ ./src/

EXPOSE 8000

# set entrypoint
CMD ["python", "src/server.py", "--host", "0.0.0.0", "--port", "8000"]
