#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define N 20
#define R 10

int a[N];

void gen_random(int upper_bound)
{
	int i;
	srand(time(NULL));
	for(i=0;i<N;i++)
		a[i] = rand() % upper_bound;
}

int howmany(int value)
{
	int count = 0, i;
	for(i=0;i<N;i++)
		if(a[i]==value)
			++count;
	return count;
}

int find_max(int p[])
{
	int i, temp;
	for(i=1;i<R;i++)
	{
		if(p[0]<p[i])
			p[0]=p[i];
	}
	return p[0];
}

int main(void)
{
	int i, j, max, histogram[R]={0};
	gen_random(R);
	//statistics
	for(i=0;i<N;i++)
	{
		histogram[a[i]]++;
	}
	//raw data
	printf("num\tfreq\t\n");
	for(i=0;i<R;i++)
	{
		printf("%d\t%d\t\n", i, histogram[i]);
	}
	//find the maxmum
	//max = find_max(histogram);
	//histogram
	printf("\nrandom histogram: \n");
	for(i=0;i<R;i++)
		printf("%d\t",i);
	printf("\n");
	for(j=0;j<10;j++)
	{
		for(i=0;i<R;i++)
		{
			if(histogram[i]>0)
			{
				printf("*\t");
				histogram[i]--;
			}else{
				printf(" \t");
			}
		}
		printf("\n");
	}
	return  0;
}
