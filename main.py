from __future__ import unicode_literals
import youtube_dl
youtube_dl.utils.std_headers['Authorization'] = 'Bearer {}'.format(access_token)

ydl_opts = {
    'format': '22/best',
    'outtmpl': '%(title)s.%(ext)s',
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=ElBcq-UtLK8'])
