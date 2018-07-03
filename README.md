Healthcare API &mdash; and so much more
===========

### Ready made to be an instant project kit with almost no setup and is easily deployed

#### The stack is made up of the following:

- PostgreSQL
- Django
    - Models
    - Views
    - Auth (including already built `login`, `logout`, and `register` views)

## Local Setup

### 1. PostgreSQL

The first thing to do is make sure you have [PostgreSQL](https://www.postgresql.org/) downloaded, installed, and **running**.  Then either get [Postico](https://eggerapps.at/postico/ "A fantastic PostgreSQL application for Mac") or open a `psql` shell.

**Run the following commands:**

```
CREATE USER <your_username> WITH CREATEDB;
ALTER USER <your_username> WITH PASSWORD '<your_password>';
CREATE DATABASE <your_database> WITH OWNER <your_username>;
```

Now you should have a development database setup on your local machine for the app to use.

### 2. Django

**Run the following from your project directory in your shell:**

```
pip install -r requirements.txt
```

Next we need to set the following variables in our bash shell so that Django knows which database to use.

**Run the following in your shell:**

```
export HEALTHSLTLX_LOCAL_NAME=<your_database>
export HEALTHSLTLX_LOCAL_USERNAME=<your_username>
export HEALTHSLTLX_LOCAL_PASSWORD=<your_password>
```

> Note: If you don't want to have to set these variables every time you open a shell, you can set them in your .bashrc (or .zshrc like me), you can write a script to export them for you, or if you use a virtual environment (recommended) follow these [instructions](#additional-notes) to have the variables always exist when in your environment.

Then we need to bring your database up to date with the state of your models.

**Run the following from your project directory in your shell:**

```
python manage.py makemigrations
python manage.py migrate
```

**All that is left is to start your server and you will have a fully working full stack web application:**

```
python manage.py runserver
```

That is all you need to get started!


## Additional Notes

The immediate value of [Virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/install.html) is easily separating the `pip` installed requirements for different projects. Different problems call for different tools, many of which often conflict, and if you are working on a Hackathon you want as few tools affecting your code as possible in order to prevent unexpected errors.

More power comes from the virtualenvwrapper in its `postactivate` & `predeactivate` files. You can run code and make changes to your environment and variables every time you enter a virtual environment, and then revert the changes when you leave. These are things that you should get familiar with before you enter a competition in order to make your time more development and less set-up!

Below are handy scripts to load and unload the environment variables for your hackathon kit.

edit: `~/.virtualenvs/<virtual_env_name>/bin/postactivate`
```
#!/bin/zsh
# This hook is sourced after this virtualenv is activated.
export HEALTHSTLX_LOCAL_NAME=<your_database>
export HEALTHSTLX_LOCAL_USERNAME=<your_username>
export HEALTHSTLX_LOCAL_PASSWORD=<your_password>
echo "Healthcare api local variables have been set."
```

edit: `~/.virtualenvs/<virtual_env_name>/bin/predeactivate`
```
#!/bin/zsh
# This hook is sourced after this virtualenv is activated.
unset HEALTHSTLX_LOCAL_NAME
unset HEALTHSTLX_LOCAL_USERNAME
unset HEALTHSTLX_LOCAL_PASSWORD
echo "Healthcare api local variables removed."
```


## Author Note

Released by [Dan Borstelmann](https://github.com/dborstelmann) on July 3, 2018.
