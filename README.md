# Test work for Numbers
- Python skript for [document](https://docs.google.com/spreadsheets/d/1h_7txa8JYjEz_oQznGaMhvbkUBUXJqi3IpIVDA1WC9g/edit#gid=0) in Google sheets.
- [Text of tasks](https://soldigital.notion.site/soldigital/developer-5b79683045a64129a2625a19bfb0c944)

## Technology
- [Python](https://www.python.org/)
- [flask](https://flask.palletsprojects.com/en/2.1.x/)
- [gspread](https://docs.gspread.org/en/latest/)

## Usage
1. Install the used libraries into your virtualenv with the command:
```sh
pip install requiremenst.txt
```
2. Create db
- Import db variable from app. After using the command to create a database
```py
from app import db

db.create_all()
```


### Starting the Development server
To start the development server, run the command:
```sh
python app.py runserver
```

### Working with skript
The server will be launched at [address](http://127.0.0.1:5000/).
To test the functionality, add an element to the [table](https://docs.google.com/spreadsheets/d/1h_7txa8JYjEz_oQznGaMhvbkUBUXJqi3IpIVDA1WC9g/edit#gid=0).

