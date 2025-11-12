thonimport requests
from bs4 import BeautifulSoup
import json

def get_transcript(url, language):
    # Request the YouTube page
    response = requests.get(url)
    if response.status_code != 200:
        return None, None

    soup = BeautifulSoup(response.text, "html.parser")
    video_data = extract_video_metadata(soup)
    transcript = extract_transcript(url, language)

    return transcript, video_data

def extract_video_metadata(soup):
    title = soup.find("meta", {"name": "title"})["content"]
    duration = soup.find("meta", {"itemprop": "duration"})["content"]
    upload_date = soup.find("meta", {"itemprop": "uploadDate"})["content"]

    return {
        "title": title,
        "duration": duration,
        "uploadDate": upload_date,
    }

def extract_transcript(url, language):
    # Placeholder for actual transcript fetching
    return [
        {"start": 0.5, "dur": 3.2, "text": "Segment 1 text"},
        {"start": 3.7, "dur": 2.8, "text": "Segment 2 text"},
    ]