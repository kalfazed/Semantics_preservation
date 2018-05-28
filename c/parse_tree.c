#include <stdio.h>
#include <string.h>
#include <stdbool.h>

#include "parse_tree.h"
#include "post_fix.h"



/* Create the new node */
pNode CreateNode(char data, pNode lchild, pNode rchild){
    pNode node = NULL;
    node = (Node*)malloc(sizeof(Node)+1);
    if(!node)
        printf("Error in allocating the memory to node\n");
    else{
        node -> value = data;
        node -> left = lchild;
        node -> right = rchild;
    }
    return node;
}



/* Initialize the stack */
NodeStack* InitNodeStack(){
    NodeStack *ret = NULL;
    ret = (NodeStack*)malloc(sizeof(NodeStack));
    if(ret)
        ret ->top = 0;
    return ret;
}


int PushNode(NodeStack* stack, Node* node){
    stack->node[stack->top] = node;
    stack->top++;
    return 1;
}

void PlayNode(NodeStack* stack){
    int i;
    if (stack->top == 0)
        printf("Empty stack\n");

    for(i = 0; i < stack->top; i++){
        printf("The data is %c\n", stack->node[i]->value);
    }
}

pNode PopNode(NodeStack* stack){
    if (stack->top == 0){
        printf("Nothing to pop\n");
        return NULL;
    }
    else{
        stack->top --;
        return stack->node[stack->top];
    }
}


void PostOrder(pNode tree){
    if(tree){
        PostOrder(tree->left);
        PostOrder(tree->right);
        printf("%c", tree->value);
    }
}


bool IsOperator(char ch){
    switch (ch){
        case '|':
        case '&':
        case '*':
        case '-':
            return true;

        default:
            return false;
    }
}

pNode ParseTree(char* PostFix_EEC){
    int i, data;
    NodeStack* stack;
    pNode node;
    char ch = NULL;

    stack = InitNodeStack();

    for(i = 0; i<strlen(PostFix_EEC); i++){
        ch = PostFix_EEC[i];
        if (IsOperator(ch)){
            pNode rchild = PopNode(stack);
            pNode lchild = PopNode(stack);
            node = CreateNode(ch, lchild, rchild);
            PushNode(stack, node);
        }else{
            node = CreateNode(ch, NULL, NULL);
            PushNode(stack, node);
        }
    }
    node = PopNode(stack);
    return node;
}

void eec2hb(pNode tree){
    if (tree){
        eec2hb(tree->left);
        eec2hb(tree->right);

        if((tree->value == '-'))
        {
            tree->value = tree->left->value;
            tree->left = NULL;
            tree->right = NULL;
        }
        
        if((tree->value == '*'))
        {
            tree->left = NULL;
            tree->right = NULL;
            tree->value = NULL;
            tree = NULL;
        }
    }
}

void GetRegularHb(pNode tree){
    if (tree){
        GetRegularHb(tree->left);
        GetRegularHb(tree->right);
        
        if((tree->value == '|')){
            if(tree->left->value == NULL){
                tree->value = tree->right->value;
                tree->right = NULL;
            }
            else if(tree->right->value == NULL){
                tree->value = tree->left->value;
                tree->left = NULL;
            }
            else if(tree->left->value == tree->right->value){
                tree->value = tree->left->value;
                tree->left = NULL;
                tree->right = NULL;
            }
        }
    }
}




