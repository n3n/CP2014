#include<stdio.h>
int main(){
    float n1, n2, n3;
    scanf("%f %f %f",&n1,&n2,&n3);
    printf("Result: (%.1f+%.1f)*(%.1f-%.1f)/%.1f=%.5f", n1, n2, n1, n2, n3, (n1+n2)*(n1-n2)/n3);
    return 0;
}
