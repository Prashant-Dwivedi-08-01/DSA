#include<bits/stdc++.h>
using namespace std; 

unordered_map<int, bool> memo = {};

bool canSum(int targetSum , vector<int> numbers){
    if(targetSum == 0) return true;
    if(targetSum < 0) return false;

    auto it = memo.find(targetSum);
    if(it != memo.end()) return it->second;

    // for the present targetSum,substract the values from array from targetSum.
    for(auto &num: numbers){
        int remainder = targetSum - num;
        if(canSum(remainder, numbers) == true){
            memo.insert({ targetSum, true});
            return true;
        }
    }

    memo.insert({ targetSum, false});
    return false; // even after substracting all the values from numbers array we dont get any solution

}

int main() 
{
    vector<int> numbers = {5,2,2};
    cout<<canSum(900, numbers);
}