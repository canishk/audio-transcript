Audio file to text transcript using OpenAI Whisper (default: `tiny` model, language: `en`) and ffmpeg


## Installation

1. **Install ffmpeg**  
    - On Ubuntu/Debian:
      ```bash
      sudo apt update
      sudo apt install ffmpeg
      ```
    - On macOS (using Homebrew):
      ```bash
      brew install ffmpeg
      ```

2. **Install Python dependencies**  
    - Create and activate a virtual environment (optional but recommended):
      ```bash
      python3 -m venv venv
      source venv/bin/activate
      ```
    - Install required packages:
      ```bash
      pip install -r requirements.txt
      ```

## Usage

```bash
python app.py <audio_file> [<whisper_model>] [<language_code>]
```

- `<audio_file>`: Path to the input audio file.
- `<whisper_model>`: (Optional) Whisper model name (default: `tiny`; options: `base`, `small`, `medium`, `large`).
- `<language_code>`: (Optional) Language code for transcription (default: `en`; e.g., `en`, `fr`, `es`).

The script processes the audio and outputs a transcribed `.txt` file.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.