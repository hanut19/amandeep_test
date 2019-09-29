1) 'requirement.txt' file contains all the dependency of this application
2) In order to setup this project need to create virtual environment "python -m venv <envname>"
3) Run the requirements.txt to install all dependencies.
4) Mysql database is use "configuration in setting.py".
5) To run migrations "python manage.py makemigrations" and then "python manage.py migrate" command run
6) To run application "python manage.py runserver"
7) Application available at "http://127.0.0.1:8000"
8) To run celery "celery -A mysite worker --loglevel=info" this command use
9) Login page http://127.0.0.1:8000/login/
10) Admin is available at http://127.0.0.1:8000/admin/
11) upload image url "http://127.0.0.1:8000/post/" when you upload a image after uploading using "celery task" it will different size of images
12) Image list is available at http://127.0.0.1:8000/list/ on click of each image you will redirect to page where all different size images list.
13) redis-server start using "redis-server" command

