#include <stdio.h>
#include <stdlib.h>


typedef struct _tag_stack_
{
    char a[20];
    int top;
}Sqstack;


Sqstack* InitStack(){
    Sqstack *ret = NULL;
    ret = (Sqstack*)malloc(sizeof(Sqstack));
    if(ret)
        ret ->top = 0;
    return ret;
}


int Push(Sqstack* stack, char data){
    stack->a[stack->top] = data;
    stack->top++;
    return 1;
}

void Play(Sqstack* stack){
    int i;
    if (stack->top == 0)
        printf("Empty stack\n");

    for(i = 0; i < stack->top; i++){
        printf("The data is %c\n", stack->a[i]);
    }
}

int Pop(Sqstack* stack, char* data){
    if (stack->top == 0)
        printf("Nothing to pop\n");
    else{
        stack->top --;
        *data = stack->a[stack->top];
    }
    return 1;
}

char* strcat_c(char* str, char c){

    int len = strlen(str);
    char* str2 = malloc(len +1 +1);
    strcpy(str2, str);
    str2[len] = c;
    str2[len+1] = '\0';
    return str2;

}

char* PostFix (char* eec){
    int i;
    char symble;
    int len;
    Sqstack* stack;
    stack = InitStack();
    
    len = strlen(eec);
    char* PostFix_eec = malloc(len);

    for (i=0; i<strlen(eec); i++)
    {
        switch (eec[i]){
            case '(':
                Push(stack, eec[i]);
                break;
            case '-':
            case '*':
                Push(stack, eec[i]);
                break;
            case ')':
                while(stack->top != 0){
                    Pop(stack, &symble);
                    if(symble != '(')
                        PostFix_eec = strcat_c(PostFix_eec, symble);
                }
                
                if(i != strlen(eec)-1)
                    Push(stack, '&');

                break;
            case ' ':
                if((stack->a[stack->top-1] == '-') || (stack->a[stack->top-1] == '*')){
                    
                    Pop(stack, &symble);
                    PostFix_eec = strcat_c(PostFix_eec, symble);
                }
                Push(stack, '|');
                break;

            default:
                PostFix_eec = strcat_c(PostFix_eec, eec[i]);
        }
    }
    return PostFix_eec;

}


int main()
{
    char* eec = "(1 1-2)(2 2-3)(4 5)(6)";
    printf("%s\n", PostFix(eec));

}
