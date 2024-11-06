# "website" (dude the name sucks wtf)

## What the fuck dude? It sucks!
Why thank you for the kind words, but as far as I'm concerned, 
the thing's as good as it gets, I have a "webstore" that 
actually does shit 
(also looks like one, but that's whole another story!)

## Oh... good job, whatever this POS is... Oh yeah what is this anyway?
Thanks for asking! This is a project I made for one of my
university subjects. The project in question is a backbone of a
website with functional payment system connected.

## Dude you suck, how did you even manage to write something like this?
I'll be taking it as a compliment! Matter of fact, it sucks a lot less
than it could!

For this magnificent garbage to come to life, I forced myself to work
with:
* [django-unicorn]
* [Stripe]
* [html] (lol)

## The hell?? No CSS? No JS?
YEAH, now fuck off will you

Nay, well, as far as I can tell (the "far" in question being
a really small amount), I kinda used some css to position the things 
on the pages at least somewhat close to what I had in mind.

So far as JS goes, the `django-unicorn` is a framework that kinda 
interconnects html with python code directly, so I had no need for JS.
I totally could use it, but I totally said "fuck it!"

## What is this code...
This is sorta-kinda typical structure of a django project.
The "server" ([manage.py]) is located in the [CarsParts] folder.

[CarsParts/CarsParts] folder contains some admin shit, like settings 
of the server, connection to PostGreSQL DB, etc

Now [cars_parts] is a tad more amusing, I mostly contributed to this
folder's sources. This is a folder of an "app" that's created by some
dark magic shit (a.k.a. `python manage.py startapp cars_parts`)

[components] is a folder that contains Unicorn components, the python
side of the [django-unicorn]. Here I tried my best to make your eyes
bleed by writing code as unoptimal as it gets.

[templates] and [templates/unicorn] folders contain all the [html] sources.
Now because I'm a dimwit when it comes to web, I made a "_load" html for
every page I'm going to, because I had no idea how to change pages while 
attaching unicorn views. Feel free to ignore (**:super-sweaty-emoji:**)!

## So you're saying you even managed the database?

Hell yeah! But fuck I'd be lying if I told you I'll give you any access
to it. Backtrack, bitch!

All in all, there are 7 tables, and they fulfil the very absolute minimum
of what you need to keep at least some track of parts and orders and the sort.

## Say I have your database, how to I test this for myself?
Rather simple really! But before you run it, setup your database connection data
in [settings.py], and do `export stripe_api_key="<your Stripe SECRET key here>"`,
Stripe will use this env var (I should be getting additional points here purely for
not committing secret keys here lol (that will backfire because I've committed
database credentials lol))

Now that you're done setting up and I'm done yapping, do this
```shell
# I used python 3.11.9 for this project, that's what the code should work with

py -3.11 -m venv .venv # Windows. Use python3.11 for Unix
. .venv/Scripts/activate # . .venv/bin/activate for Unix
pip install -r requirements.txt
cd CarsParts
python manage.py runserver
```
Voila, fuckers! [localhost], babyy

## Dude how do I navigate this shit...
However you want, the UI is totally user friendly and intuitive. Now be on your way.

## Bruh... Okay okay you've done a decent job, given how much you suck at this
Oi, why so aggressive? I'm doing my best out here...

### Special thanks to:
* Me for enduring this
* Django and Unicorn docs
* Me for reading these docs
* html docs
* css docs
* Stripe being a simple intuitive thing
* Me for not giving up

### See ya never!


[localhost]: https://127.0.0.1:8000
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