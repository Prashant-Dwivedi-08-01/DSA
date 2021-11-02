#include<bits/stdc++.h>
using namespace std; 

long long fib(int n){
    vector<long long> table(n+1);
    table[1] = 1;
    for(int i = 2; i<=n ; i++){
        table[i] = table[i-1] + table[i-2];
    }
    return table[n];
}

int main() 
{
    cout<<fib(4)<<endl;
    cout<<fib(6)<<endl;
    cout<<fib(10)<<endl;
    cout<<fib(50)<<endl;
}