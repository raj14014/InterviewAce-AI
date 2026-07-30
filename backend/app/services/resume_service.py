import os
import shutil

UPLOAD_FOLDER = "uploads"


async def save_resume(file):
    """
    Save uploaded resume to uploads folder
    """

    # Create uploads folder if it doesn't exist
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "filename": file.filename,
        "file_path": file_path
    }