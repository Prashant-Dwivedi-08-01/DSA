#include<bits/stdc++.h>
using namespace std; 

unordered_map<string, long long > memo = {};

long long gridTraveler(int m, int n){

    //base case : If there is no grid further or there is only one grid
    if(m == 1 && n == 1) return 1;
    if(m == 0 || n == 0) return 0;

    string key = to_string(m) + "," + to_string(n);

    auto it = memo.find(key);
    if(it != memo.end()) return it->second;
    else{
        long long temp = gridTraveler(m-1, n)  + gridTraveler(m, n-1);
        memo.insert({key, temp});
        return temp;
    }

}

int main() 
{
    cout<<gridTraveler(18,18);
}