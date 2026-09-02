from fastapi import APIRouter, File, HTTPException, UploadFile

from ..services.document_service import DocumentService


router = APIRouter(
    prefix="/api/documents",
    tags=["Documents"]
)

document_service = DocumentService()


@router.post("/upload")
def upload_documents(
    files: list[UploadFile] = File(...)
):
    try:
        documents = document_service.save_documents(files)

        return {
            "message": "Documentos recibidos y almacenados correctamente.",
            "documents": [
                {
                    "document_id": document.document_id,
                    "filename": document.original_filename,
                    "extension": document.extension,
                    "path": document.path
                }
                for document in documents
            ]
        }

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        ) from error