Sphinx AutoSaltSLS
*******************

Sphinx AutoSaltSLS provides a way to automatically document Salt .sls files (e.g. states, pillar, reactors, etc) using
simple directives in the comments blocks of those files.

A comment block is identified using a block start string (default is '###') and contains all subsequent lines that start
with a given comment character (default is '#''). The block ends when a new start string or a non-comment line is read.
Directives can be given in the comment block to control how the lines are parsed.

Getting Started
================

The following steps will walk through how to add AutoSaltSLS to an existing Sphinx project. For instructions on how to
set up a Sphinx project, see Sphinx's documentation on `Getting Started <https://www.sphinx-doc.org/en/master/usage/quickstart.html>`_.

Installation
-------------

AutoSaltSLS can be installed through pip:

.. code-block:: bash

    pip install sphinxcontrib-autosaltsls

Next, add and configure AutoSaltSLS in your Sphinx project's ``conf.py``.

.. code-block:: python

    extensions.append('sphinxcontrib-autosaltsls')

    autosaltsls_sources = {
        'states': {
            'title': 'States',
            'exclude': [
                'roles',
            ],
            'template_path': '_templates/autosaltsls/states',
        },
        'pillar' : {
            'title': 'Pillar'
        },
    }

The documentation will be built into the location specified by ``autosaltsls_build_root`` (defaults to '.')

To configure AutoAPI behaviour further, see the Configuration documentation.