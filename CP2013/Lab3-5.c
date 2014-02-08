#include<stdio.h>

#define PI 3.1416
int main(){
    float dia;
    scanf("%f",&dia);
    dia /= 2;
    printf("Volume: %.4f m^3\n", ((4.0/3.0)*PI*(dia*dia*dia))/1000000);
    printf("Surface Area: %.4f m^2", ((dia*dia)*PI*4)/10000 );
    return 0;
}
