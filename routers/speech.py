from fastapi import APIRouter
from ai_stem_tutor.services.text_to_speech import text_to_speech

router = APIRouter()

@router.post("/speak")
def speak_text(payload: dict):
    text = payload.get("text", "")
    output_path = text_to_speech(text)
    return {"file_path": output_path}
