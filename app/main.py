import sqlalchemy
from fastapi import FastAPI, HTTPException, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.responses import RedirectResponse

from app.api.v1.cake import router
from app.config.settings import Settings

app = FastAPI(title=Settings().app_name)
app.include_router(router, prefix="/v1")


@app.get("/")
async def docs_redirect():
    return RedirectResponse(url="/docs")


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(_, exc):
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(_, exc):
    return PlainTextResponse(str(exc), status_code=status.HTTP_400_BAD_REQUEST)


@app.exception_handler(sqlalchemy.exc.IntegrityError)
async def sql_exception_handler(_, err):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"message": f"{str(err._message)}"},
    )


@app.exception_handler(Exception)
async def general_exception_handler(request, err):
    base_error_message = f"Failed to execute: {request.method}"
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"message": f"{base_error_message}. Detail: {str(err)}"},
    )
