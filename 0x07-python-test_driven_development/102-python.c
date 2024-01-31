#include "Python.h"

/**
 * print_python_string - Prints information about Python strings.
 * @p: A PyObject string object.
 */
void print_python_string(PyObject *p) {
    if (PyUnicode_Check(p)) {
        const char *str = PyUnicode_AsUTF8(p);
        if (str != NULL) {
            printf("String: %s\n", str);
        } else {
            PyErr_Print();
        }
    } else {
        PyErr_SetString(PyExc_TypeError, "Invalid string");
        PyErr_Print();
    }
}
