#include<bits/stdc++.h>
using namespace std; 

unordered_map<string, int> memo;

int canConstruct(string target, vector<string> words){
    int size = target.size();
    if(target.size() == 0) return 1;
    
    auto it = memo.find(target);
    if(it != memo.end()) return it->second;

    int totalWaysForThisNode = 0;
    for(auto &word: words){
        auto pos = target.find(word);
        if(pos != string::npos && pos == 0){
            string subString = target.substr(word.size(), size - pos);
            int numberOfWaysFromThisBranch = canConstruct(subString, words);
                // memo[target] = true;
            totalWaysForThisNode += numberOfWaysFromThisBranch;
                // return true          //no early return should be done, all the substrings should be checked as we need total number of ways

         }
    }
    memo[target] = totalWaysForThisNode;
    // return false;
    return totalWaysForThisNode;
}

int main() 
{
    vector<string> words1 = {"ab", "abc", "cd", "def", "abcd"};
    cout<<canConstruct("abcdef", words1)<<endl;

    vector<string> words2 = {"bo", "rd", "ate", "t", "ska", "sk", "boar"};
    cout<<canConstruct("skateboard", words2)<<endl;

    vector<string> words4 = {"purp", "p", "ur", "le", "purpl"};
    cout<<canConstruct("purple", words4)<<endl;

    vector<string> words3 = {"ee", "ee", "eee", "eeee", "eeeee", "eeeeee", "eeeeee"};
    cout<<canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", words3)<<endl;
}