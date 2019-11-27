import socket

import aiohttp
from aiohttp import web
import os

PORT = os.getenv("PORT", 8080)
NAME = os.getenv("NAME", "simple_http_test_app")
HOSTNAME = socket.gethostname()
IP = socket.gethostbyname(HOSTNAME)
ID = f"{NAME} running on {HOSTNAME} ({IP}) on port {PORT}"


async def ping(request):
    return web.Response(text=f"response from {ID}\n")


async def access(request):
    url = request.match_info["url"]

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            text = await response.text()
            return web.Response(text=f"forwarded by {ID}:\n  {text}\n")


if __name__ == "__main__":
    app = web.Application()

    app.add_routes((web.get("/ping", ping),
                   (web.get("/access/{url:.*}", access))))

    web.run_app(app, port=PORT)