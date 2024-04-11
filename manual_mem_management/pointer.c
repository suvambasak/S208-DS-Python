#include <stdio.h>

int main()
{

    int i = 25;

    printf("i = %d \n", i);
    printf("&i = %p \n", &i);

    int *pi;
    pi = &i;
    printf("pi = %p \n", pi);
    printf("&pi = %p \n", &pi);
    printf("*pi = %d \n", *pi);

    int **ppi;
    ppi = &pi;
    printf("**ppi = %d \n", **ppi);
    printf("*ppi = %p \n", *ppi);
    printf("ppi = %p \n", ppi);

    printf("\n\n");
    return 0;
}

// (base) suvam@KD-304G:/mnt/Storage/Repositories/S208-DS-Python/manual_mem_management$ cc pointer.c && ./a.out
// i = 25
// &i = 0x7ffe73394ad4
// pi = 0x7ffe73394ad4
// &pi = 0x7ffe73394ad8
// *pi = 25
// **ppi = 25
// *ppi = 0x7ffe73394ad4
// ppi = 0x7ffe73394ad8
