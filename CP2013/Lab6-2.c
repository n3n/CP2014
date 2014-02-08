#include<stdio.h>

main(){
    int i, j, c=0;
    float m[4][4], n[4][4];
    printf("Matrix A\n");
    for(i=0;i<3;i++){
        for(j=0;j<3;j++){
            scanf("%f", &m[i][j]);
        }
    }
    printf("Matrix B\n");
    for(i=0;i<3;i++){
        for(j=0;j<3;j++){
            scanf("%f", &n[i][j]);
        }
    }
    printf("A x B\n");
    for(i=0;i<3;i++){
        c = 0;
        for(j=0;j<3;j++){
            printf("%.2f ", (m[i][0]*n[0][c])+(m[i][1]*n[1][c])+(m[i][2]*n[2][c]));
            //printf("%.2f >> %.2f+%.2f+%.2f\n", (m[i][0]*n[0][c])+(m[i][1]*n[1][c])+(m[i][2]*n[2][c]),(m[i][0]*n[0][c]),(m[i][1]*n[1][c]),(m[i][2]*n[2][c]));
            //printf("%.2f", (m[i][0]*n[0][c]));
            //printf("%d%dx%d%d %d%dx%d%d %d%dx%d%d\n",i,0,0,c,i,1,1,c,i,2,2,c);
            c += 1;
        }
        printf("\n");
    }
}

/*
0.81 0.91 0.28
0.91 0.63 0.55
0.13 0.10 0.96
0.96 0.96 0.14
0.16 0.49 0.42
0.97 0.80 0.92
*/
