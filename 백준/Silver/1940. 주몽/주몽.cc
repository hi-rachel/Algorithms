#include <bits/stdc++.h>
using namespace std;
int n, m, p[100004], cnt;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> n >> m;
    for(int i = 0; i < n; i++){
        cin >> p[i];
    }
    for(int i = 0; i < n; i++){
        for(int j = i+1; j < n; j++){
            if(p[i]+p[j] == m) cnt++;
        }
    }
    cout << cnt << '\n';
    return 0;
}