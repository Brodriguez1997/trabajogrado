from dataclasses import dataclass


@dataclass
class Document:
    document_id: str
    original_filename: str
    stored_filename: str
    extension: str
    path: str