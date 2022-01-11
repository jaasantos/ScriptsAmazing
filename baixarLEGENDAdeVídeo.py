from youtube_transcript_api import YouTubeTranscriptApi


srt = YouTubeTranscriptApi.get_transcript('ywIKQLRsdGw')  #link do youtube
with open('srt_file.txt','w') as f:
     for i in srt:
         f.write('%s\n' % i)
