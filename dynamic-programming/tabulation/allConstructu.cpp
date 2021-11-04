#include<bits/stdc++.h>
using namespace std; 

void printVector(vector<vector<string>> v){
    for(auto &vec: v){
        cout<<"Way: ";
        for(auto &str: vec){
            cout<<str<<" ";
        }
        cout<<endl;
    }
}

vector<vector<string>> countConstruct(string target, vector<string> words){
    vector<vector<vector<string>>> table(target.size()+1);

    for(int i = 0; i<= target.size(); i++){
        if(table[i].size() || i == 0){
            for(auto &word: words){
                if(target.substr(i, word.length()) == word){
                    //  table[i + word.length()] += table[i];
                    if(i==0){
                        vector<string>temp;
                        temp.push_back(word);
                        table[i + word.length()].push_back(temp);
                    }else{
                        for(auto &presentWays: table[i]){
                         presentWays.push_back(word);
                         table[i + word.length()].push_back(presentWays);
                        }
                    }
                     
                }
            }
        }
    }

    return table[target.length()];
}

int main() 
{
    vector<string> words1 = {"ab", "abc", "cd", "def", "abcd","ef", "c"};
    printVector(countConstruct("abcdef", words1));

    // vector<string> words2 = {"bo", "rd", "ate", "t", "ska", "sk", "boar"};
    // printVector(countConstruct("skateboard", words2));

    // vector<string> words4 = {"purp", "p", "ur", "le", "purpl"};
    // printVector(countConstruct("purple", words4));

    // vector<string> words3 = {"ee", "ee", "eee", "eeee", "eeeee", "eeeeee", "eeeeee"};
    // printVector(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee", words3));
}