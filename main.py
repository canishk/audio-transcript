import os
from fastapi import FastAPI, File, UploadFile
from tempfile import NamedTemporaryFile

from app.transcriber import Transcriber
from app.summarizer_ai import SummarizerAI

app = FastAPI()

@app.post("/transcribe")
async def transcribe_audio(file: UploadFile = File(...)):
    with NamedTemporaryFile(delete=False, suffix=".wav") as temp_file:
        temp_file.write(await file.read())
        temp_file_path = temp_file.name
    transcriber = Transcriber(model_name="tiny", language="en")
    transcription = transcriber.process_transcription(temp_file_path)
    os.remove(temp_file_path)  # Clean up the temporary file 

    summarizer = SummarizerAI(google_api_key=os.getenv("GOOGLE_API_KEY"))
    summary = summarizer.summarize_text(transcription)
    return {
        "transcription": summary,
    }