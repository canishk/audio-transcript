from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

import os
import argparse
import logging

class SummarizerAI:
    def __init__(self, google_api_key=None, logger=None):
        """
        Initialize the SummarizerAI with Google API key.
        
        :param google_api_key: Google API key for accessing the LLM service.
        """
        if google_api_key:
            self.google_api_key = google_api_key
        else:
            load_dotenv()
            self.google_api_key = os.getenv("GOOGLE_API_KEY")
        
        if not self.google_api_key:
            raise ValueError("Google API key is required.")
        
        self.llm = GoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=self.google_api_key, temperature=0.5)
        self.logger = logger or logging.getLogger(__name__)
    
    def summarize_text(self, text):
        """
        Summarize the given text using the LLM.
        
        :param text: The text to summarize.
        :return: Summary of the text."""
        prompt = PromptTemplate.from_template(
            """
            You are a helpful assistant. The following is a raw transcript of a meeting which may contain filler words, incomplete sentences, and grammatical mistakes.

            Your task is to:
            1. Provide a professional, clear, and corrected version of the conversation.
            2. Summarize the key discussion points and any decisions or action items in bullet format.

            Transcript:
            \"\"\"{transcript}\"\"\"

            Return your output in the following format:
            ---
            **Cleaned Transcript:**
            <corrected version here>

            **Summary:**
            - <bullet 1>
            - <bullet 2>
            - ...
            """
        )
        try:
            self.logger.info("Starting summarization process.")
            chain = prompt | self.llm | StrOutputParser()
            return chain.invoke({"transcript": text})
        except Exception as e:
            self.logger.error(f"An error occurred during summarization: {e}")
            raise

    
    def clean_text(self, text):
        """
        Clean the given text by fixing grammatical errors and removing irrelevant noise or filler words.
        
        :param text: The text to clean.
        :return: Cleaned text."""
        try:
            self.logger.info("Starting text cleaning process.")
            prompt = PromptTemplate.from_template(
                "Clean the following transcript by fixing grammatical errors and removing irrelevant noise or filler words:\n\n{transcript}"
            )
            chain = prompt | self.llm | StrOutputParser()
            return chain.invoke({"transcript": text})
        except Exception as e:
            self.logger.error(f"An error occurred during text cleaning: {e}")
            raise
        
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Summarize a transcript using SummarizerAI.")
    parser.add_argument("input_file", help="Path to the input text file containing the transcript.")
    parser.add_argument("output_file", help="Path to the output text file for the summary.")


    args = parser.parse_args()

    with open(args.input_file, "r", encoding="utf-8") as f:
        transcript = f.read()

    summarizer = SummarizerAI()
    summary = summarizer.summarize_text(transcript)

    with open(args.output_file, "w", encoding="utf-8") as f:
        f.write(summary)