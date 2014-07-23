Travel Log Demo
==========================

Source files for a travel log demo project in Django.

This project uses following frameworks/libraries:

1. [Django](https://www.djangoproject.com/)
2. [jQuery](http://http://jquery.com/)
3. [Bootstrap](http://getbootstrap.com/)


Usage
==========================

*Requires Django v1.6.5 (or newer)*

Just like any standard Django project:
		
		git clone https://github.com/AA33/demo-project.git
		cd demo-project/travel_log_demo/demo

Modify `settings.py`  to specify a database and it's connection details. Then:

		python manage.py syncdb
		
This will create the necessary tables in the database specified in the previous step.


To run the demo app:

		python manage.py runserver

Go to http://127.0.0.1:8000 and voila, there it is. Enjoy.


