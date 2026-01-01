from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from starlette.middleware.cors import CORSMiddleware

app = FastAPI(
    default_response_class=ORJSONResponse
)
