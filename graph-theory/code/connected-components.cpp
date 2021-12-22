#include <bits/stdc++.h>
using namespace std;

const int numberOfNodes = 6;
unordered_map<int, vector<int>> graph = {
    {0, {1, 5}},
    {1, {0, 4}},
    {2, {3}},
    {3, {2}},
    {4, {1, 5}},
    {5, {0, 4}}};
unordered_map<int, bool> visitedNodes = {
    {0, false},
    {1, false},
    {2, false},
    {3, false},
    {4, false},
    {5, false}};

vector<int> components(6);


void dfs(int node, int count)
{
    visitedNodes.insert({node, true});
    // cout << node << "->";
    components[node] = count;
    auto neighbours = graph.find(node)->second;
    for (auto &neighbour : neighbours)
    {
        auto isVisited = visitedNodes.find(neighbour);
        if (isVisited == visitedNodes.end())
        {
            cout << "Bad Node" << endl;
            return;
        }
        else if (!isVisited->second)
         dfs(neighbour,count);
    }
}

void findConnectedComponents(int n)
{
    int count = 0;
    for (int i = 0; i <= n; i++)
    {
        auto isVisited = visitedNodes.find(i);
        if (isVisited == visitedNodes.end())
        {
            cout << "Bad Node" << endl;
            return;
        }
        else if (!isVisited->second)
        {
            count++;
            dfs(i, count);
        }
            
    }
}


int main()
{
    char start_node = 'A';
    findConnectedComponents(6);
    for(auto &i: components){
        cout<<i<<" ";
    }
    cout << "END";
}