import os
import yt_dlp
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.anchorlayout import AnchorLayout
from pathlib import Path

downloads_folder = str(Path.home() / "Downloads")
playlist_folder = os.path.join(downloads_folder, "YouTube Playlist MP3")

if not os.path.exists(playlist_folder):
    os.mkdir(playlist_folder)

Window.size = (600, 400)

def download_playlist(playlist_url):
    outtmpl = os.path.join(playlist_folder, "%(title)s.%(ext)s")

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': outtmpl,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'prefer_ffmpeg': True,
        'ignoreerrors': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])

class MainWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"

        welcome_label = Label(text='YouTube Playlist Downloader', font_size=36, size_hint_y=None, height=50)
        self.add_widget(welcome_label)

        function_label = Label(text='Completely download a YouTube playlist and converts the files as MP3.', font_size=18, size_hint_y=None, height=100)
        self.add_widget(function_label)

        self.playlist_link_input = TextInput(hint_text='Enter playlist link...', multiline=False, size_hint_y=None, height=40, font_size=18, size_hint_x=None, width=400)
        
        input_layout = AnchorLayout(anchor_x='center', anchor_y='top', size_hint_y=None, height=50)
        input_layout.add_widget(self.playlist_link_input)
        self.add_widget(input_layout)

        download_button = Button(text='Download', on_press=self.on_download_clicked, size_hint_y=None, height=50, size_hint_x=1)

        exit_button = Button(text='Exit', on_press=exit, size_hint_y=None, height=50, size_hint_x=1)

        buttons_layout = BoxLayout(orientation='horizontal', spacing=50, size_hint_y=None, height=50, size_hint_x=None, width=Window.width/2)
        buttons_layout.add_widget(download_button)
        buttons_layout.add_widget(exit_button)

        buttons_anchor_layout = AnchorLayout(anchor_x='center', anchor_y='top', size_hint_y=None, height=160)
        buttons_anchor_layout.add_widget(buttons_layout)
        self.add_widget(buttons_anchor_layout)


    def on_download_clicked(self, instance):
        playlist_link = self.playlist_link_input.text
        if not playlist_link:
            popup = Popup(title='Error', content=Label(text='Please enter a playlist link.'), size_hint=(None, None), size=(300, 150))
            popup.open()
        else:
            download_playlist(playlist_link)
            popup = Popup(title='Success', content=Label(text='Downloading playlist...'), size_hint=(None, None), size=(300, 150))
            popup.open()

class PlaylistDownloaderApp(App):
    def build(self):
        return MainWindow()

if __name__ == '__main__':
    PlaylistDownloaderApp().run()