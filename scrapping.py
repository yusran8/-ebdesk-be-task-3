from googleapiclient.discovery import build
import json

api_key = "AIzaSyCZ2BBpo0nDibNrZm1wqAXfFVrLoWS9w6o"

class youtubeAPI():
    def buildConnection(self):
        yt = build('youtube', 'v3', developerKey=api_key)

        req = yt.videos().list(
            part='snippet,contentDetails,statistics',
            chart="mostPopular",
            regionCode="ID",
            maxResults=20
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

    # for video in list_video:
    #     print(video)
    def to_json(self, data, filename):
    
        with open(filename, 'w') as f:
            json.dump(data, f)

if __name__ == "__main__":
    API = youtubeAPI()
    API.buildConnection()
    data = API.getData()
    API.to_json(data, 'mostpopular.json')