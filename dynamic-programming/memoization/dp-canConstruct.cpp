#include<bits/stdc++.h>
using namespace std; 

unordered_map<string, bool> memo;

bool canConstruct(string target, vector<string> words){
    int size = target.size();
    if(target.size() == 0) return true;

    auto it = memo.find(target);
    if(it != memo.end()) return it->second;

    for(auto &word: words){
        auto pos = target.find(word);
        if(pos != string::npos && pos == 0){
            string subString = target.substr(word.size(), size - pos);
            if(canConstruct(subString, words) == true){
                memo[target] = true;
                return true;
             }
         }
    }
    memo[target] = false;
    return false;
}

int main() 
{
    vector<string> words1 = {"ab", "abc", "cd", "def", "abcd"};
    vector<string> words2 = {"bo", "rd", "ate", "t", "ska", "sk", "boar"};
    vector<string> words3 = {"ee", "ee", "eee", "eeee", "eeeee", "eeeeee", "eeeeee"};
    cout<<canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee", words3);
}