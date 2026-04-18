# 🎵 YouTube Downloader & MP3 Converter

A simple Python CLI tool to download YouTube videos, playlists, and convert them into high-quality MP3 files with embedded metadata and album art.

---

## 🚀 Features

* 📥 Download single YouTube videos
* 📂 Download entire playlists (auto-organized)
* 🎧 Convert videos to MP3 automatically
* 🖼️ Embed thumbnail as album art
* 🏷️ Add metadata (artist/title when available)
* 📁 Smart folder structure:

  ```
  Playlist Name/
    01 - Song Title.mp3
    02 - Song Title.mp3
  ```

---

## 🧱 Project Structure

```
.
├── main.py                 # CLI entry point
├── youtube_downloader.py   # Handles downloading & yt-dlp config
├── file_converter.py       # Converts video to MP3 (MoviePy)
```

---

## ⚙️ Requirements

Install dependencies:

```bash
pip install yt-dlp imageio-ffmpeg moviepy pytube
```

---

## ▶️ Usage

Run the program:

```bash
python main.py
```

You’ll see:

```
What do you want?

(1) Download YouTube Videos Manually
(2) Download a YouTube Playlist
(3) Download YouTube Videos and Convert Into MP3
```

---

## 🔧 Options Explained

### 1. Download YouTube Videos Manually

* Input one or more video URLs
* Choose quality (low → very high)

### 2. Download a Playlist

* Paste playlist URL
* Automatically downloads and organizes files

### 3. Download + Convert to MP3

* Downloads best audio
* Converts to `.mp3`
* Embeds metadata + album art

---

## 📌 Notes

* Uses **yt-dlp** for downloading and processing
* Automatically installs/uses FFmpeg via `imageio-ffmpeg`
* Output files are saved in:

  * Playlist folder (if playlist)
  * `Single/` folder (if individual videos)

---

## ⚠️ Known Issues / Improvements

* `file_converter.py` is not currently used in `main.py` (conversion is handled by `yt-dlp`)
* Quality selection is not fully implemented in downloader logic
* No error handling for invalid URLs
* Filename slicing (`filename[:-4]`) may break for non-standard extensions

---

## 🛠️ Future Improvements

* [ ] Add progress bars
* [ ] Improve error handling
* [ ] Support more formats (wav, flac)
* [ ] GUI version (Tkinter or web app)
* [ ] Better metadata parsing

---

## 📄 License

MIT License (or specify your own)

---

## 👤 Author

Built by **javab3ans**

---

## 💡 Tip

For best results, use option **(3)** — it handles everything automatically (download + convert + metadata + album art).