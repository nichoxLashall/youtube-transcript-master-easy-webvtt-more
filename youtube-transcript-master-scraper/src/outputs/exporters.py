thonimport json

def export_transcript(url, transcript, metadata):
    output_path = f"data/{url.split('=')[1]}.json"
    data = {
        "url": url,
        "language": "en",
        "title": metadata["title"],
        "duration": metadata["duration"],
        "uploadDate": metadata["uploadDate"],
        "text": transcript,
    }

    with open(output_path, "w") as f:
        json.dump(data, f, indent=4)