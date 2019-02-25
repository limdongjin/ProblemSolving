#include <iostream>
#include <string>

using namespace std;

int* checker_str(string input_str);
char checker_char(char input_char);
bool ebetAB(char target, char A, char B);
bool compareIntArr(int* arr1, int* arr2, int input_len);
void print_arr(int* input_arr, int input_len);
bool test_solution(string test_str, int* answer, int answer_len);

int main(void){
    string input_str = "undef";

    int tarr[4] = { 10, 2, 0, 2};
    int arr_len = sizeof(tarr)/sizeof(tarr[0]);

    string test_str = "This is String";

    while(getline(cin , input_str )){
        print_arr(checker_str(input_str), arr_len);
    }
}

int* checker_str(string input_str){
    int input_len = input_str.length();
    int *poutput = new int[4];

    poutput[0]=0;
    poutput[1]=0;
    poutput[2]=0;
    poutput[3]=0;
    for(int idx=0;idx < input_len; idx++ ) {
        switch(checker_char(input_str[idx])){
            case 'a':
                poutput[0] += 1;
                break;
            case 'A':
                poutput[1] += 1;
                break;
            case '0':
                poutput[2] += 1;
                break;
            case ' ':
                poutput[3] += 1;
                break;
        }
    }

    return poutput;
}

void print_arr(int* input_arr, int input_len){
    cout << input_arr[0];
    for(int idx = 1; idx < input_len; idx++){
        cout << " ";
        cout << input_arr[idx];
    }

    cout << "\n";
    return;
}

bool test_solution(string test_str, int* answer, int answer_len ){
    if(compareIntArr( checker_str(test_str) , answer, answer_len ) == true){
        print_arr( checker_str(test_str) , answer_len);
        print_arr( answer , answer_len);
        return true;
    }else{
        print_arr( checker_str(test_str) , answer_len );
        print_arr( answer, answer_len );
        return false;
    }
}

bool compareIntArr(int* arr1, int* arr2, int input_len){
    for (int idx = 0; idx < input_len; idx++){
        if(arr1[idx] != arr2[idx]){
            return false;
        }
    }
    return true;
}

bool ebetAB(char target, char A, char B){
    return target >= A && target <= B;
}

char checker_char(char input_char){
    // upper_case => return 'A';
    // down_case  => return 'a';
    // integer    => return '0';
    // blank      => return ' ';
    // wrong      => return '-';

    if(ebetAB(input_char, 'a', 'z')){
        return 'a';
    }else if( ebetAB(input_char, 'A', 'Z' )){
        return 'A';
    }else if( ebetAB(input_char, '0', '9')){
        return '0';
    }else if( input_char == ' ' ) {
        return ' ';
    }else{
        return '-';
    }
}