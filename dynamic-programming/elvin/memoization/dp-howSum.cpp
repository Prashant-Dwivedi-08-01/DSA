#include<bits/stdc++.h>
using namespace std; 

vector<int> result;
unordered_map<int, pair<bool,vector<int>> > memo;

bool howSum(int targetSum, vector<int> numbers){
    if(targetSum == 0) return true;
    if(targetSum < 0) return false;

    auto it = memo.find(targetSum);
    if(it != memo.end()){
        result = it->second.second;
        return it->second.first;
    }

    for(auto &num : numbers){
        int remainder = targetSum - num;
        if(howSum(remainder, numbers) == true) {
            result.push_back(num);
            memo.insert({ targetSum,{true, result} });
            return true;
        }
    }
    memo.insert({ targetSum,{false, result} });
    return false;
}

int main() 
{
    vector<int> v = {7, 1,2};
    if(howSum(300, v))
        for(auto &num: result) cout<<num<<" ";
    else
        cout<<"Sum not possible";
}