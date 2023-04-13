#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int p[26];
string s;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> s;
    for(char a : s){
        p[a - 'a']++;
    }
    for(int i = 0; i < 26; i++){
        cout << p[i] << ' ';
    }
    return 0;
}