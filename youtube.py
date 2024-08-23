from googleapiclient.discovery import build

class Youtube():
    def __init__(self, api_key):
        self.tubo = build('youtube', 'v3', developerKey=api_key)