#include <cstdio>
#include <assert.h>
typedef struct Human{
    int mother;
    int farther;
    int status = 1;
} Human;
Human *Humans[501];

int initHumans();
int solve(Human* humans[], int n);
void TestSolve();

int main(){
    int n;
    TestSolve();
    n = initHumans();
    printf("%d", solve(Humans, n));
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
int solve(Human* humans[], int n){
    int cnt = 0;
    for(int i = 1; i <= n; i++){
        if(humans[i]->status == 0 ||
           humans[i]->mother == 0 ||
           humans[i]->farther == 0) continue;
        if(humans[humans[i]->mother]->status == 0
           || humans[humans[i]->farther]->status == 0)
            continue;
        cnt++;
    }
    return cnt;
}
void TestSolve(){
    Human *testers[501];
    testers[1] = new Human{0, 0, 0};
    testers[2] = new Human{0, 0, 0};
    testers[3] = new Human{0, 0, 0};
    testers[4] = new Human{2, 1, 0};
    testers[5] = new Human{0, 0, 0};
    testers[6] = new Human{2, 1, 0};
    testers[7] = new Human{0, 0, 0};
    testers[8] = new Human{2, 1, 0};
    testers[9] = new Human{2, 1, 1};
    testers[10] = new Human{0, 0, 1};
    testers[11] = new Human{0, 0, 1};
    testers[12] = new Human{0, 0, 1};
    testers[13] = new Human{0, 0, 0};
    testers[14] = new Human{0, 0, 0};
    testers[15] = new Human{14, 0, 1};
    testers[16] = new Human{14, 0, 1};
    testers[17] = new Human{14, 0, 0};
    assert(solve(testers, 17) == 0);
}