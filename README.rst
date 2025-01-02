==============
sphinx-autorun
==============

sphinx-autorun is an extension for Sphinx_ that can execute the code from a
runblock directive and attach the output of the execution to the document.

.. _Sphinx: https://sphinx.readthedocs.io/

For example::

    .. runblock:: pycon

        >>> for i in range(5):
        ...    print i

Produces::

    >>> for i in range(5):
    ...    print i
    1
    2
    3
    4
    5


Another example::

    .. runblock:: console

        $ date

Produces::

    $ date
    Thu  4 Mar 2010 22:56:49 EST

Currently autorun supports ``pycon`` and ``console`` languages. It's also
possible to configure autorun (from `conf.py`) to run other languages.


Installation
------------

Installing via pip (recommended)::

    $ pip install sphinx-autorun

Install from source::

    $ git clone https://github.com/WhyNotHugo/sphinx-autorun/
    $ pip install .

To enable autorun add 'sphinx_autorun' to the ``extension`` list in
`conf.py`::

    extensions.append('sphinx_autorun')

The documentation is in the doc/ folder.

About this fork
---------------

sphinx-contrib/autorun was abandoned and broken for several months. Since it
did not even work, this fork was created as a continuation of it with mostly
critical fixes.
