# FastAPI Template

A minmal FastAPI Template for starting an AI project from scratch.

## Application Features:

- Configurable with BaseSettings of Pydantic
- Structured Logging
- API endpoints secured with API key authentication
- Centralized error handling with custom exceptions and detailed logging

## How To Adapt

### Docker

> [!IMPORTANT]
> Run `Setup` as your init command (or after `Clean`).

1. Build the Docker image:

    ```bash
    docker build --no-cache -t fastapi-app:latest
    ```

2. Run the Docker container locally with:

    ```bash
    docker run --rm -p 8000:8080 -v ${PWD}/.env:/usr/app/.env fastapi-app:latest
    ```

3. Run the service container:
    - Run this command to start it:
        ```bash
        docker compose up -d --build
        ```
    - Run this command to stop it:
        ```bash
        docker compose down
        ```

### Boostrap Environment

To easily install the dependencies, a `Makefile` is created

- Check: `make clean`
    - Use it to check `which pip3` and `which python3` that point to the right path
- Setup: `make setup`
    - Create an environment and installs all dependencies
- Tidy up the codebase: `make tidy`
    - Run Ruff check and format
- Clean artifacts: `make clean`
    - Removes the environment and all cached files
- Test configurations: `make test`
    - Runs all tests using [pytest](https://pypi.org/project/pytest/)

## References

- [Using uv with FastAPI](https://docs.astral.sh/uv/guides/integration/fastapi/#using-uv-with-fastapi)
- [Deployments Concepts](https://fastapi.tiangolo.com/deployment/concepts/)
- [How to secure APIs built with FastAPI: A complete guide](https://escape.tech/blog/how-to-secure-fastapi-api/)