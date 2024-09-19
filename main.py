import os
import subprocess
import yt_dlp

def download_youtube_video(url, output_path):
    # yt-dlp options for downloading the video
    ydl_opts = {
        'format': 'best',  # Download the best quality video
        'outtmpl': output_path  # Specify the download path and filename
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def trim_video(input_file, start_time, end_time, output_file):
    # ffmpeg command to trim the video
    command = [
        'ffmpeg', '-i', input_file,  # Input file
        '-ss', start_time,  # Start time
        '-to', end_time,  # End time
        '-c', 'copy',  # Copy the video and audio without re-encoding
        output_file  # Output file path
    ]
    subprocess.run(command)

def main():
    # Get user input
    video_url = input("Enter YouTube video URL or Shorts URL: ")
    start_time = input("Enter start time (in format HH:MM:SS): ")
    end_time = input("Enter end time (in format HH:MM:SS): ")
    
    # Define paths for input and output
    download_folder = '/storage/emulated/0/Download/'  # Mobile Download folder path
    downloaded_video = os.path.join(download_folder, 'video.mp4')  # Temp file for downloaded video
    trimmed_video = os.path.join(download_folder, 'trimmed_video.mp4')  # Output file for trimmed video

    # Download the YouTube video
    print("Downloading video...")
    download_youtube_video(video_url, downloaded_video)

    # Trim the video using ffmpeg
    print("Trimming video...")
    trim_video(downloaded_video, start_time, end_time, trimmed_video)

    print(f"Trimmed video saved as: {trimmed_video}")

if __name__ == "__main__":
    main()
