#include<bits/stdc++.h>
using namespace std; 

int gridTraveler(int m, int n){
    vector<vector<int>> table( m+1 , vector<int> (n+1, 0));

    cout<<endl;
    table[1][1] = 1;
    for(int i = 0; i <= m; i++){
        for(int j = 0; j <= n; j++){
            int currentElement = table[i][j];
            if(i+1 <= m) table[i+1][j] += currentElement;
            if(j+1 <= n) table[i][j+1] += currentElement;
        }
    }
    return table[m][n];
}

int main() 
{
    cout<<gridTraveler(3,2);
}