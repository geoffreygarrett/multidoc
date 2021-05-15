.. multidoc documentation master file, created by
   sphinx-quickstart on Sun May  9 18:07:26 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to ``multidoc``'s documentation!
========================================

Creating and maintaining an API Reference for multiple programming languages
consumes unnecessary time. ``multidoc`` attempts to solve this through the use
of ``jinja2`` templating and ``pydantic`` data modelling. At the core, is the
API Declaration:

.. code-block:: yaml
   :caption: ``api/hello.yaml``

   summary: This is the hello module...
   notes: It's probably not that impressive 🤔

   functions:
      - name: hello
        returns:
           name: world
           type: str
           description: Returns the world!

With the API Declaration in hand, we can add replacement tags to the C++
source code:

.. code-block:: C++
   :caption: ``cpp_src/foo.h``

   //! @get_docstring(__doc__)
   #include <string>

   namespace hello {

   //! @get_docstring(world)
   std::string world();

   }

In the ``pybind11`` exposed module, docstrings can also be added:

.. code-block:: C++
   :caption: ``pybind_src/foo.cpp``

   #include <pybind11/pybind11.h>
   #include <pybind_src/docstrings.h>
   #include <cpp/foo.h>

   namespace py = pybind11;

   PYBIND11_MODULE(hello, m) {
       m.doc() = hello::get_docstring("__doc__");
       m.def("world", &hello::world, hello::get_docstring("world"));
   }

>>> generate_documented(src="pybind_src", dest=".", local={"py": True}, api="api/module.yaml")
>>> generate_documented(src="cpp_src", dest=".", local={"cpp": True}, api="api/module.yaml"))

.. toctree::
   :maxdepth: 2
   :caption: Modules:

   parsing
   template
   generate
   regex
   error


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
