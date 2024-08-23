class Video():
    def __init__(self, videos):
        self.id = videos['snippet']['resourceId']['videoId']
        self.video = videos['snippet']['title']
        self.date = videos['snippet']['publishedAt']
        self.url = f"https://www.youtube.com/watch?v={videos['snippet']['resourceId']['videoId']}"
    