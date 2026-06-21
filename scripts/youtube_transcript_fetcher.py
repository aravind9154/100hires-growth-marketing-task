from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs
import os

def get_video_id(url):
    parsed = urlparse(url)

    if parsed.hostname in ["www.youtube.com", "youtube.com"]:
        return parse_qs(parsed.query)["v"][0]

    elif parsed.hostname == "youtu.be":
        return parsed.path[1:]

    return None

def save_transcript(video_url, output_file):
    video_id = get_video_id(video_url)

    transcript = YouTubeTranscriptApi.get_transcript(video_id)

    with open(output_file, "w", encoding="utf-8") as f:
        for item in transcript:
            f.write(item["text"] + "\n")

    print(f"Transcript saved to {output_file}")

if __name__ == "__main__":
    video_url = input("Enter YouTube URL: ")
    filename = input("Enter output filename: ")

    os.makedirs("output", exist_ok=True)

    save_transcript(
        video_url,
        os.path.join("output", filename)
    )
