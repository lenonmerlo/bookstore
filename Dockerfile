# Use Python 3.12 slim image as base
FROM python:3.12-slim as python-base

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.7.1 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

# Prepend poetry and venv to path
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

# Install dependencies (Poetry and other build tools)
RUN apt-get update && apt-get install --no-install-recommends -y \
        curl \
        build-essential \
        libpq-dev gcc \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && apt-get clean

# Set working directory
WORKDIR $PYSETUP_PATH

# Copy poetry files and install dependencies
COPY poetry.lock pyproject.toml ./
RUN poetry install --no-dev --no-root

# Set app directory
WORKDIR /app

# Copy application code
COPY . /app/

# Install runtime dependencies (already installed during build)
RUN poetry install --no-dev

# Expose port 8000 for the app
EXPOSE 8000

# Run the application using Gunicorn (recommended for production)
CMD ["gunicorn", "bookstore.wsgi:application", "--bind", "0.0.0.0:$PORT"]
