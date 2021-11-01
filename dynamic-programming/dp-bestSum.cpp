#include<bits/stdc++.h>
using namespace std; 

vector<int> result;
vector<int> shortestResult;
unordered_map<int, pair<bool,vector<int>> > memo;

bool bestSum(int targetSum, vector<int> numbers){
    if(targetSum == 0) return true;
    if(targetSum < 0) return false;

    auto it = memo.find(targetSum);
    if(it != memo.end()){
        result = it->second.second;
        // return it->second.first;
    }

    for(auto &num : numbers){
        int remainder = targetSum - num;
        if(bestSum(remainder, numbers) == true) {
            result.push_back(num);
            if(result.size() <= shortestResult.size()) shortestResult = result;
            memo.insert({ targetSum,{true, result} });
        }
    }
    memo.insert({ targetSum,{false, result} });
    return false;
}

int main() 
{
    vector<int> v = {1, 4 , 3, 2, 2};
    if(bestSum(7, v))
        for(auto &num: result) cout<<num<<" ";
    else
        cout<<"Sum not possible";
}