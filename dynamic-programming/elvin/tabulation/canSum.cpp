#include<bits/stdc++.h>
using namespace std; 

bool canSum(int targetSum, vector<int> numbers){
    // intialize the table
    vector<bool> table(targetSum+1, false);
    table[0] = true;
    for(int i = 0; i<= targetSum; i++){
        if(table[i]){
            for(auto &num: numbers){
                if(i+num <= table.size()-1)
                    table[i+num] = true;
            }
        }
    }
    return table[targetSum];
}

int main() 
{
    vector<int> v ={0, 3, 3};
    cout<<canSum(7, v);
}