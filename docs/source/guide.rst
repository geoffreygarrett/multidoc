.. code-block:: C++
   :caption: ``FooClass.h``

   #include <string>

   namespace foo {

   //! @get_docstring(FooClass.__doc__)
   class FooClass {
   public:

      //! @get_docstring(FooClass.ctor, 0)
      FooClass();

      //! @get_docstring(FooClass.ctor, 1)
      FooClass(int i);

      //! @get_docstring(FooClass.bar)
      std::string bar();

   }

   }

.. code-block:: C++
   :caption: ``FooClass.h``

   #include <pybind11/pybind11.h>
   #include <foo/docstrings.h>
   #include <foo/FooClass.h>

   namespace py = pybind11;
   using namespace foo;

   PYBIND11_MODULE(foo, m) {
       m.doc() = get_docstring("__doc__");  // module docstring

       m.def("hello", &hello, get_docstring("hello"));

       py::class_<foo::FooClass>(m, "FooClass", get_docstring("FooClass.bar"))
         .def(py::init<>(),                     get_docstring("FooClass.ctor", 0))
         .def(py::init<int>(), py::arg("i"),    get_docstring("FooClass.ctor", 1)))
         .def("bar", &FooClass::bar,            get_docstring("FooClass.bar"));

       m.def("add", &add, "A function which adds two numbers");
   }

