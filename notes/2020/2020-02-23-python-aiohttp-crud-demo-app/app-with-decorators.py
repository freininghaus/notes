import json
import os
from aiohttp import web

DATA = {}


routes = web.RouteTableDef()


@routes.get("/")
async def list_keys(request):
    return web.json_response(sorted(DATA))


@routes.put("/{key}")
@routes.post("/{key}")
async def add_document(request):
    key = request.match_info["key"]
    try:
        document = await request.json()
    except json.decoder.JSONDecodeError as error:
        raise web.HTTPBadRequest(
            text=f"Failed to parse request content as JSON. Error at position {error.pos}: {error.msg}")

    DATA[key] = document
    return web.Response(text="ok")


@routes.delete("/{key}")
async def delete_document(request):
    key = request.match_info["key"]
    try:
        del DATA[key]
    except KeyError:
        raise web.HTTPNotFound()

    return web.Response(text="ok")


@routes.get("/{key}")
async def get_document(request):
    key = request.match_info["key"]
    try:
        return web.json_response(DATA[key])
    except KeyError:
        raise web.HTTPNotFound()


print("CRUD demo app (routes added to RouteTableDef with decorators)")

app = web.Application()
app.add_routes(routes)
web.run_app(app, port=os.getenv("PORT", 8080))
