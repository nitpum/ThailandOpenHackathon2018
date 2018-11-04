#include <stdio.h>
#include <string.h>
struct data
{
    int CUSTOMER_ID;
    char REDEMP_DT[100];
    char REDEMP_TM[100];
    char CAT_DESC[100];
    char SUB_CAT_DESC[100];
    char PRNTR_DESC[100];
    char REDEEM_TYPE_DESC[100];
    char CMPGN_TYPE_DESC[100];
    char CHNL[100];
    char input[11][100];
};
struct data data[1000000];
int main ()
{
    int count = 0;
    char str[10000],*token;
    for(int i=0;fgets(str,sizeof(str),stdin)!=NULL;i++)
    {
        count=0;
        /*token=strtok(str,"|");
        while(token!=NULL)
        {
            token = strtok(NULL,"|");
            printf(">%s\n",token);
            strcpy(data[i].input[count++],token);
        }*/
    }

}

