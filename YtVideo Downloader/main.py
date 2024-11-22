import yt_dlp
import tkinter as tk
from tkinter import filedialog

# Function to download the video
def download_video(url, save_path):
    try:
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',  # Download the best video and audio available
            'outtmpl': f'{save_path}/%(title)s.%(ext)s',  # Save the file as the video title
            'merge_output_format': 'mp4',  # Ensure the output format is mp4
            'noplaylist': True,  # Avoid downloading playlists
        }

        # Use yt-dlp to download the video
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download completed successfully!")

    except Exception as e:
        print(f"Error during download: {e}")

# Function to open a file dialog and select the save location
def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")
        return folder
    else:
        print("No folder selected.")
        return None

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    # Get the video URL from the user
    video_url = input("Please enter a YouTube URL: ")

    # Get the save directory from the file dialog
    save_dir = open_file_dialog()

    if save_dir:
        print("Started download...")
        download_video(video_url, save_dir)
    else:
        print("Invalid save location. Please try again.")
