#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_SIZE_EEC 100
#define MAX_SIZE_MTG 100

int main(int argc, char* argv[]){
    char mtg[MAX_SIZE_EEC][MAX_SIZE_MTG];
    char task_info[5][MAX_SIZE_MTG];
    char formula[MAX_SIZE_EEC][MAX_SIZE_MTG];
    char eec[MAX_SIZE_EEC];
    FILE *fp;

    int i = 0;
    int j = 0;

    if((fp = fopen(argv[1], "r")) == NULL)
        printf("fail to open .mtg\n");

    /*Read data from .mtg into mtg*/
    while(fgets(mtg[i], MAX_SIZE_EEC, fp) != NULL){
        strcpy(task_info[i], strtok(mtg[i], ":"));
        strcpy(formula[i], strtok(NULL, ""));
        printf("%s\n", task_info[i]);
        printf("%s\n", formula[i]);
        i++;
    }

    


    fclose(fp);
    return 1;

}
