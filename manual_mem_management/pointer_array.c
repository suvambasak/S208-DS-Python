#include <stdio.h>

int main()
{

    int arr[5] = {1, 2, 3, 4, 5};

    printf("arr = %p \n", arr);

    printf("arr+0 = %p \t *arr+0= arr[0] = %d  \n", arr + 0, *arr + 0);
    printf("arr+1 = %p \t *arr+1= arr[1] = %d  \n", arr + 1, *arr + 1);
    printf("arr+2 = %p \t *arr+2= arr[2] = %d  \n", arr + 2, *arr + 2);

    printf("\n\n");
    return 0;
}

// (base) suvam@KD-304G:/mnt/Storage/Repositories/S208-DS-Python/manual_mem_management$ cc pointer_array.c && ./a.out
// arr = 0x7fffd3b6a210
// arr+0 = 0x7fffd3b6a210   *arr+0= arr[0] = 1
// arr+1 = 0x7fffd3b6a214   *arr+1= arr[1] = 2
// arr+2 = 0x7fffd3b6a218   *arr+2= arr[2] = 3