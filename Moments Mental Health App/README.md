# Moments

Too much going on? Starting to lose perspective? Feeling anxious and don’t know what to do next?\
Take a (virtual) walk down memory lane in our app to reminisce on all the important moments in your life.\
A private and secure space to document your thoughts, fears, failures, accomplishments and key life moments.

### Contributors:
Ozan Caglar, Kashan Sheikh, Lionel Smith and Zeynep Yanar

## Operating instructions:

### BACKEND

### To install pipenv
pip install pipenv  **# to install dependencies and activate env**\
pipenv install  **# from back_end**\
pipenv shell  **# to activate**

### To setup database
python manage.py makemigrations **# from back_end/moments**\
python manage.py migrate

### To create user to access admin
python manage.py createsuperuser  **# from back_end/moments**

### To create prompts into your backend
***You will lose anything already in your journal tables***\
python manage.py loaddata journal **# from back_end/moments**


### FRONTEND

npm install **# from main folder and then from front_end**
