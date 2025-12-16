from fastapi import FastAPI, Request
from fastapi.responses import ORJSONResponse


def server_error_handler(app: FastAPI):
    @app.exception_handler(Exception)
    def unexpected_errors(request: Request, exc: Exception):
        return ORJSONResponse(
            status_code=500,
            content={
                "message": "An unexpected error occurred",
                "detail": "The service is temporarily unavailable. We apologize"
            }
        )