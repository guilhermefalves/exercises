/**
 * Dada uma expressão qualquer com parênteses, indique se a quantidade de 
 * parênteses está correta ou não, sem levar em conta o restante da expressão.
 * Por exemplo: 
 *      a+(b*c)-2-a       está correto
 *      (a+b*(2-c)-2+a)*2 está correto
 *      (a*b-(2+c)  está incorreto
 *      2*(3-a))    está incorreto
 *      )3+b*(2-c)( está incorreto
 * Ou seja, todo parênteses que fecha deve ter um outro parênteses que abre
 * correspondente e não pode haver parênteses que fecha sem um previo parenteses
 * que abre e a quantidade total de parenteses que abre e fecha deve ser igual.
 * 
 * Como entrada, haverá N expressões (1 <= N <= 10000), cada uma delas com até 
 * 1000 caracteres. Saída O arquivo de saída deverá ter a quantidade de linhas
 * correspondente ao arquivo de entrada, cada uma delas contendo as palavras 
 * correct ou incorrect de acordo com as regras acima fornecidas.
 * 
 * @author Guilherme F Alves (Sistemas de informação)
 * UNESP - Bauru/SP
 */
#include <stdio.h>
#include <stdlib.h>

typedef struct node {
    char value;
    struct node *next;
} node;

char pop(node **stack)
{
    node *l    = (*stack);
    char value = (*stack)->value;
    (*stack)   = (*stack)->next;
    free(l);
    return value;
}

void push(node **stack, char val)
{
    node *new  = (node *)malloc(sizeof(node *));
    new->value = val;
    new->next  = (*stack);
    (*stack)   = new;
}


char *isValid(char *expr)
{
    int i = 0;
    node *pParenthese = NULL;
    while(expr[i] != '\0') {
        if (expr[i] == ')' && pParenthese == NULL) {
            return "incorrect";
        }

        if (expr[i] == ')') {
            pop(&pParenthese);
            i++;
            continue;
        }

        if (expr[i] == '(') {
            push(&pParenthese, expr[i]);
            i++;
            continue;
        }
        i++;
    }

    if (pParenthese != NULL) {
        return "incorrect";
    }

    return "correct";
}

int main()
{
    char expr[1000];
    while (scanf("%s", expr) != EOF) {
        printf("%s\n", isValid(expr));
    }
}