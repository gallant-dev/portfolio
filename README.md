# My Personal Portfolio Project - Udacity Full Stack Web Developer Nanodegree

This is my personal portfolio website which I then converted into a Flask, and 
mod_wsgi application. It showcases some of the projects I completed for the 
Udacity Full Stack Nanodegree, as well as some previous hobby gamedevelopment
projects.

My portfolio follows responsive design principals, using media queries to
adjust the layout and size to display better on various devices. Flexbox is
used to adjust the layout of the project icons depending on the screen width.

## Requirements

* Python 2.7.12 or higher
* Apache 2
* mod_wsgi
* Flask, render_template
* A webserver.
* An active internet connection

## How to run the app

Place the files in the /var/www/ directory of your server. 

Configure your `.conf` apache files to use WSGIScriptAlias
to set the alias to `/var/www/portfolio/portfolio.wsgi`.

In the address bar type in the domain or IP of your server
to view the website.

Alternatively the website can be viewed at:
https://gallant-dev.com

Authored by: Adam Gallant, 2018-07-08

