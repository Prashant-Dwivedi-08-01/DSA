#include<bits/stdc++.h>
using namespace std; 

vector<int> canSum(int targetSum, vector<int> numbers){
    // intialize the table
    vector<vector<int>> table(targetSum+1);
    for(int i = 0; i<= targetSum; i++){
        if(table[i].size() || i == 0){
            for(auto &num: numbers){
                if(i+num <= table.size()-1){
                    table[i+num] = table[i];
                    table[i+num].push_back(num);
                }
            }
        }
    }
    return table[targetSum];
}

int main() 
{
    vector<int> v ={5, 3, 4};
    vector<int> res =  canSum(7, v);
    for(auto &num: res){
        cout<<num<<" ";
    }   
    cout<<endl;
}