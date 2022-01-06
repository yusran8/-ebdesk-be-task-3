# ebdesk-be-task-3
## REST API CRUD to mysql

### Running the server
1. Install `requirements.txt` using `pip install -r requirements.txt`
2. Make sure you have connection to mysql database. You can change the database detail in `main.py` 
3. run `main.py` to run the server.

### Testing server
1. Best to use `postman` for testing. download [here](https://www.postman.com/downloads/). or you can use browser.
> note : some feature might not be able to run properly if test using browser
2. use URL `localhost:5000/insert` using `GET` methods to insert scrapped data from youtube into database
3. use URL `localhost:5000/update/<id>` to update data by id using methods `PUT` with Request Body like below:
```
{
  "channel_id" : <new_channel_id>
  "title" : <new_title>
  "channel_name" : <new_channel_name>
  "waktu_publish" : <new waktu_publish>
}
```
4. use URL `localhost:5000/delete/<id>` using `DELETE` methods to delete data by id
5. use URL `localhost:5000/show` using `GET` methods to show all data in table
6. use URL `localhost:5000/showBYwaktu` using `GET` methods to show all data sorted by published time in descending order.
7. use URL `localhost:5000/search?query=<keyword>` using `POST` methods to scrapped a new video from youtube with inputted keyword and insert data to database.
