typedef struct _tag_stack_
{
    char a[20];
    int top;
}Sqstack;


Sqstack* InitStack();
int Push(Sqstack*, char);
void Play(Sqstack*);
int Pop(Sqstack*, char*);
char* strcat_c(char*, char);
char* PostFix(char*);

