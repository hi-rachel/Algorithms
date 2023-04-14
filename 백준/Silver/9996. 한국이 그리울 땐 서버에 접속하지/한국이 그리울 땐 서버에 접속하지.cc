#include <bits/stdc++.h>
using namespace std;
int n;
string p, a;
int main(){
    cin >> n;
    cin >> p;
    int idx = p.find('*');
    string pre = p.substr(0, idx);
    string suf = p.substr(idx + 1);
    for(int i = 0; i < n; i++){
        cin >> a;
        if(pre.size() + suf.size() > a.size()) cout << "NE\n";
        else{
            if(pre == a.substr(0, pre.size()) && suf == a.substr(a.size() - suf.size())) cout << "DA\n";
            else cout << "NE\n";
        }
    }
    return 0;
}
