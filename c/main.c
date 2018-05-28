#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "post_fix.h"
#include "parse_tree.h"

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



    char* EEC = "(1 1-2)(2 2-3)(4 5)(6)";
    char* EEC2 = "(1*2 3-2 1-2)";

    char* post_fix1 = PostFix(EEC);
    pNode parse_tree1 = ParseTree(post_fix1);

    char* post_fix2 = PostFix(EEC2);
    pNode parse_tree2 = ParseTree(post_fix2);

    printf("PostFix(EEC) is %s\n", post_fix1);
    printf("Parse_tree_eec is: ");
    PostOrder(parse_tree1);
    printf("\n");
    eec2hb(parse_tree1);
    printf("Parse_tree_hb is: ");
    PostOrder(parse_tree1);
    printf("\n");
    GetRegularHb(parse_tree1);
    PostOrder(parse_tree1);
    printf("\n");
    printf("\n");


    printf("PostFix(EEC2) is %s\n", post_fix2);
    printf("Parse_tree_eec2 is: ");
    PostOrder(parse_tree2);
    printf("\n");
    eec2hb(parse_tree2);
    printf("Parse_tree_hb2 is: ");
    PostOrder(parse_tree2);
    printf("\n");
    GetRegularHb(parse_tree2);
    PostOrder(parse_tree2);
    printf("\n");
    printf("\n");

    fclose(fp);

    return 1;

}
