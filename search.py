from googleapiclient.discovery import build
import json

api_key = "AIzaSyCZ2BBpo0nDibNrZm1wqAXfFVrLoWS9w6o"

class SearchVideo():
    def __init__(self, query):
        self.query = query

    def buildConnection(self):
        yt = build('youtube', 'v3', developerKey=api_key)

        req = yt.search().list(
            part="snippet",
            maxResults=1,
            q=self.query
        )
        self.response = req.execute()

    def getData(self):
        datas = self.response.get('items', [])
        self.list_video=[]
        for data in datas:
            channel_id = data['snippet']['channelId'].strip()
            title = data['snippet']['title'].strip()
            channel_name= data['snippet']['channelTitle'].strip()
            waktu_publish = data['snippet']['publishedAt'].strip()   
            
            video= {'channel_id': channel_id, 'title':title, 'channel_name':channel_name, 'waktu_publish': waktu_publish}
            self.list_video.append(video)
            
        return self.list_video

if __name__ == "__main__":
    API = SearchVideo('kaguya')
    API.buildConnection()
    data = API.getData()
    print(data)
