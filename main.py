print("Welcome to NeuralNine YouTube Downloader and Converter v0.2 Alpha")
print("Loading...")

import youtube_downloader

print('''
What do you want?

(1) Download a YouTube Playlist (MP3)
''')

choice = input("Choice: ")

if choice == "1":
    link = input("Enter the link to the playlist: ")

    print("Downloading playlist...")
    youtube_downloader.download_playlist(link)
    print("Download finished!")

else:
    print("Invalid input! Terminating...")