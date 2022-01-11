from redvid import Downloader

reddit = Downloader(max_q=True)
reddit.url = 'https://v.redd.it/c8oic7ppc2751'
reddit.download()