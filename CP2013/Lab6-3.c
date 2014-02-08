#include<stdio.h>

main(){
    int i, j, c=0;
    float m[4][4];
    for(i=0;i<3;i++){
        for(j=0;j<3;j++){
            scanf("%f", &m[i][j]);
        }
    }
    if(m[0][0] == m[1][1] && m[1][1] == m[2][2]){
        for(i=0;i<3;i++){
            for(j=0;j<3;j++){
                if(!(i==j) && m[i][j] == 0.0){
                    c++;
                }
            }
        }
    }
    if (c==6){
        printf("This is a scalar matrix");
    }
    else{
        printf("This is not a scalar matrix");
    }


}
