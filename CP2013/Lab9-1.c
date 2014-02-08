#include<stdio.h>

int intcmp(int*, int*);
int sum(int*, int);
int main()
{
    int n, i;
    scanf("%d", &n);
    int arr[n];

    for(i=0;i<n;i++)
        scanf("%d",&arr[i]);

    qsort(arr,n,sizeof(int),intcmp);

    int max = arr[n-1], cnt = 1, party[n];
    party[0] = max;
    //printf("Party: %d\n", party[0]);
    for(i=0;i<n;i++)
    {
        //printf("%d > %d - %d - %d\n", sum(party,cnt) , sum(arr,n) , max , sum(party,cnt));
        if( sum(party,cnt) > (sum(arr,n) - max - sum(party,cnt)) )
        {
            if(cnt == 1 || cnt == 0)
                printf("Require %d Party", cnt);
            else
                printf("Require %d Parties", cnt);
            break;
        }
        else
        {
            party[cnt] = arr[n-1-cnt];
            cnt++;
        }
    }
    return 0;
}

int intcmp(int *a, int *b)
{
    return *a-*b;
}

int sum(int *arr, int n)
{
    int i, summation = 0;
    for(i=0;i<n;i++)
        summation += arr[i];
    return summation;
}

