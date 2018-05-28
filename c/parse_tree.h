#include <stdbool.h>

typedef struct node
{
    char value;
    struct node *left;
    struct node *right;
    struct node *father;
}Node, *pNode;

typedef struct _node_stack_
{
    pNode node[20];
    int top;
}NodeStack;


NodeStack* InitNodeStack();
int PushNode(NodeStack*, Node*);
void PlayNode(NodeStack*);
pNode PopNode(NodeStack*);


pNode CreateNode(char, pNode, pNode);
void PostOrder(pNode);
bool IsOperator(char);
pNode ParseTree(char*);
void eec2hb(pNode);
void GetRegularHb(pNode);
