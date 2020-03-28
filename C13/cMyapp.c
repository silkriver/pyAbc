#include <stdio.h>
#include "cLib.h"

int main()
{
    int n;
    printf("计算1累加至n，请输入n：");
    scanf("%d", &n);
    int result = accum(n);
    printf("1累加至%d的结果是%d\n", n, result);
    return 0;
}
