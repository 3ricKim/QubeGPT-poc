import re
import pytube
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter


pattern = re.compile(r"^(https?\:\/\/)?(www\.)?(youtube\.com|youtu\.?be)\/.+") 

def is_youtube_url(url):
    return pattern.match(url) is not None

def get_youtube_id(url):
    if is_youtube_url(url):
        if "youtu.be" in url:
            return url.split("/")[-1].split("?")[0]
        else:
            return url.split("v=")[-1].split("&")[0]
    else:
        return None

def get_youtube_title(url):
    if is_youtube_url(url):
        yt = pytube.YouTube(url)
        return yt.title
    else:
        return None
def get_transcript(url):
    if is_youtube_url(url):
        yt_id = get_youtube_id(url)
        transcript_list = YouTubeTranscriptApi.list_transcripts(yt_id)
        en_subtitles = [t.language_code for t in transcript_list if t.language_code.startswith('en')]
        ko_subtitles = [t.language_code for t in transcript_list if t.language_code.startswith('ko')]

        return YouTubeTranscriptApi.get_transcript(yt_id, languages=en_subtitles)
    else:
        return None

def get_transcript_text(raw_transcript):
    formatter = TextFormatter()
    return formatter.format_transcript(raw_transcript)

if __name__ == '__main__':
    url = input("Enter a YouTube URL: ").strip()
    transcript = get_transcript(url)
    if transcript is not None:
        with open('./export/' + get_youtube_title(url) + ".txt", "w") as f:
            transcript_text = get_transcript_text(transcript).split('\n')
            text = ' '.join(transcript_text)
            f.write(text)
            print("Transcript saved to ./export/" + get_youtube_title(url) + ".txt")
    else:
        print("Invalid YouTube URL")

   

