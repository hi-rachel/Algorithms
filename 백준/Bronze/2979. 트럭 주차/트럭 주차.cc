#include <bits/stdc++.h>
using namespace std;
int A, B, C, a, b, p[104], ret;
int main(){
    cin >> A >> B >> C;
    for(int i = 0; i < 3; i++){
        cin >> a >> b;
        for(int j = a; j < b; j++){
            p[j]++;
        }
    }
    for(int j = 1; j < 100; j++){
        if(p[j]){
            if(p[j] == 1) ret += A;
            else if(p[j] == 2) ret += B * 2;
            else if(p[j] == 3) ret += C * 3;
        }
    }
    cout << ret << '\n';
    return 0;
}