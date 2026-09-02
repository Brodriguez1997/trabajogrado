from fastapi import FastAPI

from .controllers.document_controller import router as document_router


app = FastAPI(
    title="Analizador de Documentos con IA",
    description="API para recepción y análisis de documentos académicos",
    version="1.0.0"
    # ,docs_url=None,
    # redoc_url=None,
    # openapi_url=None
)


app.include_router(document_router)


@app.get("/")
def root():
    return {
        "message": "Backend del analizador de documentos funcionando"
    }