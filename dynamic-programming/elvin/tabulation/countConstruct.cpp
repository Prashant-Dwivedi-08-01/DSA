#include<bits/stdc++.h>
using namespace std; 

int countConstruct(string target, vector<string> words){
    vector<int> table(target.size()+1, 0);
    table[0] = 1;
    for(int i = 0; i<= target.size(); i++){
        if(table[i] >= 1){
            for(auto &word: words){
                if(target.substr(i, word.length()) == word) table[i + word.length()] += table[i];
            }
        }
    }

    return table[target.length()];
}

int main() 
{
    vector<string> words1 = {"ab", "abc", "cd", "def", "abcd"};
    cout<<countConstruct("abcdef", words1)<<endl;

    vector<string> words2 = {"bo", "rd", "ate", "t", "ska", "sk", "boar"};
    cout<<countConstruct("skateboard", words2)<<endl;

    vector<string> words4 = {"purp", "p", "ur", "le", "purpl"};
    cout<<countConstruct("purple", words4)<<endl;

    vector<string> words3 = {"ee", "ee", "eee", "eeee", "eeeee", "eeeeee", "eeeeee"};
    cout<<countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee", words3)<<endl;
}