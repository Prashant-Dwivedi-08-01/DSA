#include<bits/stdc++.h>
using namespace std; 
//? Simple Logic: One half of array(left half) is sorted and we need to pick one element from right and "INSERT" 
//? it in left half at proper location.

void insertion_sort(vector<int> &v){
    int n = v.size();
    for(int i = 0; i<(n-1); i++){
        for (int j = i+1; j > 0; j--)
        {
            if(v[j] < v[j-1]) swap(v[j], v[j-1]);
            else break; // as the all the elements from here to the left of v[j-1] are already in sorted order
        }
    }
}

int main() 
{
    vector<int> v  {3,5,-1,6,-8, 0};
    insertion_sort(v);
    for(int &i: v) cout<<i<<" ";
}