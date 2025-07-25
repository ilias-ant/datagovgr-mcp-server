# datagovgr-mcp-server

An MCP server for the data.gov.gr API.

## Install

The quickest way to run the MCP server is via Docker:

```bash
docker build -t datagovgr-mcp-server:latest .

docker run -p 8000:8000 datagovgr-mcp-server:latest
```

For a development installation, it is recommended to use [uv](https://github.com/astral-sh/uv) with 
Python **3.12**:

```bash
python3 -m pip install uv

python3 -m uv venv

python3 -m uv sync

python3 -m uv run python src/server.py
```

If you want to run the test suite:

```bash
PYTHONPATH=. python3 -m uv run pytest tests
```

## Usage

Assuming that the MCP Server is running on [http://0.0.0.0:8000/mcp/](http://0.0.0.0:8000/mcp/), you can now connect to this server from various applications/clients e.g. Cursor, Claude etc.  (*see connection guides for various applications below*).

Some indicative prompts that you can try are the following:

```text
Fetch me the internet traffic dataset from data.gov.gr. I want data from 21/06 until 24/07 for 2025. Download them as CSV as well, in a newly created directory called datagovgr_datasets
```

### Connect to Cursor

Assuming that the localhost MCP Server is running on http://127.0.0.1:8000:

1. Head over to Cursor > Settings... > Cursor Settings.
2. Click on Tools & Integrations.
3. Under MCP Tools, click the button: Add Custom MCP.
4. A new file, called `mcp.json` will open. Register the MCP server as in the example below, and save the file:

```json
{
  "mcpServers": {
    "data.gov.gr MCP Server": {
      "url": "http://0.0.0.0:8000/mcp"
    }
  }
}
```

Heading back to the MCP Tools view of step #3, you will see the tool `data.gov.gr MCP Server` being available. Make sure
it is enabled. In that case, you should be able to see something like `1 tool enabled` displayed. This means integration is ready!

## License

Distributed under the [MIT License](LICENSE).
