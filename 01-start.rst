***************
Getting started
***************

All instructions assume that you are working within the :term:`virtualenv`
you already created. For convenience, run the following command so as
to use the tools that are installed in that environment::

    source $VENV/bin/activate


greeting the world
==================

Let's dive right in:

.. literalinclude:: src/01a.py

Run that code, then visit http://localhost:8080,
which should display the famous greeting in your web browser.

Now, read the code and try to make sense of what's going on.
It's about as simple a Pyramid app can get.

.. sidebar:: WSGI (Web Server Gateway Interface)

   A Python standard that defines an interface between web
   servers and Python web applications.
   It is the most common such interface in the Python world,
   and all Pyramid apps are WSGI apps.

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

Okay, that was a mouthful, especially for a mere 3 lines of code.
Well, sort of... I ignored what happens in the ``main()`` function:

- *line 14*: we create a :class:`~pyramid.config.Configurator` instance.
  As the name implies, this is what we use to configure out app,
  as you will soon see.

.. [#] The ugly details are at :rfc:`5735`.
