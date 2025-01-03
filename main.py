import asyncio
from contextlib import asynccontextmanager

import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from mock_server import GRPCServer
from settings import settings
from information_system_design import routes


@asynccontextmanager
async def lifespan(app: FastAPI):
    if settings.DEBUG:
        grpc_server = GRPCServer()
        await grpc_server.start()  # Запускаем сервер
        task = asyncio.create_task(
            grpc_server.server.wait_for_termination()
        )  # Ожидание завершения сервера

        try:
            yield
        finally:
            await grpc_server.stop()  # Остановка сервера
            await task  # Дождаться завершения задачи


app = FastAPI(
    lifespan=lifespan,
    title="Example gRPC service on Python",
    description="This showing how to use gRPC on Python",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routes.router)

if __name__ == "__main__":
    uvicorn.run(
        "main:app", port=settings.MAIN_PORT, host=settings.MAIN_HOST, reload=True
    )
