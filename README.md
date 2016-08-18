A simple reminder application to send emails based on Django, DRF, Celery, Redis and SQLite

Todo : 
* Supervisor doesn't support Python3 and hence use the fork for monitoring and deployment. 
* Move to MySQL.
* Editing/Deleting a todo to clear off the celery task queue.
* Move to a better mail service provider.

Assumptions : 

* Todo cannot be edited or deleted and cleared off the celery queue
