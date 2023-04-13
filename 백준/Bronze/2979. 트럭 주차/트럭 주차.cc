#include <bits/stdc++.h>
using namespace std;
int A, B, C, a, b, p[104], ret;
int main(){
    cin >> A >> B >> C;
    for(int i = 0; i < 3; i++){
        cin >> a >> b;
        for(int j = a; j < b; j++) p[j]++;
    }
    for(int i = 1; i < 100; i++){
        if(p[i]){
            if(p[i] == 1) ret += A;
            else if(p[i] == 2) ret += B * 2;
            else if(p[i] == 3) ret += C * 3;
        }
    }
    cout << ret << '\n';
    return 0;
}