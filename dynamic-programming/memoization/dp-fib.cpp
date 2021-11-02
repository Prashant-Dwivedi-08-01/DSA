#include<bits/stdc++.h>
using namespace std; 

unordered_map<int, long long> memo = {};

long long fib(int n){
    if(n <= 2) return 1;

    auto it = memo.find(n); // find if present fib call is already called once and stored in memo map
    if(it != memo.end()) return it->second;
    else {
        long long temp = fib(n-1) + fib(n-2);
        memo.insert({ n, temp }); // inserting the present call in memo so that it can be reused
        return temp;
    }
}

int main() 
{
    cout<<fib(8);
}