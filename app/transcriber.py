import whisper
import os, sys
import logging

class Transcriber:
    def __init__(self, model_name="base", language="en", logger=None):
        self.model_name = model_name
        self.language = language
        self.model = whisper.load_model(model_name)
        self.logging = logger or logging.getLogger(__name__)
        
        self.logging.info(f"Whisper model '{model_name}' loaded successfully.")
    

    def transcribe_audio(self, audio_path):
        """
        Transcribe audio file using Whisper model.
        
        :param audio_path: Path to the audio file."""
        self.logging.info(f"Transcribing audio file: {audio_path} with model: {self.model_name} and language: {self.language}")
        if not os.path.exists(audio_path):
            self.logging.error(f"Audio file {audio_path} does not exist.")
            raise FileNotFoundError(f"Audio file {audio_path} does not exist.")
        result = self.model.transcribe(audio_path, language=self.language)
        return result['text']
    def clean_text(self, text):
        """
        Clean the transcript text by fixing grammatical errors and removing irrelevant noise or filler words.
        
        :param text: Raw transcript text.
        :return: Cleaned transcript text."""
        self.logging.info("Cleaning transcript text.")
        # Placeholder for actual cleaning logic
        cleaned_text = text.replace(" uh ", " ").replace(" um ", " ").strip()
        return cleaned_text
    
    def process_transcription(self, audio_path):
        """
        Process the transcription by transcribing and cleaning the audio file.
        
        :param audio_path: Path to the audio file.
        :return: Cleaned transcript text."""
        try:
            transcription = self.transcribe_audio(audio_path)
            cleaned_transcription = self.clean_text(transcription)
            outfile = os.path.splitext(audio_path)[0] + "_transcription.txt"
            with open(outfile, 'w', encoding='utf-8') as f: 
                f.write(cleaned_transcription)
            self.logging.info(f"Transcription saved to {outfile}")
            return cleaned_transcription
        except Exception as e:
            self.logging.error(f"An error occurred during transcription: {e}")
            raise
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python transcriber.py <audio_file_path> [model_name] [language]")
        sys.exit(1)
    audio_file_path = sys.argv[1]
    model_name = sys.argv[2] if len(sys.argv) > 2 else "tiny"
    language = sys.argv[3] if len(sys.argv) > 3 else "en"
    try:
        trans = Transcriber(model_name, language)
        print(f"Transcribing audio file: {audio_file_path} using model: {model_name} and language: {language}")
        print(trans.process_transcription(audio_file_path))
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
