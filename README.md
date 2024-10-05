# Project no longer works, everything moved to a newly improved version of this.  [https://github.com/fm-frga/AudioDownloader](https://github.com/fm-frga/AudioDownloader)


# YouTube Playlist MP3 Downloader

YouTube Playlist MP3 Downloader is a Python script that allows you to download an entire YouTube playlist and convert the videos into MP3 format. The application uses the [yt-dlp](https://github.com/yt-dlp/yt-dlp) library for downloading and converting the videos and the Kivy framework for creating a simple graphical user interface (GUI).

## Features

- Download an entire YouTube playlist.
- Convert downloaded videos to MP3 format.
- Simple and intuitive graphical user interface.

## Prerequisites

- Python 3.6 or higher
- FFmpeg
- Kivy

## Installation

1. Install Python if you don't have it already. You can download the installer from the official [Python website](https://www.python.org/downloads/).

2. Install FFmpeg. You can download the appropriate version for your operating system from the official [FFmpeg website](https://www.ffmpeg.org/download.html). Follow the installation instructions provided for your platform.

3. Install `Kivy` using pip: 
```
pip install kivy
```

4. Install `yt_dlp` using pip:
```
pip install yt-dlp 
```
5. Clone the repository or download the script:
```
git clone https://github.com/fm-frga/youtube-playlist-mp3-downloader.git
```

## Usage


1. Navigate to the directory containing the script:
```
cd youtube-playlist-mp3-downloader
```

2. Run the script:
```
python main.py
```


3. Enter the URL of the YouTube playlist you want to download.

4. Click the "Download" button to start the downloading and conversion process.

5. The downloaded MP3 files will be saved in the "YouTube Playlist MP3" folder within your user's "Downloads" directory.

## Troubleshooting

If you encounter any issues during the installation or usage of the application, make sure you have installed all the prerequisites correctly. Ensure that FFmpeg is in your system's PATH, and that you are using a compatible version of Python.

If you still experience issues, please create an issue on the GitHub repository, and provide as much information as possible about the problem you are facing.

## License

This project is licensed under the MIT License. See the [LICENSE](https://opensource.org/license/mit/) file for more details.

