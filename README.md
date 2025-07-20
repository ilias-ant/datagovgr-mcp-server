# datagovgr-mcp-server

An MCP server for the data.gov.gr API.

## Install

This project requires **Python 3.12**.

It is recommended to use [uv](https://github.com/astral-sh/uv) for dependency management (a fast, modern Python package manager).
Alternatively, you can use `pip` with the `pyproject.toml` file.

### Using uv

```bash
python -m pip install uv

uv venv
uv sync
```

## Usage

### Running the MCP Server

To start the server (by default on http://127.0.0.1:8000):

```bash
python src/server.py
```

You can now connect to this server with various applications e.g. Cursor, Claude etc.
