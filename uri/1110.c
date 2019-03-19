#include <stdio.h>

int incrementPosition(int position, int queueSize)
{
    return (position != (queueSize - 1)) ? position + 1 : 0;
}

int pop(int max, int fila[max], int *init)
{
    int aux = fila[(*init)];
    (*init) = incrementPosition((*init), max);
    return aux;
}

int push(int max, int fila[max], int *end, int val)
{
    (*end) = incrementPosition((*end), max);
    fila[(*end)] = val;
}

void fill(int max, int (*fila)[max], int *fim)
{
    int i;
    for (i = 0; i < max; i++) {
        (*fila)[i] = i + 1;
    }
    (*fim) = max - 1;
}

void print(int max, int *fila, int start, int end) {
    int i = 0;
    do {
        printf("%d%s", fila[start], (start == end) ? "\n" : ", ");
        start = incrementPosition(start, max);
    } while (start != incrementPosition(end, max));
}

int main()
{
    int n;
    scanf("%d", &n);
    while (n != 0) {
        int fBin = -1, fQueue = -1, iBin = 0, iQueue = 0;
        int toEnd, toBin;
        int queue[n], bin[n];
        fill(n, &queue, &fQueue);

        int i;
        for(i = 0; i < (n - 1); i++) {
            toBin = pop(n, queue, &iQueue);
            toEnd = pop(n, queue, &iQueue);

            push(n, queue, &fQueue, toEnd);
            push(n, bin, &fBin, toBin);
        }

        printf("Discarded cards: ");
        print(n, bin, iBin, fBin);
        printf("Remaining card: %d\n", queue[iQueue]);
        scanf("%d", &n);
    }
    return 0;
}