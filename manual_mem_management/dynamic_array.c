#include <stdio.h>
#include <stdlib.h>

int main()
{

    int *arr;

    arr = (int *)malloc(sizeof(int) * 5);

    printf("arr = %p \n", arr);

    printf("arr+0 = %p \t *arr+0= arr[0] = %d  \n", arr + 0, *arr + 0);
    printf("arr+1 = %p \t *arr+1= arr[1] = %d  \n", arr + 1, *arr + 1);
    printf("arr+2 = %p \t *arr+2= arr[2] = %d  \n", arr + 2, *arr + 2);

    free(arr);
    arr = NULL;

    printf("\n\n");
    return 0;
}

// (base) suvam@KD-304G:/mnt/Storage/Repositories/S208-DS-Python/manual_mem_management$ cc dynamic_array.c && ./a.out
// arr = 0x55ddce4482a0
// arr+0 = 0x55ddce4482a0   *arr+0= arr[0] = 0
// arr+1 = 0x55ddce4482a4   *arr+1= arr[1] = 1
// arr+2 = 0x55ddce4482a8   *arr+2= arr[2] = 2