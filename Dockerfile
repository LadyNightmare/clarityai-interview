FROM python:3.9-slim AS build
COPY --from=ghcr.io/astral-sh/uv:0.8.21 /uv /uvx /bin/
WORKDIR /app
ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy
COPY uv.lock pyproject.toml ./
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --no-install-project --no-dev
COPY ./data/ ./data/
COPY ./src/ ./src/
COPY ./tests/ ./tests/
COPY ./pyproject.toml ./pyproject.toml
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev

FROM build AS test
ENV PATH="/app/.venv/bin:$PATH"
WORKDIR /app
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen
    
FROM python:3.9-slim AS runtime
ENV PATH="/app/.venv/bin:$PATH"
RUN groupadd -g 1001 appgroup && \
    useradd -u 1001 -g appgroup -m -d /app -s /bin/false appuser
WORKDIR /app
COPY --from=build --chown=appuser:appgroup /app .
USER appuser
ENTRYPOINT ["python", "src/main.py"]