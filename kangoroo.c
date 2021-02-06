#include <stdio.h>

int kangaroo(int x1, int v1, int x2, int v2) {
        
        int result = 0;

        for (int i = 0; i < 10000; i++) {
            int x = x1 + (v1 * i);
            int y = x2 + (v2 * i);
            if (x == y) {
                result = 1;
                break;
            }
        }
        return result;
    }


int main()
{

    int x1, v1, x2, v2;
    scanf("%d %d %d %d", &x1, &v1, &x2, &v2);
    
    int answer = kangaroo(x1, v1, x2, v2);

    if (answer==1){printf("YES\n");}
    else if(answer == 0){printf("NO\n");}


    return 0;
}

