Movable Ink Demo Application
============================

This is a sample web page powered by python/flask that can be used with Movable Ink's [Web Crop](http://movableink.com/apps/web-crop) app.

[See it live](http://movableink-python-demo.heroku.com)

Prerequisites
-------------

 * git
 * Heroku account (unless you're hosting it elsewhere)

Setup
-----

    git clone git://github.com/movableink/python-demo.git movableink-python-demo
    cd movableink-python-demo
    gem install heroku
    heroku login
    heroku create --stack=cedar
    git push heroku

License
-------

Licensed under the MIT License. See LICENSE.md.
