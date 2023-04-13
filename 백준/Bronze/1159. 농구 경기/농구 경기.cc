#include <bits/stdc++.h>
using namespace std;
int n, a[26];
string s, ret;

int main(){
    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> s;
        a[s[0] - 'a']++;
    }
    for(int i = 0; i < 26; i++){
        if(a[i] >= 5) ret += i + 'a';
    }
    if(ret.length()) cout << ret << '\n';
    else cout << "PREDAJA" << '\n';
    return 0;
}