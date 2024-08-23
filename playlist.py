class Playlist():
    def __init__(self, id):
        self.id = id
        self.videos = ''
    
    def get_upload_playlist(self, api):
        self.videos = api.tubo.playlistItems().list(playlistId=self.id, part='snippet', maxResults=50).execute()
        return self.videos['items']