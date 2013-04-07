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
which should display the famous greeting.

Now, read the code and try to make sense of what's going on.
The code is about as simple an app as we can get with this web framework.

Let's go through it:

.. TODO: what is WSGI

- line 21: we call ``main()``, which returns a WSGI app.
- line 22: we use :func:`~wsgiref.simple_server.make_server` to create
  a WSGI server.
- ``0.0.0.0`` means this server listens on all configured interfaces,
  which means that the app, found on port ``8080``,
  will be reachable by all machines that can reach the host.
  If we used ``127.0.0.1`` instead, only the host would reach the app. [#]_
- line 23: ``serve_forever`` method keeps the server running until
  the Python process is killed.

Okay, that was a mouthful, especially for a mere 3 lines of code.
Well, sort of... I ignored what happens in the ``main()`` function.


.. [#] The ugly details are at :rfc:`5735`.
