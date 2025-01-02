=====================
Autorun Documentation
=====================

:maintainer: Hugo Osvaldo Barrera <hugo@barrera.io>
:author: Vadim Gubergrits <vadim.gubergrits@gmail.com>

Autorun is an extension for Sphinx that can execute the code from a
runblock directive and attach the output of the execution to the document.

For example:

.. code-block:: rst

    .. runblock:: pycon

        >>> for i in range(5):
        ...    print(i)
        ...

Produces

.. runblock:: pycon

    >>> for i in range(5):
    ...    print(i)
    ...


Another example

.. code-block:: rst

    .. runblock:: console

        $ date

Produces

.. runblock:: console

    $ date

Should a user desire to omit some lines:

.. code-block:: rst

    .. runblock:: pycon

        >>> setup_function(args)  # ignore
        >>> for i in range(5):
        ...    print(i)
        ...

Produces

.. runblock:: pycon

    >>> for i in range(5):
    ...    print(i)
    ...


Currently autorun supports ``pycon`` and ``console`` languages. It's also
possible to configure autorun (from :file:`conf.py`) to run other languages.


Installation
-----------------

Installing via pip

.. code-block:: console

    $ pip install sphinx_autorun

Installing from sources

.. code-block:: console

    $ git clone https://github.com/WhyNotHugo/sphinx-autorun
    $ pip install .


Configuration
-----------------

To enable the autorun extension add 'sphinx_autorun' to the ``extensions`` list
in :file:`conf.py`.

.. code-block:: python

    extensions = [
      'sphinx_autorun',
    ]

By default autorun supports ``pycon`` and ``console``.  It's possible to
configure autorun to run other languages. First you need to be able to pipe your
source to an executable. In many cases it's already done but you can build
your own program to do that.


``autorun_languages``:

    This is a dictionary in :file:`conf.py` that maps a language to an
    executable. For example:

    .. code-block:: python

        autorun_languages = {}
        autorun_languages['pycon']='python -'

    In order to pipe python code to python executable we must use the ``-``
    argument.

    It's also possible to specify the number of characters to remove from each
    line before sending the code. To do that map ``${language}_prefix_chars``
    to the number of characters to remove.

    .. code-block:: python

        autorun_languages = {}
        autorun_languages['pycon'] = 'python -'
        autorun_languages['pycon_prefix_chars'] = 4


Example of configuring autorun to run gnuplot scripts.

.. code-block:: python

    autorun_languages['gnuplot'] = 'gnuplot'

.. code-block:: rst

    .. runblock:: gnuplot

        set term png
        set out 'log.png'
        plot log(x)


This will not produce any output on stdout but it will write the
:download:`log.png` file that can be included with a standard image directive:

.. code-block:: rst

    .. image:: log.png
