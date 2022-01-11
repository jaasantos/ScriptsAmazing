'''

import youtube_dl


ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=Sc2BK09eKhk&list=RDnxEkRwNrACg&index=4'])

print('download success')

'''


# YouTube video link
import youtube_dl
link = input('Enter the link of the video: ')


youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'}).download([f'{link}'])

print('download realizado com sucesso!')
