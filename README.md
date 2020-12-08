<!-- ACTIONS BAGDES -->



<!-- PROJECT LOGO -->
<br />
<p align="center">

  <h1 align="center">Django Challenge</h1>

  <p align="center">
    A Django project with a CRUD for the data set of Regular Plans.
    <br />
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

[![Product Name Screen Shot][product-screenshot]](https://example.com)

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

You need things to use and run the software.
* docker-compose
* gmail account

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
1. You just need type in your bash:
   ```sh
   docker-compose up
   ```
2. Install NPM packages
   ```sh
   npm install
   ```



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<!-- CONTACT -->
## Contact

Luis Carlos - [@sir.turing](https://instagram.com/sir.turing) - luiscarlos.sf2017@gmail.com

Project Link: [https://github.com/luiscarlossf/django-challenge](https://github.com/luiscarlossf/django-challenge)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* []()
* []()
* []()


