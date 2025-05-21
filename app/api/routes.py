from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from app.controllers.scanner_controller import ScannerController

router = APIRouter()

@router.post("/scan/")
async def scan_file(file: UploadFile = File(...)):
    try:
        result = await ScannerController.scan_file(file)
        return JSONResponse(content=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
