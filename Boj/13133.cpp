#include <cstdio>
#include <assert.h>
typedef struct Human{
    int mother;
    int farther;
    int status = 1;
} Human;
Human *Humans[501];
int initHumans();
int solve(int n);

int main(){
    int n;
    n = initHumans();
    printf("%d", solve(n));
}

int initHumans(){
    int n;
    scanf("%d", &n);
    int m, idx = 1, mother, farther, tmp;
    tmp = n;
    while(tmp--){
        Human* h = new Human;
        scanf("%d %d", &mother, &farther);
        h->mother = mother;
        h->farther = farther;
        Humans[idx++] = h;
    }
    scanf("%d", &m);
    for(int i =0;i<m;i++){
        scanf("%d", &tmp);
        Humans[tmp]->status = 0;
    }
    return n;
}

int solve(int n){
    int cnt = 0;
    for(int i = 1; i <= n; i++){
        if(Humans[i]->status == 0 ||
            Humans[i]->mother == 0 ||
            Humans[i]->farther == 0) continue;
        if(Humans[Humans[i]->mother]->status == 0
           || Humans[Humans[i]->farther]->status == 0)
            continue;
        cnt++;
    }
    return cnt;
}