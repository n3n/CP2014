#include<stdio.h>
void swap(int *p, int*q)
{
    int tmp;
    tmp = *p;
    *p = *q;
    *q = tmp;
}
void bubble(int a[], int n)
{
        int i, j, tmp;
        for(i = 0;i < n - 1; ++i)
            for(j=n-1 ; j > i; --j)
                if(a[j-1] > a[j])
                    tmp = a[j-1];
                    a[j-1] = a[j];
                    a[j] = tmp;
                    //swap(&a[j-1], &a[j]);
}

main()
{
    int i, a[10];
    for(i=0;i<10;i++)
        scanf("%d",&a[i]);
    bubble(a,10);
    for(i=0; i<10; i++)
        printf("%d ", a[i]);

}


