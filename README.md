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

3. **(Optional) Enable Google Generative AI Summarization**  
    - To use Google Generative AI for transcript summarization, add your API key to a `.env` file:
        ```
        GOOGLE_API_KEY=your_google_api_key_here
        ```
    - The script will automatically detect the API key and generate a summary of the transcript using Google Generative AI.
    ## Usage

    Start the FastAPI server:

    ```bash
    uvicorn app:app --reload
    ```

    ### API Endpoints

    #### Transcribe Audio

    - **POST** `/transcribe`
      - **Request**: Multipart/form-data with an audio file.
      - **Optional Query Parameters**:
        - `model`: Whisper model name (`tiny`, `base`, `small`, `medium`, `large`). Default: `tiny`
        - `language`: Language code for transcription (e.g., `en`, `fr`, `es`). Default: `en`
      - **Response**: JSON with the transcript.

    **Example using `curl`:**

    ```bash
    curl -X POST "http://localhost:8000/transcribe?model=tiny&language=en" \
      -F "file=@/path/to/audio.mp3"
    ```


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.