#include<bits/stdc++.h>
using namespace std; 

const int numberOfNodes = 6;
unordered_map<char, vector<char>> graph={
    {'A', {'B', 'F'}},
    {'B', {'C', 'D'}},
    {'C', {'E'}},
    {'D', {}},
    {'E', {}},
    {'F', {}}
};
unordered_map<char, bool> visitedNodes = {
    {'A', false},
    {'B', false},
    {'C', false},
    {'D', false},
    {'E', false},
    {'F', false}
};

void dfs(char node){
    auto isVisited = visitedNodes.find(node);
    if(isVisited == visitedNodes.end()){
        cout<<"Bad Node"<<endl;
        return;
    }
    else if(isVisited->second) return;
    
    cout<<node<<"->";
    auto neighbours = graph.find(node)->second;
    for(auto &neighbour: neighbours){
        dfs(neighbour);
    }
}

int main() 
{
    char start_node = 'A';
    dfs(start_node);
    cout<<"END";
}