thonimport json
import os
from extractors.youtube_parser import get_transcript
from outputs.exporters import export_transcript
from config.settings import load_config

def main():
    config = load_config()
    video_urls = config.get("video_urls")
    language = config.get("language", "en")

    for url in video_urls:
        transcript, metadata = get_transcript(url, language)
        if transcript:
            export_transcript(url, transcript, metadata)
        else:
            print(f"Failed to process {url}")

if __name__ == "__main__":
    main()