#include <bits/stdc++.h>
using namespace std;
int n, m;
string a;
map<int, string> mp;
map<string, int> mp2;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> n >> m;
    for(int i = 1; i <= n; i++){
        cin >> a;
        mp[i] = a;
        mp2[a] = i;
    }
    for(int i = 1; i <= m; i++){
        cin >> a;
        if(atoi(a.c_str()) == 0){
            cout << mp2[a] << '\n';
        } else {
            cout << mp[atoi(a.c_str())] << '\n';
        }
    }
    return 0;
}