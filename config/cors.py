from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

def create_app(enable_cors: bool = True) -> FastAPI:
    app = FastAPI()

    if enable_cors:
        # Configurar CORS
        origins = [
            "http://127.0.0.1:5000",
            "http://localhost:5000",
        ]

        app.add_middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    return app