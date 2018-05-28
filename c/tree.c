#include <stdio.h>
#include <stdlib.h>
#include "post_fix.h"

typedef char element;

typedef struct tree{
    element data;
    struct tree *lchild;
    struct tree *rchild;
}Tree, *pTree;


pTree InitTree();
void PreOrder(pTree);
void InOrder(pTree);
void PostOrder(pTree);


int main(){
    pTree tree;
    printf("Please input data, end with '#': ");
    tree = InitTree();

    /*
    printf("PreOrder is : ");
    PreOrder(tree);
    printf("\n");
    printf("InOrder is : ");
    InOrder(tree);
    printf("\n");
    printf("Postorder is : ");
    PostOrder(tree);
    printf("\n");
    */
    return 1;
}


pTree GetParseTree(char* PostFix){
    Sqstack* stack;
    stack = InitStack();
    pTree tree;

    int i = 0;
    for (i = 0; i<strlen(PostFix); i++)
    {
        if(IsOperator(PostFix[i]))
            CreateNode(stack);
        else 
            Pop(stack, PostFix[i]);
        
    }
}

bool IsOperator(char ch)
{
    switch (ch){
        case '|':
        case '&':
            return true;
        default:
            return false;
    }
}




pTree InitTree(){
    char input;
    pTree tree = NULL;
    
    scanf("%c", &input);
    if(input == '#')
        tree = NULL;
    else{
        tree = (Tree*)malloc(sizeof(Tree)+1);
        if(!tree)
            printf("Error in allocating memory to tree\n");
        else{
            tree->data = input;
            tree->lchild = InitTree();
            tree->rchild = InitTree();
        }
    }
    return tree;
}
        

void PreOrder(pTree tree){
    if(tree){
        printf("%c", tree->data);
        PreOrder(tree->lchild);
        PreOrder(tree->rchild);
    }
}
        

void InOrder(pTree tree){
    if(tree){
        InOrder(tree->lchild);
        printf("%c", tree->data);
        InOrder(tree->rchild);
    }
}


void PostOrder(pTree tree){
    if(tree){
        PostOrder(tree->lchild);
        PostOrder(tree->rchild);
        printf("%c", tree->data);
    }
}
