# Simple full stack application
## Tech Stack

JS - React<br>
Python - Bottle<br>
DB - pymysql (MySQL)<br>

## Build App and Install Depedencies
### Back End:
```

Install the DB (located in workshopdb.sql)

$ cd workshop-be

// Create VENV 
$ python -m venv venv

// Activate VENV
$ . venv/Scripts/activate

// Install depedencies
$ pip install -r requirments.txt
```
### Front End:
```
$ cd workshop-fe

// Install depedencies
$ npm install

// Run the build
$ npm run build
```

### Launch app
```
$ cd workshop-be
$ python main.py

// visit http://localhost:4000 on your nearest browser
```
