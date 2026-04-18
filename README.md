````markdown
# 📥 NeuralNine YouTube Downloader & Converter v0.2 Alpha

A simple Python tool that downloads **YouTube playlists** and automatically converts them into **MP3 files with metadata and thumbnails** using `yt-dlp` and `ffmpeg`.

---

## 🚀 Features

- 🎵 Download full YouTube playlists  
- 🎧 Convert videos to MP3 (192kbps)  
- 🖼️ Embed thumbnails into audio files  
- 🏷️ Add metadata (title, artist where available)  
- 📁 Automatically organize files by playlist  
- ⚡ Powered by `yt-dlp` + `ffmpeg`

---

## 📦 Requirements

- Python 3.8+
- yt-dlp
- imageio-ffmpeg

Install dependencies:

```bash
py -m pip install yt-dlp imageio-ffmpeg
````

---

## ▶️ How to Run

```bash
python main.py
```

You will see:

```
What do you want?

(1) Download a YouTube Playlist (MP3)
```

---

## 📥 Usage

### Step 1: Run the program

```bash
python main.py
```

### Step 2: Select option

```
Choice: 1
```

### Step 3: Enter details

```
Please choose a quality (low, medium, high, very high): high
Enter the link to the playlist: https://www.youtube.com/playlist?list=XXXX
```

### Step 4: Done 🎉

Your playlist will be downloaded and converted automatically.

---

## 📁 Output Structure

```
Playlist_Name/
    01 - Video Title.mp3
    02 - Video Title.mp3
    03 - Video Title.mp3
```

---

## ⚙️ How It Works

* Uses `yt-dlp` to extract playlist videos
* Downloads best available audio
* Converts audio to MP3 using FFmpeg
* Embeds metadata + thumbnails
* Saves files in organized folders

---

## 🧠 Notes

* The **quality option is currently not used** (reserved for future upgrades)
* Only playlist downloads are supported in this version
* FFmpeg is handled automatically via `imageio-ffmpeg`

---

## 🛠️ Project Structure

```
youtube-downloader/
│
├── main.py
├── youtube_downloader.py
└── README.md
```

---

## 🔮 Future Improvements

* 🎚️ Real audio quality control (128 / 192 / 320 kbps)
* 📊 Download progress bar
* ⏯️ Resume interrupted downloads
* 🎵 Single video download mode
* 🖥️ GUI version (Tkinter / Electron)

---

## ⚠️ Disclaimer

This project is for **educational purposes only**.
Please respect YouTube’s Terms of Service and copyright laws.

---

## 👨‍💻 Author

Built as a Python learning project inspired by NeuralNine-style tutorials.
