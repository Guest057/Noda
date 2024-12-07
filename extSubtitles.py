import yt_dlp
import whisper

import uuid

def download_video(youtube_url, output_dir="./downloaded"):
    
    random_filename = f"{uuid.uuid4().hex}.mp4"
    output_path = f"{output_dir}/{random_filename}"
    
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': output_path,
        'merge_output_format': 'mp4',
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }],
        'quiet': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])
    
    return output_path

def extract_subtitles(video_path):
    model = whisper.load_model("base")
    result = model.transcribe(video_path)
    return result.get("text", "")
