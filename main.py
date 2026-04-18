print("Welcome to NeuralNine YouTube Downloader and Converter v0.2 Alpha")
print("Loading...")

import youtube_downloader


def is_playlist(url: str) -> bool:
    return "list=" in url.lower()


link = input("Enter a YouTube playlist URL: ")

if is_playlist(link):
    print("Playlist detected ✔")
    print("Downloading playlist...")
    youtube_downloader.download_playlist(link)
    print("Download finished!")
else:
    print("❌ This does not look like a playlist URL.")
    print("Make sure it contains 'list=' (YouTube playlist link).")