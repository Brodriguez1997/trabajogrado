from pathlib import Path


ALLOWED_EXTENSIONS = {
    ".pdf",
    ".docx",
    ".doc",
    ".docm",
    ".dotx",
    ".dotm",
    ".dot",
    ".odt",
}


def validate_file_extension(filename: str) -> str:
    extension = Path(filename).suffix.lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise ValueError(
            "Formato de archivo no permitido. "
            "Los formatos permitidos son: "
            "PDF, DOCX, DOC, DOCM, DOTX, DOTM, DOT y ODT."
        )

    return extension
