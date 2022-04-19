Queclinkdoc
===========

Queclinkdoc is a simple, clean, and less-configured theme for the `Sphinx <https://www.sphinx-doc.org>`_ documentation system developed by `Queclink Wireless Solutions Co., Ltd <https://www.queclink.com>`_.

We show the global **TOC** tree of the documentation in a drop-down list at the head of the page, and even if you browse to the end of the page, this TOC tree will still be fixed at the head, so you can jump to other pages at any time.

We recommend using *Google Chrome* or *Firefox* to read the generated documentation. 

You can make and install **queclinkdoc** theme like this:

.. code-block:: Python

   py setup.py sdist
   py -m pip install dist\queclinkdoc-x.x.tar.gz

When using the `ref <https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#ref-role>`_ directive to jump to the top of the page, for a good experience, please name the label at the top of the page with **headlabel-** as a prefix, for example:

.. code-block::
   :linenos:

   .. _headlabel-page-title:

   Page Title
   ===========

In addition, this theme supports the following custom HTML options:

- zoomout_asize

  Can be *true* or *false*, default is *true*. The font size of the <a> tag whose first character is a capital letter will be reduced to 0.95em when it is true, and will not be reduced when it is false. You can change it to false like this:

  .. code-block::

     html_theme_options = {
       'zoomout_asize': 'false',
     }

`Here <snapshot.png>`_ is a snapshot of the **queclinkdoc** theme.

If you have any questions or suggestions, please contact us, thanks in advance.
