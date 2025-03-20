import os
from fastapi import FastAPI, HTTPException, Request
from importlib.metadata import version

from fastapi.responses import JSONResponse, RedirectResponse

from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from espie_character_gen import configs
from espie_character_gen.rest_app.authentication import (
    get_verifier,
    token_auth_scheme,
)


try:
    _version = version("espie_character_gen")
except:  # pragma: no cover
    _version = "dev"

fastapi_app = FastAPI(
    title="Espie Character Gen API",
    version=_version,
)

fastapi_app.add_middleware(
    CORSMiddleware,
    allow_origins=configs.cors_origins,
    allow_credentials=configs.cors_allow_credentials,
    allow_methods=configs.cors_methods,
    allow_headers=configs.cors_headers,
)


@fastapi_app.middleware("http")
async def hydrate_user(
    request: Request,
    call_next,
):
    try:
        token = await token_auth_scheme(request)
    except HTTPException as e:
        if e.detail == "Not authenticated":
            return await call_next(request)
        return JSONResponse(
            {"status": "error", "message": "Not Authenticated"}, status_code=401
        )

    result = get_verifier().verify(token.credentials)

    if result.get("status"):
        return JSONResponse(result, status_code=403)
    request.state.user = result
    return await call_next(request)


@fastapi_app.get("/healthz")
def healthz():
    return {"o": "k"}


@fastapi_app.get("/version")
def version():
    return {"version": _version}


@fastapi_app.get("/me")
def get_me(request: Request):
    return getattr(request.state, "user", None)


templates = Jinja2Templates(
    directory=os.path.join(os.path.dirname(__file__), "templates")
)


def link(url: str, name: str):
    return {"url": url, "name": name}


LINKS = [
    link("/", "Home"),
    link("/about", "About"),
    link("/contact", "Contact"),
]


def context(**kwargs):
    return {
        **kwargs,
        "links": LINKS,
    }


@fastapi_app.get("/")
def index(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context=context(name="Billy Ichiban"),
    )


@fastapi_app.get("/{path:path}")
def catch_all(path: str):
    return RedirectResponse(url="/", status_code=302)
