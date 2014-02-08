#include <stdio.h>

// --------------- Prototype Func ----------------
int check_3x3(char mat[9][9]);
int Vertical_check(char mat[9][9]);
int Horizontal_check(char mat[9][9]);
int itissudoku(char mat[9][9]);
int itisduplicate(int *mat);
// --------------- Prototype Func ----------------

int main()
{
	int i, j;
	char mat[9][9];
	for(i=0;i<9;i++)
	{
	    for(j=0;j<9;j++)
        {
            scanf(" %c", &mat[i][j]);
        }
	}

    //printf("%d", check_3x3(mat));
    //printf("%d", Vertical_check(mat));

	if(itissudoku(mat))
		printf("Valid");
	else
		printf("Invalid");
	return 0;
}

int itissudoku(char mat[9][9])
{
	if(check_3x3(mat) == 0 || Vertical_check(mat) == 0 || Horizontal_check(mat) == 0)
		return 0;
	return 1;
}

int check_3x3(char mat[9][9])
{
	int i, j, k, l, p, arr[9] = { 0 }, cnt=0;
	for(i=0;i<9;i+=3)
	{
		for(l=0;l<9;l+=3)
		{
			for(k=0;k<9;k+=3)
			{
				for(p=k;p<k+3;p++)
				{
					for(j=l;j<l+3;j++)
					{
						arr[cnt] = mat[p][j];
						//printf("%c", mat[p][j]);
						cnt++;
					}
					//printf("\n");
				}
				if(itisduplicate(arr) == 0)
					return 0;
				cnt=0;
			}
		}
	}
	return 1;
}

int Vertical_check(char mat[9][9])
{
	int i, j, k, arr[9] = { 0 }, cnt=0;
	for(i=0;i<9;i++)
	{
		for(j=0;j<9;j++)
		{
			arr[cnt] = mat[j][i];
			cnt++;
		}
		if(itisduplicate(arr) == 0)
			return 0;
        cnt=0;

	}
	return 1;
}

int Horizontal_check(char mat[9][9])
{
	int i, j, k, arr[9] = { 0 }, cnt=0;
	for(i=0;i<9;i++)
	{
		for(j=0;j<9;j++)
		{
			arr[cnt] = mat[i][j];
			cnt++;
		}
		if(itisduplicate(arr) == 0)
			return 0;
		cnt=0;
	}
}
int itisduplicate(int *mat)
{
	int i, j, cnt=0;
	char arr[] = { '1','2','3','4','5','6','7','8','9'};
	for(i=0;i<9;i++)
	{
		for(j=0;j<9;j++)
		{
			if(arr[i] == mat[j])
				cnt++;
			if(cnt>1)
				return 0;
		}
		cnt = 0;
	}
	return 1;
}
