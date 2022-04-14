#include <stdio.h>
#define MaxSize 50
typedef int KeyType;
typedef int InfoType;
typedef struct 
{
	KeyType key;
	InfoType data;
}RecType;
/*≤Â»Î≈≈–Ú”–÷±Ω”≤Â»Î≈≈–Ú£¨’€∞Î≤Â»Î≈≈–Ú£¨œ£∂˚≈≈–Ú*/
//≥ı ºªØ–Ú¡–
void initRec(RecType R[],KeyType keys[],int n)
{
	for(int i=0;i<n;i++)
	{
		R[i].key=keys[i];
	}
}
// ‰≥ˆ–Ú¡–
void printRec(RecType R[],int n)
{
	for(int i=0;i<n;i++)
	{
		printf("%d ",R[i].key);
	}
	printf("\n");
}
//÷±Ω”≤Â»Î≈≈–ÚÀ„∑®
void directInsertSort(RecType R[],int n)
{
	RecType tmp;
	for(int i=1,j;i<n;i++)
	{
		tmp=R[i];j=i-1;
		while(j>=0&&tmp.key<R[j].key)
		{
			R[j+1]=R[j];
			j--;
		}
		R[j+1]=tmp;
	}
}
//’€∞Î≤Â»Î≈≈–Ú
void halfInsertSort(RecType R[],int n)
{
	RecType tmp;
	for(int i=1,low,high,mid;i<n;i++)
	{
		low=0,high=i-1;tmp=R[i];
		while(low<=high)
		{
			mid=(low+high)/2;
			if(tmp.key>R[mid].key) low=mid+1;
			else high=mid-1;
		}
		for(int j=i-1;j>high;j--)
			R[j+1]=R[j];
		R[high+1]=tmp;
	}
}
//œ£∂˚≤Â»Î≈≈–Ú
void shellInsertSort(RecType R[],int n)
{
	int gap=n/2;RecType tmp;
	while(gap>0)
	{
		
	}
}
void checkInsertSort()
{
	RecType R[MaxSize];
	KeyType keys[]={5,2,3,9,7,0,1,6,4,8};
	int n=10;
	initRec(R,keys,n);
	printf("≥ı ºªØ–Ú¡–:\t");
	printRec(R,n);
	printf("÷±Ω”≤Â»Î≈≈–Ú:\t");
	directInsertSort(R,n);
	printRec(R,n);
	initRec(R,keys,n);
	printf("’€∞Î≤Â»Î≈≈–Ú:\t");
	halfInsertSort(R,n);
	printRec(R,n);
}
void main()
{
	checkInsertSort();
}