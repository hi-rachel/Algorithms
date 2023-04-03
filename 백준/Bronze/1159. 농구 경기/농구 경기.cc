#include <bits/stdc++.h>
using namespace std;

int N, p[26];
string s, ans;
int main(){
    cin >> N;
    for(int i = 0; i < N; i++){
        cin >> s;
        p[s[0] - 'a']++;
    }
    for(int i = 0; i < 26; i++){
        if(p[i] >= 5) ans += (i + 'a');
    }
    if(ans.size()) cout << ans << '\n';
    else cout << "PREDAJA" << '\n';
    return 0;
}