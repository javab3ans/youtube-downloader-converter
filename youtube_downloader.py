import yt_dlp
import imageio_ffmpeg

def get_ffmpeg():
    return imageio_ffmpeg.get_ffmpeg_exe()

def get_opts():
    return {
        "format": "bestaudio/best",
        "ffmpeg_location": get_ffmpeg(),

        # Smart folder + numbering
        "outtmpl": "%(playlist_title|Single)s/%(playlist_index|01)02d - %(title)s.%(ext)s",

        # Album art
        "writethumbnail": True,

        # Try to parse artist/title
        "parse_metadata": [
            "%(artist)s - %(title)s"
        ],

        # MP3 + metadata + artwork
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            },
            {"key": "FFmpegMetadata"},
            {"key": "EmbedThumbnail"},
        ],

        "embed_metadata": True,
        "quiet": False,
    }

def download_video(url, quality):
    ydl_opts = get_opts()
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def download_videos(urls, quality):
    for url in urls:
        download_video(url, quality)

def download_playlist(playlist_url, quality):
    ydl_opts = get_opts()
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])

def input_links():
    links = input("Enter URL(s) (comma separated): ")
    return [link.strip() for link in links.split(",")]