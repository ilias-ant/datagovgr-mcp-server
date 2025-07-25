from typing import Annotated, Optional

from fastmcp import FastMCP
from pydantic import Field

mcp = FastMCP("data.gov.gr MCP Server")


@mcp.tool
def get_dataset(
    dataset: Annotated[
        str, Field(description="The dataset name from https://data.gov.gr")
    ],
    date_from: Annotated[
        Optional[str],
        Field(
            description="Start date (YYYY-MM-DD) - not all datasets require this.",
            json_schema_extra={"example": "2025-01-01"},
        ),
    ] = None,
    date_to: Annotated[
        Optional[str],
        Field(
            description="End date (YYYY-MM-DD) - not all datasets require this.",
            json_schema_extra={"example": "2025-01-31"},
        ),
    ] = None,
    download: Annotated[
        bool,
        Field(
            description="Whether to download the dataset. Use this only if user asks for a download.",
            json_schema_extra={"example": False},
        ),
    ] = False,
    type_: Annotated[
        Optional[str],
        Field(
            description="In which format to download the dataset - this is only available for download=true",
            json_schema_extra={"example": "json"},
        ),
    ] = None,
):
    """Get a dataset from the https://data.gov.gr API."""
    from pydatagovgr import DataGovClient

    gov = DataGovClient()

    params = {}

    if date_from:
        params["date_from"] = date_from
    if date_to:
        params["date_to"] = date_to
    if download:
        dataset = f"download/{dataset}"
    if type_:
        params["type"] = type_

    return gov.query(dataset, **params)


if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)
