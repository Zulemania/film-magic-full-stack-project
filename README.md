## CASTING AGENCY API

## Introduction

The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies.  The Casting agency API supports the agency by allowing users to query the database for movies and actors. There are three different roles and each has a set of related permissions attached to them.

These Roles include:
1. Casting Assistant
    - Can view actors and movies
2. Casting Director
    - All permiissions a Casting Assistant has and...
    -  Add or delete an actor from the database
    - Modify actors or movies
3. Executive Producer
    - All permissions the Casting Director has and...
    - Add or delete a movie from the database

I developed this project to use all the concepts and skill that I acquired in this programme to build an API and host it. By doing so, I gained more confidence in these skills.

## PROJECT MOTIVATION

- The primary motivation for this project was to use the hands-on knowledge that I acquired in this program to develop a functional app, thereby gaining more confidence in my skill set as a software engineer

## Capstone Project for Udacity's Full Stack Developer Nanodegree

Heroku link: https://film-magic.herokuapp.com/

Local host link: http://127.0.0.1:5000/


## SETUP

## Installinq Dependencies

1. **Python 3.9.8** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)


2. **Virtual Environment** - We recommend working within a Virtual environment whenever using Python for projects. This keeps the dependencies for each project seperate and organized. Instructions for setting up a virtual environment can be found in [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

3. **PIP Dependencies** - Once you have your virtual environment setup and running, install dependencies by runnung:
```bash
pip install -r requirements.txt
```
This will install all of the required packages we selected within the `requirements.txt` file.


4. **Key Dependencies**
 - [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

 - [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

 - [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

### Deploy on Heroku
 - Create app in heroku
 - Set your environment variables
 - Define your Procfile
 - Push your code to github
 - Connect your repository to heroku
 - Click on the deploy option

### Running the server

First, you have to start the postgresql service by running the following command

```bash
brew services start postgresql
```

Then, create database by running
```
dropdb capstone
createdb capstone
```

From within the ./capstone directory first ensure you are working within your created virtual environment.

Each time you open a new terminal session, run:

```bash
export DATABASE_URL=postgresql:cynthiachisom@localhost:5432/capstone
export FLASK_APP=app.py;
export AUTH0_DOMAIN='capstone-projekt.us.auth0.com'
export ALGORITHMS=['RS256']
export API_AUDIENCE='magic'
export CLIENT_ID='06lGES4xRP9Z7cZu6Uyj52iyK7bCq5Pw'
```

To run the server, execute:

```bash
export FLASK_ENV=development
flask run
```

The `FLASK_ENV` variable to `development` flag will detect file changes and restart server automatically.


## ENDPOINTS

GET ' / '
- root endpoint
- requires no authentication
- Example request: https://film-magic.herokuapp.com/
- Example response:
```
{
    "success": true,
    "message":"Finally, it works!!!"
}
```

GET '/actors'
- Get all the actors on the list
- requires "get:actors" permission
- Example request: curl -XGET -H "Authorization: Bearer ${CASTING_ASSISTANT}" https://film-magic.herokuapp.com/actors
- Example request: curl -XGET -H "Authorization: Bearer ${EXECUTIVE_PRODUCER}" http://127.0.0.1:5000/actors
- Example response:
```
{"actors":[
    {
        "gender":"M",
        "id":2,
        "name":"Denzel"
    },
    {
        "gender":"M","id":3,
        "name":"Mofesola Babalola"
    },
    {
        "gender":"M",
        "id":5,
        "name":"Ed Helms"
    },
    {
        "gender":"M",
        "id":6,
        "name":"Tom Hardy"
    },
    {
        "gender":"M",
        "id":7,
        "name":"Denzel"
    },
    {
        "gender":"M",
        "id":8,
        "name":"Denzel"
    },
    {
        "gender":"M",
        "id":9,
        "name":"Denzel"
    },
    {
        "gender":"M",
        "id":11,
        "name":"Denzel"
    },
    {
        "gender":"M",
        "id":12,
        "name":"Denzel"
    },
    {
        "gender":"M",
        "id":13,
        "name":"Denzel"
    },
    {
        "gender":"M",
        "id":14,
        "name":"Denzel"
    },
    "success":true
}
```

GET '/actors/{actor_id}
- Get a particular actor on the list
- requires "get:actors-detail" permission
- Example request: curl -XGET -H "Authorization: Bearer ${CASTING_ASSISTANT}" https://film-magic.herokuapp.com/actors/1
- Example response:
```
{
    "actor":{
        "gender":"M",
        "id":1,
        "name":"Denzel"},
    "success":true
}
```

POST '/actors
- Add a new actor to the list
- requires "post:actor" permission
- Example request: curl -XPOST -H "Authorization: Bearer ${CASTING_DIRECTOR}" https://film-magic.herokuapp.com/actors
- Request Body:
{
    "name": "Mofesola Babalola",
    "age": 32,
    "gender": 'M'

}

- Example Response:
```
{
    "success": true,
}
```

GET '/movies'
- Get all the movies on the list
- requires "get:movies" permission
- Example request: curl -XGET -H "Authorization: Bearer ${CASTING_ASSISTANT}" https://film-magic.herokuapp.com/movies
- Example request: curl -XGET -H "Authorization: Bearer ${EXECUTIVE_PRODUCER}" http://127.0.0.1:5000/actors
- Example response:
```
{
  "movies": [
    {
      "id": 2, 
      "release_year": "Fri, 19 Apr 2019 00:00:00 GMT", 
      "title": "Joker"
    }, 
    {
      "id": 4, 
      "release_year": "Fri, 05 Apr 2019 00:00:00 GMT", 
      "title": "Eran Iya Osogbo"
    }, 
    {
      "id": 5, 
      "release_year": "Fri, 15 May 2015 00:00:00 GMT", 
      "title": "Mad max"
    }, 
    {
      "id": 6, 
      "release_year": "Wed, 29 Jul 2015 00:00:00 GMT", 
      "title": "Vacation"
    }, 
    {
      "id": 7, 
      "release_year": "Fri, 05 Apr 2019 00:00:00 GMT", 
      "title": "Coming"
    }, 
    {
      "id": 8, 
      "release_year": "Fri, 05 Apr 2019 00:00:00 GMT", 
      "title": "Coming"
    }, 
    {
      "id": 9, 
      "release_year": "Fri, 05 Apr 2019 00:00:00 GMT", 
      "title": "new title"
    }, 
    {
      "id": 11, 
      "release_year": "Fri, 05 Apr 2019 00:00:00 GMT", 
      "title": "new title"
    }, 
    {
      "id": 12, 
      "release_year": "Fri, 05 Apr 2019 00:00:00 GMT", 
      "title": "new title"
    }, 
    {
      "id": 13, 
      "release_year": "Fri, 05 Apr 2019 00:00:00 GMT", 
      "title": "new title"
    }, 
    {
      "id": 14, 
      "release_year": "Fri, 05 Apr 2019 00:00:00 GMT", 
      "title": "new title"
    }, 
    {
      "id": 15, 
      "release_year": "Fri, 05 Apr 2019 00:00:00 GMT", 
      "title": "new title"
    }, 
    {
      "id": 16, 
      "release_year": "Fri, 05 Apr 2019 00:00:00 GMT", 
      "title": "new title"
    }, 
    {
      "id": 17, 
      "release_year": "Fri, 05 Apr 2019 00:00:00 GMT", 
      "title": "new title"
    }, 
    {
      "id": 18, 
      "release_year": "Fri, 05 Apr 2019 00:00:00 GMT", 
      "title": "new title"
    }, 
    {
      "id": 19, 
      "release_year": "Fri, 05 Apr 2019 00:00:00 GMT", 
      "title": "new title"
    }
  ], 
  "success": true
}
```

GET '/movies/{movie_id}
- Get a particular movie on the list
- requires "get:movies-detail" permission
- Example request: curl -XGET -H "Authorization: Bearer ${CASTING_ASSISTANT}" https://film-magic.herokuapp.com/movies/5
- Example request: curl -XGET -H "Authorization: Bearer ${EXECUTIVE_PRODUCER}" http://localhost:5000/movies/5
- Example response:

```
{
    "movie":{
        "id":5,
        "release_year":"Fri, 15 May 2015 00:00:00 GMT",
        "title":"Mad max"
    },
    "success":true
}
```



## TESTING

For testing the app, run the following commands () 
```
dropdb capstone
createdb capstone
psql capstone < capstone.psql
python test.py
```