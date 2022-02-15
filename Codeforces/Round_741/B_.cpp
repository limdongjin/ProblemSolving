#include <iostream>
#include <vector>
using namespace std;

void solve(int k, string str_n){
    vector<int> num_table(11);
    for (const auto &item : str_n)
        num_table[item - '0'] += 1;

    // 1. (1,4,6,8,9) 를 포함한다면, 그 숫자를 출력
    for (const auto &item : vector<int>({1,4,6,8,9})){
        if (num_table[item]){
            cout << 1 << "\n";
            cout << item << "\n";
            return;
        }
    }

    // 2. (2, 3, 5, 7) 에 속한 같은 숫자를 두개 이상 가졌다면, 그 숫자 두개를 출력
    // ex, 22 33 55 77
    for (const auto &item : vector<int>({2, 3, 5, 7})){
        if (num_table[item] > 1){
            cout << 2 << "\n";
            cout << item << item << "\n";
            return;
        }
    }

    // 3. str_n 에 2를 포함하면서, 2로 시작하지않으면,
    // 시작숫자+2 조합으로 출력. (사실 굳이 시작숫자를 고르지 않아도 무방하지만)
    // 4. str_n 에 5를 포함하면서, .....
    // 3 과 동일 로직
    for (const auto& item : vector<int>({2, 5})){
        if(num_table[item] && str_n[0]-'0' != item){
            cout << 2 << "\n";
            cout << str_n[0] << item << "\n";
            return;
        }
    }

    // 5. (2,3,7) 을 모두 포함 -> 27
    if (str_n[0] == '2'){
        cout << 2 << "\n";
        cout << 27 << "\n";
        return;
    }
    // 6. (5,3,7) 을 모두 포함 -> 57
    cout << 2 << "\n";
    cout << 57 << "\n";
}

int main(){
    int t, k;
    string str_n;

    cin >> t;

    while (t--){
        cin >> k;
        cin >> str_n;
        solve(k, str_n);
    }
    return 0;
}