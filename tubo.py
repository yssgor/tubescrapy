# IMPORTS
from youtube import Youtube
from channel import Channel
from playlist import Playlist
from video import Video
from comment import Comment


""" import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-channel", "--channel", dest="channel", required=True, type=str, action="store", help="Channel name")

parser.add_argument("-t", "--time", dest="time", required=True, type=str, action="store", help="Type time get comments")

parser.add_argument("-hours", "--hours", dest="qtd_hours", required=True, default=12, action="store", help="Hours get comments")

parser.add_argument("-index", "--index", dest="index", required=True, type=str, action="store", help="Index opensearch get comments")

parser.add_argument("-u", "--username", dest="username", type=str, action="store", help="User name Opensearch")

parser.add_argument("-p", "--password",  dest="password", type=str, action="store", help="User password Opensearch") """

if __name__ == '__main__':

    # Definições de canal e API
    api = Youtube('AIzaSyBNom0ROPKzOuM2Md90_vOzMJ6E_QJwp5Y')
    channel = Channel("JovemNerd")

    # Captura dados do canal e id da playlist uploads
    channel.get_details(api)
    playlist = Playlist(channel.playlistuploads)

    # Capturar dados dos videos na playlist uploads
    videos = playlist.get_upload_playlist(api)
    
    videos_info = []
    comments = []

    for video in videos:
        comment = Comment(video['snippet']['resourceId']['videoId'])
    