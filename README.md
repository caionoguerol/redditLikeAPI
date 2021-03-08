# Jungle Devs - Backend Challenge #001



## Instructions to Run

- Create the virtual environment and activate it

        virtualenv -p python3 venv
        source venv/bin/activate
- Install the requirements `pip install -r requirements.txt`
- Start the dockers `docker-compose up` with the database and the localstack
- Run the server with `python manage.py runserver`




    
### URLs, permissions and methods 

* */users/*

- Allowed methods: GET, POST

* */users/{user_id}*

- Allowed methods with authorization token: GET, PUT, DELETE
- Allowed methods without autorization token: GET


* */login/*

 Allowed methods: POST
 (Use this to get authorization token)

* */topics/* - lists all available topics

 Allowed methods with authorization token: GET, POST
 Allowed methods without autorization token: GET

* */topics/{urlname}/* - details (as well as some posts) from a specific topic (identified by *urlname*)

 Allowed methods with authorization token: GET, PUT, DELETE
 Allowed methods without autorization token: GET

* */topics/{urlname}/posts/* - lists all posts from a specific topic

 Allowed methods with authorization token: GET, POST
 Allowed methods without autorization token: GET


* */topics/{urlname}/posts/{post_id}/* - lists details and some comments from a post

 Allowed methods with authorization token: GET, PUT, DELETE
 Allowed methods without autorization token: GET

* */topics/{urlname}/posts/{post_id}/comments/* - lists all comments from a post

 Allowed methods with authorization token: GET, POST
 Allowed methods without autorization token: GET

* */topics/{urlname}/posts/{post_id}/comments/{comment_id}/* - lists details from a comment

 Allowed methods with authorization token: GET, PUT, DELETE
 Allowed methods without autorization token: GET




