***************
Getting started
***************

All instructions assume that you are working within the :term:`virtualenv`
you already created. For convenience, run the following command so as
to use the tools that are installed in that environment::

    source $VENV/bin/activate


greeting the world
==================

.. sidebar:: WSGI (Web Server Gateway Interface)

   A Python standard that defines an interface between web
   servers and Python web applications.
   It is the most common such interface in the Python world,
   and all Pyramid apps are WSGI apps.

Let's dive right in:

.. literalinclude:: src/01a.py

Run that code, then visit http://localhost:8080,
which should display the famous greeting in your web browser.

Now, read the code and try to make sense of what's going on.
It's about the most simple Pyramid app possible.

serving the app
===============

Let's go through it:

- *line 21*: we call ``main()``, which returns a :term:`WSGI` app.
- *line 22*: we use :func:`~wsgiref.simple_server.make_server` to create
  a WSGI server.
- ``0.0.0.0`` means this server listens on all configured interfaces,
  which means that the app, found on port ``8080``,
  will be reachable by all machines that can reach the host.
  If we used ``127.0.0.1`` instead, only the host would reach the app. [#]_
- *line 23*: ``serve_forever`` method keeps the server running until
  the Python process is killed.

creating and configuring the app
================================

Okay, that was a mouthful, especially for a mere 3 lines of code.
Well, sort of... I ignored what happens in the ``main()`` function:

- *line 14*: we create a :class:`~pyramid.config.Configurator` instance.
  As the name implies, this is what we use to configure our app,
  as you will soon see.
- *line 15*: we add a route to our configuration,
  giving it some arbitrary name. The ``/`` is a matching pattern,
  and in this case represents the root path (http://localhost:8080/).
  If you used ``/greets`` instead, you would need to visit
  http://localhost:8080/greets to see what you saw earlier on... ``Hello World``.
- *line 16*: :meth:`~pyramid.config.Configurator.scan` scans for objects
  marked with configuration decoration,
  which in our case is ``@view_config`` on *line 8*.
- *line 17*: we finally creat (and return) the :term:`WSGI` app.


.. TODO: scan needs a better explanation

the View
========

It does not seem to be getting easier does it?
And we are not even done yet, but let's not give in just yet:

- *line 8*: this decorator indicates that the function decorated is a View,
  a callable object that returns the results on the web pag;
  note the argument, which matches the name we gave the route (see *line 15*).
  This means that the View (aka :term:`View Callable`)
  will get invoked when the given path pattern matches,
  which in our case is just root (``/``).
- *line 9*: here we define the View; do consider the ``request`` object magic
  for now... a sudden appearance of something that seems to come from nowhere.
  I displayed its content out of curiosity (``print request``),
  and got this output::

    GET / HTTP/1.1
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
    Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.3
    Accept-Encoding: gzip,deflate,sdch
    Accept-Language: en-GB,en-US;q=0.8,en;q=0.6
    Cache-Control: max-age=0
    Connection: keep-alive
    Content-Length:
    Content-Type: text/plain
    Host: localhost:8080

  HTTP stuff! You probably need to read some fundamental HTTP stuff to
  fully digest all of that, but you can always postpone that.

.. TODO: request needs a better explanation

- *line 10*: we finally return (and therefore display) the famous greeting.

summary
=======

Basically, we create a WSGI app and serve it.
We do of course have to configure it,
things like what route pattern for which View (yes, we can have a few of each).
The View would then result in the desired displayed info on the browser.


.. [#] The ugly details are at :rfc:`5735`.
