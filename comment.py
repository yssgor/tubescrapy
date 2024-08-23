class Comment():
    def __init__(self, video_id):
        self.video_id = video_id
        self.content = ''
        self.user = ''
        self.date = ''
        self.vote = ''
        self.replie = ''

    def get_replies(self, comment):
        comment_replies = []
        if comment['kind'] == 'youtube#commentThread' and comment['snippet'].get('totalReplyCount') and comment.get('replies'):
            replies = comment['replies']['comments']
            for reply in replies:
                reply_info = reply['snippet']
                comment_replies.append({'Conteúdo': reply_info['textOriginal'], 'Usuário': reply_info['authorDisplayName'],
                                        'Horário': reply_info['publishedAt'], 'Votos': reply_info['likeCount'], 'Respostas': self.get_replies(reply)})

        return comment_replies
    
    def get_comments(self, api):
        page_token = ''
        comments = []
        get_next_page = True

        try:
            while get_next_page:
                comments_info = api.tubo.commentThreads().list(
                    videoId=self.video_id, part='snippet,replies', maxResults=50, pageToken=page_token).execute()

                for comment in comments_info['items']:
                    comment_info = comment['snippet']['topLevelComment']['snippet']

                    replies = self.get_replies(comment)
                    self.content = comment_info['textOriginal']
                    self.user = comment_info['authorDisplayName']
                    self.date = comment_info['publishedAt']
                    self.vote = comment_info['likeCount']
                    self.replie = replies

                    comments.append(self.content, self.user, self.date, self.vote, self.replie)

                page_token = comments_info.get('nextPageToken')

                if not page_token:
                    get_next_page = False

            
        except Exception as e:
            print('Comentários bloqueados')