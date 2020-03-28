#include "cLib.h"

int accum(int n)
{
    int result = 0;
    int i = 1;
    while (i <= n)
    {
        result += i;
        i++;
    }
    return result;
}
