.. _another-pyramid-tutorial:

************
Introduction
************

why another tutorial
====================

There are a few :ref:`pyramid-tutorials` out there,
so you may wonder why one more:

* I wanted to write a tutorial I would have loved to read when I first
  came across the web framework;
  I prefer a gentler approach than what I've seen so far.

* An excuse for me to learn Pyramid (and web technologies) more thoroughly;
  I want to get to a point where I am competent enough to build a simple
  clone of `Stack Overflow`__.


__ http://stackoverflow.com


why Pyramid
===========

I will not repeat the detailed info from the official documentation,
:ref:`what_makes_pyramid_unique`.
Reading something like that was enough to choose Pyramid over competitors.


.. _prerequisites:

prerequisites
=============

.. TODO: finish this

- I assume a Linux-based OS, but you are free to use anything else,
  and will have to adapt the relevant instructions.
- an installed Pyramid, in a :term:`virtualenv`; see :ref:`installing_chapter`
- some Python knowledge (will assume `Python 3`__)
- some SQL knowledge
- some template knowledge (Jinja or Mako?)
- some HTML knowledge

__ http://docs.python.org/3


advice
======

I will sprinkle links all over this tutorial,
but do not be pressured to visit them;
I will try to keep this all self-contained,
with the exception of the above-mentioned :ref:`prerequisites`.
Try not to be led astray (there's so much info out there),
but feel free to keep notes/bookmarks.
If you do get stuck, `tell me how I can improve the tutorial`__.

__ https://bitbucket.org/tshepang/another-pyramid-tutorial/issues


TODO
====

- output that depends on path
- output that depends on shit like /path?name=Tshepang
- explore non-root routes
- intro templates
- ...
- intro DB, using raw SQL (with SQLite)
- ...
- intro SQLAlchemy
- ...
- intro PostgreSQL
- maybe: some SQLAlchemy knowledge: :ref:`ormtutorial_toplevel`
- ...
- Stack Overflow clone:

  - openid
  - postgresql
  - rate-limiting
  - see if pyramid_persona would be of use
