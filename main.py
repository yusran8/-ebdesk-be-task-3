from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from scrapping import youtubeAPI
from search import SearchVideo
import json

app = Flask(__name__)


app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'TerminateItself99'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_DB'] = 'ebdesk'

app.config['JSON_SORT_KEYS'] = False

mysql = MySQL(app)


@app.route('/insert', methods=['POST', 'GET'])
def insert():
    cursor = mysql.connection.cursor()
    API = youtubeAPI()
    API.buildConnection()
    datas = API.getData()

    sql = "insert into videos(channel_id, title, channel_name, waktu_publish) values (%s, %s, %s, %s)"

    for data in datas:
        channel_id = data['channel_id']
        title = data['title']
        channel_name = data['channel_name']
        waktu_publish = data['waktu_publish']
        value = (channel_id, title, channel_name, waktu_publish)

        cursor.execute(sql, value)
        mysql.connection.commit()
    
    response = jsonify('insert data successfully. go to /show to view data')
    response.status_code = 200

    return response

@app.route('/update/<int:id>', methods=['PUT', 'GET'])
def update(id):
    json = request.json
    _id = id
    _channel_id = json['channel_id']
    _title = json['title']
    _channel_name = json['channel_name']
    _waktu_publish = json['waktu_publish']

    if _id and _channel_id and _title and _channel_name and _waktu_publish and request.method=='PUT':

        cursor = mysql.connection.cursor()
        sql = 'update videos SET channel_id=%s, title=%s, channel_name=%s, waktu_publish=%s where id=%s'
        value = (_channel_id, _title, _channel_name, _waktu_publish, _id)

        cursor.execute(sql, value)
        mysql.connection.commit()

    response = jsonify('update data successfully. go to /show to view data')
    response.status_code = 200

    return response

@app.route('/delete/<int:id>', methods=['DELETE', 'GET'])
def delete(id):
    cursor = mysql.connection.cursor()

    cursor.execute("DELETE from videos where id=%s", (id,))
    mysql.connection.commit()

    response = jsonify('deleted data with id=' + str(id))
    response.status_code = 200

    return response

@app.route('/show', methods=['GET'])
def show():
    cursor = mysql.connection.cursor()
    cursor.execute("select * from videos")
    header = [column[0] for column in cursor.description]
    rows = cursor.fetchall()
    json_data = []
    for res in rows:
        json_data.append(dict(zip(header, res)))

    return jsonify(json_data)

@app.route('/showBYwaktu', methods=['GET'])
def show_by_waktu():
    cursor = mysql.connection.cursor()
    cursor.execute("select * from videos order by waktu_publish desc")
    header = [column[0] for column in cursor.description]
    rows = cursor.fetchall()
    json_data = []
    for res in rows:
        json_data.append(dict(zip(header, res)))

    return jsonify(json_data)

@app.route('/search', methods=['POST', 'GET'])
def search():

    query = request.query_string.decode()
    query = query.partition("=")[2]

    API = SearchVideo(query)
    API.buildConnection()
    datas = API.getData()

    sql = "insert into videos(channel_id, title, channel_name, waktu_publish) values (%s, %s, %s, %s)"
    cursor = mysql.connection.cursor()

    for data in datas:
        channel_id = data['channel_id']
        title = data['title']
        channel_name = data['channel_name']
        waktu_publish = data['waktu_publish']
        value = (channel_id, title, channel_name, waktu_publish)

        cursor.execute(sql, value)
        mysql.connection.commit()

    response = jsonify('insert data successfully. go to /show to view data')
    response.status_code = 200

    return response

if __name__ == "__main__":
    app.run()
