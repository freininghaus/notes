import json
import os
from aiohttp import web

DATA = {}


async def list_keys(request):
    return web.json_response(sorted(DATA))


async def add_document(request):
    key = request.match_info["key"]
    try:
        document = await request.json()
    except json.decoder.JSONDecodeError as error:
        raise web.HTTPBadRequest(
            text=f"Failed to parse request content as JSON. Error at position {error.pos}: {error.msg}")

    DATA[key] = document
    return web.Response(text="ok")


async def delete_document(request):
    key = request.match_info["key"]
    try:
        del DATA[key]
    except KeyError:
        raise web.HTTPNotFound()

    return web.Response(text="ok")


async def get_document(request):
    key = request.match_info["key"]
    try:
        return web.json_response(DATA[key])
    except KeyError:
        raise web.HTTPNotFound()


print("CRUD demo app (using a list of routes)")

app = web.Application()
app.add_routes([
    web.get("/", list_keys),
    web.put("/{key}", add_document),
    web.post("/{key}", add_document),
    web.delete("/{key}", delete_document),
    web.get("/{key}", get_document)
])

web.run_app(app, port=os.getenv("PORT", 8080))
