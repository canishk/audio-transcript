import sys, os
import logging
from dotenv import load_dotenv
from app.summarizer_ai import SummarizerAI
from app.transcriber import Transcriber

class AudioTranscriberApp:
    def __init__(self):
        """
        Initialize the AudioTranscriberApp with default configurations.
        """
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        load_dotenv()  # Load environment variables from .env file
        self.google_api_key = os.getenv("GOOGLE_API_KEY")
        
    
    def main(self,audio_file_path, model_name="tiny", language="en"):
        """
        Main method to transcribe and summarize audio file.
        
        :param audio_file_path: Path to the audio file."""
        self.logger.info(f"Starting transcription for audio file: {audio_file_path} using model: {model_name} and language: {language}")
        try:
            transcriber = Transcriber(model_name=model_name, language=language, logger=self.logger)
            cleaned_transcription = transcriber.process_transcription(audio_file_path)
            if self.google_api_key:
                summarizer = SummarizerAI(google_api_key=self.google_api_key, logger=self.logger)
                summary = summarizer.summarize_text(cleaned_transcription)
                outfile = os.path.splitext(audio_file_path)[0] + "_summary.txt"
                with open(outfile, 'w', encoding='utf-8') as f:
                    f.write(summary)
                f.close()
        except Exception as e:
            self.logger.error(f"An error occurred during transcription or summarization: {e}")
            raise
    
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python app.py <audio_file_path> [model_name] [language]")
        sys.exit(1)

    audio_file_path = sys.argv[1]
    model_name = sys.argv[2] if len(sys.argv) > 2 else "tiny"
    language = sys.argv[3] if len(sys.argv) > 3 else "en"

    app = AudioTranscriberApp()
    try:
        app.main(audio_file_path, model_name, language)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
    else:
        print("Transcription and summarization completed successfully.")
        print(f"Transcription saved to {os.path.splitext(audio_file_path)[0]}_transcription.txt")
        print(f"Summary saved to {os.path.splitext(audio_file_path)[0]}_summary.txt")
        sys.exit(0)

