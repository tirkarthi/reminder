POST /api/reminders/

Create a new reminder

email - A valid email ID
message - A valid message
time - Time for the mail to be sent of the format "YYYY-MM-DDTHH:MM:SS" and greater than the current time. Timezone : UTC

Format : http POST <host>/api/reminders/ email=<email> message=<message> time=<time>
Example : http POST :9000/api/reminders/ email="tir.karthi@gmail.com" message="Notify me" time="2016-08-18T04:53:50"
Output :

{
    "email": "tir.karthi@gmail.com", 
    "id": 4,
    "message": "Notify me",
    "status": 0,
    "time": "2016-08-18T04:53:50"
} 


GET /api/reminders/<id>

Get details of a reminder

message - The message to be sent
status - The status of the reminder
email - The email ID for the reminder
time - Time for the reminder mail to be sent

Example : http :9000/api/reminders/4

Output :

{
    "email": "tir.karthi@gmail.com", 
    "id": 4,
    "message": "Notify me",
    "status": 1,
    "time": "2016-08-18T04:53:50"
} 
