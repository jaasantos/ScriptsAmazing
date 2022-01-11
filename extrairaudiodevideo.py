from moviepy.editor import *

mp4_file = "JM.mp4"
mp3_file = "JM.mp3"

videoclip = VideoFileClip(mp4_file)
audioclip = videoclip.audio

audioclip.write_audiofile(mp3_file)
audioclip.close()
videoclip.close()
