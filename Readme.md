# Jobify
***
***Jobify*** - is the API for a job search platform. Here you can create companies, vacancies and 
apply for that vacancies as a user.

### Contents

   * [Installation](#installation)
   * [API Documentation](#api-documentation)

## Installation
Clone this GitHub repository
```
git clone https://github.com/nnbzh/jobify.git
```
You must have pre-prepared virtual environment. Install necessary requirements 
```
cd jobify
pip install -r requirements.txt
```
Apply all necessary migrations and run.
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## API documentation

Import Postman collection from [here](https://www.getpostman.com/collections/f8e2d8fa6ca23c8a85a9)