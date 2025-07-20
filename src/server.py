from typing import Optional

from fastmcp import FastMCP

mcp = FastMCP("data.gov.gr MCP Server")


@mcp.tool
def get_dataset(
    dataset: str, date_from: Optional[str] = None, date_to: Optional[str] = None
):
    """Get a dataset from the data.gov.gr API."""
    from pydatagovgr import DataGovClient

    gov = DataGovClient()

    if date_from is None or date_to is None:
        return gov.query(dataset)
    else:
        return gov.query(dataset, date_from=date_from, date_to=date_to)


if __name__ == "__main__":
    mcp.run(transport="http", host="127.0.0.1", port=8000)
