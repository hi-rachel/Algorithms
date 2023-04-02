#include <bits/stdc++.h>
using namespace std;
string word, temp;
int main(){
    cin >> word;
    temp = word;
    reverse(temp.begin(), temp.end());
    if(word == temp) cout << 1 << '\n';
    else cout << 0 << '\n';
    return 0;
}