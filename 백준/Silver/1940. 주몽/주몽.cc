#include <bits/stdc++.h>
using namespace std;
int n, m, a, g[15004], ans;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> n >> m;
    for(int i = 0; i < n; i++){
        cin >> g[i];
    }
    for(int i = 0; i < n; i++){
        for(int j = i + 1; j < n; j++){
            if(g[i] + g[j] == m){
                ans++;
            }
        }
    }
    cout << ans << '\n';
    return 0;
}