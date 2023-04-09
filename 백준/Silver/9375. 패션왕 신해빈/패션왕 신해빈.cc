#include <bits/stdc++.h>
using namespace std;
int t, n;
string a, b;
int main(){
    cin >> t;
    while(t--){
        map<string, int> _map;
        cin >> n;
        for(int i = 0; i < n; i++){
            cin >> a >> b;
            _map[b]++;
        }
        long long ret = 1;
        for(auto m : _map){
            ret *= ((long long)m.second + 1);
        }
        ret--;
        cout << ret << '\n';
    }
    return 0;
}