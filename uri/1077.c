#include <stdio.h>
#include <stdlib.h>

typedef struct node {
    char val;
    struct node* next;
} node;

int len(char *string);
void push(node **pilha, char value);
char pop(node **pilha);
int isOperator(char c);
int getPriority(char c);
void transform(char *);

int main()
{
    int quantity = 0, i = 0;
    scanf("%d", &quantity);
    char expr[quantity][1000];
    while (quantity > i) {
        scanf("%s", expr[i]);
        i++;
    };

    i = 0;
    while (quantity > i) {
        transform(expr[i]);
        printf("\n");
        i++;
    }
    
}

void transform(char *expr)
{
    int exprLen = len(expr), i;
    node *pOperadores = NULL;

    for (i = 0; i < exprLen; i++) {
        char c = expr[i];
        if (!isOperator(c)) {
            printf("%c", c);
            continue;
        }

        if (c == '(') {
            push(&pOperadores, c);
            continue;
        }

        if (c == ')') {
            while(pOperadores != NULL && pOperadores->val != '(') {
                printf("%c", pop(&pOperadores));
            }

            pop(&pOperadores);
            continue;
        }

        while (pOperadores != NULL && getPriority(pOperadores->val) >= getPriority(c)) {
            printf("%c", pop(&pOperadores));
        }

        push(&pOperadores, c);
    }

    while (pOperadores != NULL) {
        printf("%c", pop(&pOperadores));
    }
}

int len(char *string)
{
    int len = 0;
    while(string[len] != '\0') {
        len++;
    }
    return len;
}

void push(node **pilha, char value)
{
    node *new = (node *) malloc(sizeof(node *));
    new->val = value;
    
    new->next = (*pilha);
    (*pilha) = new;
}

char pop(node **pilha)
{
    node *bin = (*pilha);
    char val  = (*pilha)->val;
    (*pilha)  = (*pilha)->next;
    free(bin);

    return val;
}

int isOperator(char c)
{
    return
        c == '^' ||
        c == '*' || c == '/' ||
        c == '-' || c == '+' ||
        c == '(' || c == ')';
}

int getPriority(char c)
{
    switch(c) {
        case '^': return 3; break;
        case '*': case '/': return 2; break;
        case '-': case '+': return 1; break;
        default:  return 0; break;
    }
}
