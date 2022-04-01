#include<bits/stdc++.h>
using namespace std; 

bool canConstruct(string target, vector<string> words){
    vector<bool> table(target.size()+1, false);
    table[0] = true;
    for(int i = 0; i<= target.size(); i++){
        if(table[i] == true){
            for(auto &word: words){
                if(target.substr(i, word.length()) == word) table[i + word.length()] = true;
            }
        }
    }
    return table[target.length()];
}

int main() 
{
    vector<string> words = {"ab", "abc", "cd", "def", "abcd"};
    cout<<canConstruct("abcxdef", words);
}