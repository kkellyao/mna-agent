from fastapi import APIRouter, Depends, HTTPException, UploadFile
from pydantic import BaseModel

from app.core.config import Settings, get_settings

router = APIRouter(prefix="/documents", tags=["documents"])


class UploadResponse(BaseModel):
    filename: str
    saved_path: str
    status: str


@router.post("/upload", response_model=UploadResponse, status_code=201)
async def upload_document(
    file: UploadFile,
    settings: Settings = Depends(get_settings),
) -> UploadResponse:
    if file.content_type != "application/pdf" or not (file.filename or "").endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are accepted.")

    settings.vault_dir.mkdir(parents=True, exist_ok=True)
    dest = settings.vault_dir / file.filename

    contents = await file.read()
    dest.write_bytes(contents)

    return UploadResponse(
        filename=file.filename,
        saved_path=str(dest),
        status="uploaded",
    )
