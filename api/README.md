# fast-food-fast
Fast-Food-Fast is a food delivery service app for a restaurant.  
- This repo contains the api for the above application
## Build status
[![Build Status](https://travis-ci.com/Kasulejoseph/fast-food-fast.svg?branch=develop)](https://travis-ci.com/Kasulejoseph/fast-food-fast)
[![Maintainability](https://api.codeclimate.com/v1/badges/3a96327f2825ea0ab3bd/maintainability)](https://codeclimate.com/github/Kasulejoseph/fast-food-fast/maintainability)
[![Coverage Status](https://coveralls.io/repos/github/Kasulejoseph/fast-food-fast/badge.svg?branch=develop)](https://coveralls.io/github/Kasulejoseph/fast-food-fast?branch=develop)
## Prerequisites
``` - Python3.6 - A Programming language that is convienient for this app. version3.6 is highly recommended
   - Flask - A most powerful Python web framework. Flask==1.0.2 is the recommended version
   - Virtualenv - A tool to create isolated virtual environment
   - Pytest - python web testing frame work
   ```
   ## Installation
   Clone this repo to your local machine
   ```
      - $ https://github.com/Kasulejoseph/fast-food-fast.git
      - $ cd fast-food-fast
   ```
   Install virtual environment
   ```
     - On linux
      $ virtualenv env -to create virtual environment
      $ source env/bin/activate -- to activate the virtual environment
     - On windows
       https://programwithus.com/learn-to-code/Pip-and-virtualenv-on-Windows/
   ```
   Start the server
   ```
   - $ cd api
   - $ python run.py
   ```
   ## End Points
   |Method | End-Point | Functionality|
   | ---| --- | ---|
   | POST |api/v1/orders| Place an order |
   | GET |api/v1/orders/id | Get a specific order by id. |
   | PUT |api/v1/orders/id | Updates order status. |
   | GET |api/v1/orders/ | Get all orders available. |
   | DELETE |api/v1/orders/id | Admin delete a specific order. |
   
   ## Versioning
   The url versioning for this API startS, with the letter “v”. As you can see in the endpoints above
   ```
   For example
   POST >> https://127.0.0.1:5000/api/v1/orders/
   PUT >> https://127.0.0.1:5000/api/v1/orders/7
   ```
   ## Automated Tests
   ```
   - make sure the server is runing
   - install a test client like Postman or restman to your machine
   - copy paste the url of the local server to the test client you chose
   - for every request method you perform append a necessary end point to its equivalent
     to your request method
   - comfirm data is returned for every request made
   ```
   ## Units Tests
   Install pytest and run
   ```
   $ pytest -v --cov api --cov-report
   ```
   ## Deployment
   The app is hosted on [heroku](https://fast-food-fast-api-kasule.herokuapp.com/api/v1/orders/)
   ## Author 
   [Kasule Joseph](https://github.com/Kasulejoseph)
   ## Acknowlegments
   - [Andela](https://andela.com/)




