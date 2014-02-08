#include<stdio.h>

int max(int* arr, int n);
int sum(int *arr, int n);

int main(){
    int n, i, temp=0, c=0;
    scanf("%d",&n);
    int mem[n],party[n];
    for(i=0;i<n;i++)
        scanf("%d",&mem[i]);



    int process = 1;
    for(i=0;i<50;i++)
        printf("%c", 3);
    printf("\n");
    while(process)
    {
        temp += max(mem,n);
        printf("Checking: [Temp: %d > Sum: %d]\n", temp, sum(mem,n));
        for(i=0;i<n;i++)
        {
            if(mem[i] == max(mem, n))
            {
                mem[i]=0;break;
            }
        }
        if(temp>sum(mem,n))
        {
            printf("True!!!\n");
            printf("Require %d Party\n",c);
            printf("Love Love Love\n");
            process = 0;
            break;
        }
        printf("False!!!\n");
        c++;
    }
    for(i=0;i<50;i++)
        printf("%c", 3);
    return 0;
}
int sum(int *mem, int n) {
    int i, summation = 0;
    for(i=0;i<n;i++)
        summation += mem[i];
    return summation;
}

int max(int* mem, int n) {
    int maxValue = 0, i;
    for(i=0; i<n; i++) {
        if(mem[i] > maxValue) {
            maxValue = mem[i];
        }
    }
    return maxValue;
}


