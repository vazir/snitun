"""Tests for aiohttp snitun client."""
from unittest.mock import patch

from snitun.utils.aiohttp_client import SniTunClientAioHttp


async def test_init_client():
    """Init aiohttp client for test."""

    with patch("snitun.utils.aiohttp_client.SockSite"):
        client = SniTunClientAioHttp(None, None, "127.0.0.1")

    assert not client.is_connected


async def test_client_stop_no_wait():
    """Test that we do not wait if wait is not passed to the stop"""

    with patch("snitun.utils.aiohttp_client.SockSite"):
        client = SniTunClientAioHttp(None, None, "127.0.0.1")

    with patch("snitun.utils.aiohttp_client.socket.socket.fileno") as fileno:
        fileno.return_value = -1
        await client.stop()
        fileno.assert_not_called()

        await client.stop(wait=True)
        fileno.assert_called()
