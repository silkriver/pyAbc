/* C/C++编写Python扩展模块示例 */
#include <Python.h>
/* 计算斐波纳契数列的项 */
int cFib(int n)
{
    if (n < 2)
        return n;
    return cFib(n - 1) + cFib(n - 2);
}
/* Python函数 */
static PyObject *fib(PyObject *self, PyObject *args)
{
    int n;
    if (!PyArg_ParseTuple(args, "i", &n))
        return NULL;
    return Py_BuildValue("i", cFib(n));
}
/* Python方法列表 */
static PyMethodDef module_methods[] = {
    {"fib", fib, METH_VARARGS, "calculates the fibonachi number"},
    {NULL, NULL, 0, NULL}};
/* Python模块 */
static struct PyModuleDef mymath =
    {
        PyModuleDef_HEAD_INIT,
        "mymath",        /* 模块名 */
        "mymath module", /* 模块文档字符串 */
        -1,              /* 保持全局状态 */
        module_methods};
/* Python模块初始化 */
PyMODINIT_FUNC PyInit_mymath()
{
    return PyModule_Create(&mymath);
}
