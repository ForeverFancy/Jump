#include <stdio.h>
#include <string.h>

int step[2][2000];
int map[10][10];
int n,count=0,stepcount=1;
int rowChange[]={1,1,-1,-1,2,2,-2,-2};
int colChange[]={2,-2,2,-2,1,-1,1,-1};

int judge(int i,int j)
{
    return i>=0 && i<n && j>=0 && j<n ;
}

void jump(int a,int b)
{
    int flag=0;
    for(int i=0;i<n;i++)
        for(int j=0;j<n;j++)
            if(map[i][j]==-1)
                flag=1;
    if(flag==0)
    {
        count++;
        FILE *fp=NULL;
        fp=fopen("D://solution.txt","a");
        for(int i=0;i<n*n-1;i++)
            fprintf(fp,"%d%d,",step[0][i],step[1][i]);
        fprintf(fp,"%d%d\n",step[0][n*n-1],step[1][n*n-1]);
        return;
    }
    for(int k=0;k<8;k++)
    {
        if (judge(a+rowChange[k],b+colChange[k]) && map[a+rowChange[k]][b+colChange[k]]==-1)
        {
            map[a+rowChange[k]][b+colChange[k]]=1;
            step[0][stepcount]=a+rowChange[k];
            step[1][stepcount]=b+colChange[k];
            stepcount++;
            jump(a+rowChange[k],b+colChange[k]);
            map[a+rowChange[k]][b+colChange[k]]=-1;
            stepcount--;
        }
    }

}

int main()
{
    printf("Please input the size:");
    scanf("%d",&n);
    memset(map,-1, sizeof(map));
    memset(step,-1, sizeof(step));
    map[0][0]=1;
    step[0][0]=0;
    step[1][0]=0;
    jump(0,0);
    printf("%d",count);
}