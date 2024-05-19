#include<stdio.h>
int are[1000000];
int main()
{
    int i;
    are[0]=1;
    are[1]=2;
    for(i=2; i<100000; i++)
    {
        are[i]=(are[i-1]+are[i-2])%3;
        if(are[i]==2&&are[i-1]==1)
            break;
    }

    int n;
    while(scanf("%d",&n)!=EOF)
    {
        n=n%(i-1);
        if(are[n]==0) printf("yes\n");
        else printf("no\n");

    }
    return 0;
}