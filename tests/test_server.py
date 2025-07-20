from unittest.mock import patch

import pytest
from fastmcp import Client

from src.server import mcp


@patch("pydatagovgr.DataGovClient.query")
@pytest.mark.asyncio
async def test_get_dataset(mock_query):
    mock_query.return_value = {"data": "yes"}
    async with Client(mcp) as client:
        result = await client.call_tool("get_dataset", {})
        assert result.data == {"data": "yes"}
