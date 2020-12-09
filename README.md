<!-- ACTIONS BAGDES -->



<!-- PROJECT LOGO -->
<br />
<p align="center">

  <h1 align="center">Django Challenge</h1>

  <p align="center">
    A Django project with a CRUD for the data set of Regular Plans.
    <br/>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#setup">Setup</a></li>
        <li><a href="#how-to-run">How to run</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Django Challenge Screen Shot][api-screenshot]](https://github.com/luiscarlossf/django-challenge/screenshots/api_root.png)

API for list, update and create Regular plans. When a use does a plan public, a notice e-mail will be send to user. Every 5 minutes a cronjob does a backup of data, copying data from PostegresDB to a MongoDB.


### Built With

* [Django Rest Framework](https://www.django-rest-framework.org/)
* [Docker](https://www.docker.com/)
* [MongoDB](https://www.mongodb.com/)
* [Celery](https://docs.celeryproject.org/)



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

You need somethings to run and use the software.
* Docker Compose

See [Docker documentation](https://docs.docker.com/compose/install/) to install Docker Compose.
* Gmail Account

To send e-mail for users when a Regular Plan is public, we need a e-mail to access SMTP Gmail Server.
1. Create a [Google account](https://accounts.google.com/signup/v2/webcreateaccount?service=accountsettings&continue=https%3A%2F%2Fmyaccount.google.com%2F&gmb=exp&biz=false&flowName=GlifWebSignIn&flowEntry=SignUp)
2. Go to `Settings` and then `Forwardin POP/IMAP`
3. Enable IMAP and Save editions.
4. Access [here](https://myaccount.google.com/u/0/lesssecureapps?pli=1&rapt=AEjHL4OTUgsgQ56kedi8EINX35w-3ObeKavFNh_NutvB8iilFa3PTjjt4Gt-1O2FN3m7xBR9u2xYa9iEw4fOlp9Pxma4z1nPRg) 
5. Enable `Allow less secure apps` option.

### Setup
#### Cloning the repo
    $ git clone https://github.com/luiscarlossf/django-challenge.git
    $ cd django-challenge
#### Defining enviroment variables
1. Create a file `.env` in current directory
2. Copy the variables from `.env-example` to `.env`
```sh
#[Postgres Database envs]
POSTGRES_DB=
POSTGRES_HOST=
POSTGRES_TEST_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=

#[MongoDB Database envs]
MONGO_INITDB_DATABASE=
MONGO_INITDB_ROOT_USERNAME=
MONGO_INITDB_ROOT_PASSWORD=

#[Info for Django superuser]
DJANGO_USER=
DJANGO_EMAIL=
DJANGO_PASSWORD=

#[Credentials gmail to config STMP host]
EMAIL_HOST_USER= 
EMAIL_HOST_PASSWORD=

#[Info for Rabbitmq broker]
RABBITMQ_DEFAULT_VHOST=
RABBITMQ_DEFAULT_USER= 
RABBITMQ_DEFAULT_PASS= 
```

### How to run

You just need to type:
   ```sh
   docker-compose up
   ```
   
<!-- USAGE EXAMPLES -->
## Usage

_Please refer to the [Documentation]()_

<!-- CONTACT -->
## Contact

Luis Carlos - [@sir.turing](https://instagram.com/sir.turing) - luiscarlos.sf2017@gmail.com

Project Link: [https://github.com/luiscarlossf/django-challenge](https://github.com/luiscarlossf/django-challenge)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [Docker Documentation](https://docs.docker.com/)
* [Django Rest Framewok Documentation](https://www.django-rest-framework.org/)
* [Celery Documentation](https://docs.celeryproject.org/)
* [Postgres Documentation](https://www.postgresql.org/docs/current/)
* [Django Documentation](https://docs.djangoproject.com/)
* [RabbitmMQ](https://www.rabbitmq.com/)


