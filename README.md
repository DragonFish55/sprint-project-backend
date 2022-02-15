# sprint-project-backend

# To setup the app after cloning the repo you first
# need to install the required python packages.
# Run pip install requirements.txt to install the 
# dependencies.

# Next in the app folder there is a __init__.py file.
# Flask uses postgresql as the server. In the init file
# there is a database URI connection with the following setup:
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://{user}:{password}@localhost:5432/{database}"
# Default values for the user, password, and database are already used so you need to install postgresql
# onto your computer and either create the same database, user, and password, used or create new ones
# and replace the values in the URI.

# In addition the flask environment variables need to be set by 
# running the included bash script:
# set_ev.sh
# The env are set according to windows format:
# set FLASK_APP=app
# set FLASK_ENV=development or set FLASK_ENV=production

# To create the tables you need to run "flask db init"
# in the top folder which will create a migrations folder
# for the tables

# To run the app enter: "python run.py" or "flask run"

# Finally the tests are in their respective files:
# Signin API tests: signin_test.py
# Signout API tests: signout_test.py
# Logout API tests: logout_test.py