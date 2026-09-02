import os
import shutil
from pathlib import Path
from uuid import uuid4

from dotenv import load_dotenv
from fastapi import UploadFile

from ..models.document_model import Document
from ..utils.file_validator import validate_file_extension


load_dotenv()


class DocumentService:

    def save_document(self, file: UploadFile) -> Document:

        if not file.filename:
            raise ValueError("No se recibió ningún archivo.")

        extension = validate_file_extension(file.filename)

        temporary_folder = os.getenv(
            "TEMPORARY_FOLDER",
            "temporary"
        )

        temporary_path = Path(temporary_folder)
        temporary_path.mkdir(
            parents=True,
            exist_ok=True
        )

        document_id = str(uuid4())

        stored_filename = f"{document_id}{extension}"

        file_path = temporary_path / stored_filename

        with open(file_path, "wb") as destination:
            shutil.copyfileobj(
                file.file,
                destination
            )

        return Document(
            document_id=document_id,
            original_filename=file.filename,
            stored_filename=stored_filename,
            extension=extension,
            path=str(file_path)
        )

    def save_documents(
        self,
        files: list[UploadFile]
    ) -> list[Document]:

        documents = []

        for file in files:
            document = self.save_document(file)
            documents.append(document)

        return documents