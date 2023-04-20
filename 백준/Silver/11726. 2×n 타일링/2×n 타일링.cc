#include <bits/stdc++.h>
using namespace std;
int n;
map<int, int> mp;
int main(){
    cin >> n;
    mp.insert({1,1});
    mp.insert({2,2});
    for(int i = 3; i <= n; i++){
        mp[i] = (mp[i - 1] + mp[i - 2]) % 10007;
    }
    cout << mp[n] << '\n';
    return 0;
}