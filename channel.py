class Channel():
    def __init__(self, name) -> None:
        self.name = name
        self.id = ''
        self.title = ''
        self.description = ''
        self._customUrl = ''
        self.playlistuploads = ''

    def get_details(self, api):
        channel = api.tubo.channels().list(part="snippet,contentDetails",forUsername=self.name).execute()
        channel = channel['items'][0]
        self.id = channel['id']
        self.title = channel['snippet']['title']
        self.description = channel['snippet']['description']
        self._customUrl = channel['snippet']['customUrl']
        self.playlistuploads = channel['contentDetails']['relatedPlaylists']['uploads']

    def get_id(self):
        return self.id
    
    def __str__(self):
        return f'id: {self.id}\n title: {self.title}\n description: {self.description}\n customUrl: {self._customUrl}\n playlistUploads: {self.playlistuploads}'