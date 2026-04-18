import yt_dlp
import imageio_ffmpeg


def get_ffmpeg():
    return imageio_ffmpeg.get_ffmpeg_exe()


def get_opts():
    return {
        # audio only
        "format": "bestaudio/best",

        # ffmpeg path
        "ffmpeg_location": get_ffmpeg(),

        # playlist folder structure
        "outtmpl": "%(playlist_title|Single)s/%(playlist_index|)02d - %(title)s.%(ext)s",

        # thumbnail + metadata
        "writethumbnail": True,

        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            },
            {"key": "FFmpegMetadata"},
            {"key": "EmbedThumbnail"},
        ],

        "quiet": False,
    }


def download_playlist(playlist_url):
    # quality kept for future use (ignored for now)
    with yt_dlp.YoutubeDL(get_opts()) as ydl:
        ydl.download([playlist_url])