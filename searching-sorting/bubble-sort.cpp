#include<bits/stdc++.h>
using namespace std; 

void bubble_sort(vector<int> &v){
    int n = v.size();
    for(int pass = 0; pass < n; pass++){
        bool swapped = false;
        for(int j = 1; j<(n-pass); j++){
            if(v[j-1] > v[j]){
                swap(v[j], v[j-1]);
                swapped = true;
            }
        }
    }
}

int main() 
{
    vector<int> v = {5,4,3,2,1};
    bubble_sort(v);
    for(auto &val: v) cout<<val<<" ";
    
}