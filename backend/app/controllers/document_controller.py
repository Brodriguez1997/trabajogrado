from fastapi import APIRouter, File, HTTPException, UploadFile

from ..services.document_service import DocumentService

router = APIRouter(
    prefix="/api/documents",
    tags=["Documents"]
)

document_service = DocumentService()


@router.post("/upload")
def upload_document(
    file: UploadFile = File(...)
):
    try:
        document = document_service.save_document(file)

        return {
            "message": "Documento recibido y almacenado correctamente.",
            "document_id": document.document_id,
            "filename": document.original_filename,
            "extension": document.extension,
            "path": document.path
        }

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        ) from error