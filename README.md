# CarsParts "website"

## What is this?
This is a project created for one of university subjects. 
The project in question is a backbone of a webstore with 
functional payment system connected.

## How is this?
This is a python-based project, that uses
* [django-unicorn]
* [Stripe]
* [html] (lol)
* [PostGreSQL DB](https://www.postgresql.org/)

## No CSS? No JS?
I kinda did use some css to position the things on the pages at 
least somewhat close to what I had in mind.

So far as JS goes, `django-unicorn` is a framework that kinda 
interconnects html with python code directly, so I had no need for JS.

## Structure
This is the typical structure of a django project.
The "server" ([manage.py]) is located in the [CarsParts] folder.

[CarsParts/CarsParts] folder contains some admin shit, like settings 
of the server, connection to PostGreSQL DB, etc

[cars_parts]. I mostly contributed to this folder. 
This is a folder of an "app" that's created by `python manage.py startapp cars_parts`

[components] contains Unicorn components, the python side of the 
[django-unicorn].

[templates] and [templates/unicorn] folders contain all the [html] sources.
Now because I'm a noob when it comes to web, I made a "_load" html for
every page I'm going to, because I had no idea how to change pages while 
attaching unicorn views.

## Database
All in all, there are 7 tables, and they fulfil the very absolute minimum
of what you need to keep at least some track of parts and orders and the sort.

* models
  * brand varchar,
  * model varchar
* prices
  * uah float,
  * usd float, (unused)
  * eur float (unused)
* parts
  * model_id integer REFERENCES models (id),
  * name varchar,
  * description text,
  * available integer,
  * pricing integer
* images
  * image_name varchar,
  * part_id integer REFERENCES parts (id)
* customers
  * recipient_name varchar,
  * recipient_address varchar,
  * phone varchar,
  * email varchar
* orders
  * order_number integer,
  * customer_id integer REFERENCES customers (id)
* ordered_parts
  * order_id integer REFERENCES orders (id),
  * part_id integer REFERENCES parts (id),
  * quantity integer

The tables are populated with minimal amount of data, just enough to
run the simulation

## Setup and testing
Before you run everything, setup your database connection data in 
[settings.py], and do `export stripe_api_key="<your Stripe SECRET key here>"`
in your shell, Stripe will use this env var as validation token

When that's out of the way, open the [root folder] in terminal and run the
following
```shell
# I used python 3.11.9 for this project, that's what the code should work with

py -3.11 -m venv .venv # Windows. Use python3.11 for Unix
. .venv/Scripts/activate # . .venv/bin/activate for Unix
pip install -r requirements.txt
cd CarsParts
python manage.py runserver
```
Voila, [localhost]

## Contributing
Don't.

### Special thanks to:
* Me for enduring this
* Django and Unicorn docs
* Me for reading these docs
* html docs
* css docs
* Stripe being a simple intuitive thing
* Me for not giving up

[root folder]: ./
[localhost]: http://127.0.0.1:8000/
[Stripe]: https://docs.stripe.com/
[html]: https://en.wikipedia.org/wiki/HTML
[django-unicorn]: https://www.django-unicorn.com/
[CarsParts/CarsParts]: ./CarsParts/CarsParts
[CarsParts]: ./CarsParts
[cars_parts]: ./CarsParts/cars_parts
[components]: ./CarsParts/cars_parts/components
[templates]: ./CarsParts/cars_parts/templates
[templates/unicorn]: ./CarsParts/cars_parts/templates/unicorn
[manage.py]: ./CarsParts/manage.py
[settings.py]: ./CarsParts/CarsParts/settings.py