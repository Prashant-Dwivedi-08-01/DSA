#include<bits/stdc++.h>
using namespace std; 

//* For the Questions with Pattern: 1 to N. This swapping used when numbers are in range.
//! Here, we have only O(n) time Complexity, as the number of Comparisions are 2*N - 1

void cyclic_sort(vector<int> &v){
    int present_index = 0;
    while(present_index < v.size()){
        int correct_index = v[present_index] - 1; //Correct Index of Number at i is (that number) - 1;
        if(v[present_index] != v[correct_index]){
            swap(v[present_index], v[correct_index]);
        }
        else{
            present_index++;
        }
    }
}

int main() 
{
    vector<int> v = {3,5,2,1,4};
    cyclic_sort(v);  
    for(int &value: v) cout<<value<<" "; 
}