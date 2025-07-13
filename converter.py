import whisper
import os, sys

def transcribe_audio(audio_path, model_name="base", language="en"):
    if not os.path.exists(audio_path):
        raise FileNotFoundError(f"Audio file {audio_path} does not exist.")
    model = whisper.load_model(model_name)
    result = model.transcribe(audio_path, language=language)
    return result['text']

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python converter.py <audio_file_path> [model_name] [language]")
        sys.exit(1)

    audio_file_path = sys.argv[1]
    model_name = sys.argv[2] if len(sys.argv) > 2 else "base"
    language = sys.argv[3] if len(sys.argv) > 3 else "en"

    try:
        transcription = transcribe_audio(audio_file_path, model_name, language)
        outfile = os.path.splitext(audio_file_path)[0] + "_transcription.txt"
        with open(outfile, 'w', encoding='utf-8') as f:
            f.write(transcription)
        print(f"Transcription saved to {outfile}")
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
    else:
        print("Transcription completed successfully.")
        sys.exit(0)
