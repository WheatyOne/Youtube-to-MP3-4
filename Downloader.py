import tkinter as tk
from pytube import YouTube
import os
from pathlib import Path

downloads = Path.home() / 'Downloads'
downloads = str(downloads).replace('\\', '\\\\')

window = tk.Tk()
window.resizable(False, False)

def downloadVideo():
    print(str(choice.get()))
    video = YouTube(urlEntry.get())
    if choice.get() == 1:
        video = video.streams.get_highest_resolution()
        video.download(downloads)

    elif choice.get() == 2:
        video = video.streams.filter(only_audio = True).first()
        fileOne = video.download(downloads)
        base, ext = os.path.splitext(fileOne)
        fileTwo = base + '.mp3'
        os.rename(fileOne, fileTwo)


text = tk.StringVar()
text.set('Enter URL here')

choice = tk.IntVar()
choice.set(1)

urlEntry = tk.Entry(window, textvariable = text, width = 30, bd = 2)
urlEntry.place(x = 52, y = 75)

confirmBtn = tk.Button(window, text = "Download", fg = 'black', command = downloadVideo)
confirmBtn.place(x = 285, y = 70)

choiceOne = tk.Radiobutton(window, text = "MP4", variable = choice, value = 1)
choiceTwo = tk.Radiobutton(window, text = "MP3", variable = choice, value = 2)
choiceOne.place(x = 47, y = 30)
choiceTwo.place(x = 127, y = 30)

window.title('Youtube Downloader')
window.geometry('400x150')
window.mainloop()
