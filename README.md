## Getting Started

Setup project environment with [virtualenv](https://virtualenv.pypa.io) and [pip](https://pip.pypa.io).

```bash
$ virtualenv project-env
$ source project-env/bin/activate

# Below command installs django version 2.2.5
$ pip install -r https://raw.githubusercontent.com/piyushHere/Grofers-SDE-Assignment/master/requirements.txt

$ django-admin startproject --template https://github.com/piyushHere/Grofers-SDE-Assignment/archive/master.zip Lucky_Draw_Gaming_Service

$ cd Lucky_Draw_Gaming_Service/
$ python manage.py migrate
$ python manage.py runserver
```

# Database

We have used the default database in Django which is 'sqlite3'. We have created 3 tables in our database:
1) First we have a user table which contains the user details i.e a unique username which we have set as primary key so nullable values are not allowed.
2) Ticket table which contains all the details of generated tickets, the user which generated this ticket, ticket number and event name in which this ticket is used (contains blank if this ticket is yet to be used).
3) An event table which stores the details of all events i.e event names, their prizes, their winner and the time at which they start and end.

# Cron job 
We have scheduled a periodic task which will update the event winner daily at 12 am which is the time at which daily contests end.
It will call the function called update winner at scheduled time. 

## RESTful APIs

We are going to use RESTful API to implement our endpoints in our application. In our case, we have one single resource, lucky_draw, so we will use the following URLS - /lucky_draw/ and /lucky_draw/<str> for collections and elements, respectively and we will implement the required four functionality as below:
Endpoint |HTTP Method | CRUD Method | Result
-- | -- |-- |--
`contest/generateticket` | POST | Create | Create a single ticket 
`contest/participate`| POST | Create | Takes the ticket from user, verifies it and updates the event column for that ticket to signify that this ticket has been used.
`contest/upcoming_event` | GET| Show | Show the upcoming contest.
`contest/last_week_winners` | GET | Show | Show the winners of all contests that happened in the past 1 week.

## How to hit APIs described above

To verify the APIs above, we can send requests to the port number depicted by the URL http://127.0.0.1:8000 locally. For this purpose I have used a tool called POSTMAN.

Generate ticket-
http POST request -  http://127.0.0.1:8000/lucky_draw/generateticket"
For the above request, we have sent username in the body tag of request as below:
{
    "username" : "piyush_here"
}
If the request is successful, we will get a response as below:
{
    "success": true,
    "ticket": "98a176e9-b4ee-11eb-b22a-9828a617c8b8"
}

Participate in an event using a ticket-
http POST request on the URL http://127.0.0.1:8000/participate
The body for above request is as follows:
{
	"username":"piyush_here",
	"ticket_number":"123",
	"event_name":"may_15"
}
If the request is successful, we will get a response as below:
{
    "success": true
}

Get the upcoming event-
http GET request on the URL http://127.0.0.1:8000/upcoming_event
The response will be as below:
{
    "success": true,
    "event_name": "may_15",
    "event_prize": "Samsung TV"
}

To get the winners for contests that happened in the past week:

http GET on URL http://127.0.0.1:8000/api/v1/contest/last_week_winners
The reponse will be as below:
{
    "may_10": "Aman Kohli"
}
Note: It shows only one winner in the past week because only 1 event happened this week. 

