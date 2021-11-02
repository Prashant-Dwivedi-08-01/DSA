#include <bits/stdc++.h>
using namespace std;

vector<vector<string>> allConstruct(string target, vector<string> words)
{
    int size = target.size();
    if (size == 0)
    {
        vector<vector<string>> v;
        return v;
    }
    // vector<t> as = {1,3};
    vector<vector<string>> waysFromThisNode;
    for (auto &word : words)
    {
        auto pos = target.find(word);
        if (pos != string::npos && pos == 0)
        {
            string subString = target.substr(word.size(), size - pos);
            vector<vector<string>> s = allConstruct(subString, words);
            if (s.size() == 0)
            {
                vector<string> temp;
                temp.insert(temp.begin(), word);
                waysFromThisNode.insert(waysFromThisNode.begin(), temp);
            }
            else
            {
                for (auto &temp : s)
                {
                    temp.insert(temp.begin(), word);
                    waysFromThisNode.insert(waysFromThisNode.begin(), temp);
                }
            }
        }
    }
    return waysFromThisNode;
}

int main()
{
    vector<string> words1 = {"ab", "abc", "cd", "def", "abcd"};
    vector<vector<string>> result = allConstruct("abcdef", words1);

    // vector<string> words4 = {"purp", "p", "ur", "le", "purpl"};
    //  vector<vector<string>> result = allConstruct("purple", words4);
    int count = 1;
    for (auto &i : result)
    {
        cout<<"Way "<<count<<": ";
        for (auto &j : i)
            cout << j << " ";
        cout << endl;
        count++;
    }
}