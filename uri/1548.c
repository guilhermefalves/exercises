#include <stdio.h>

void sort(int size, int (*fila)[size])
{
    int aux, i;
    for (size; size > 0; size--) {
        for (i = 0; i < (size - 1); i++) {
            if ((*fila)[i] < (*fila)[i + 1]) {
                aux            = (*fila)[i];
                (*fila)[i]     = (*fila)[i + 1];
                (*fila)[i + 1] = aux;
            }
        }
    }
}

int main()
{
    char *a;
    int n, m, p, notChanged = 0;
    int i;

    scanf("%d", &n);
    while (n > 0) {
        notChanged = 0;
        scanf("%d", &p);
        int fila[p], oFila[p];
        for (i=0; i < p; i++) {
            scanf("%d", &fila[i]);
            oFila[i] = fila[i];
        }

        sort(p, (&oFila));
        for (i = 0; i < p; i++) {
            if (fila[i] == oFila[i]) {
                notChanged++;
            }
        }

        printf("%d\n", notChanged);
        n--;
    }
    return 0;
}
