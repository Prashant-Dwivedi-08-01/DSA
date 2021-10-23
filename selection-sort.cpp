#include <bits/stdc++.h>
using namespace std;

//? slect the N'th position from last and then find the max from start to N'th position,
//? and then swap that max with N'th Position elelemt. Keep doing this till we reach to end
//? O(N) each time for Max element and O(N) times for each N elements, thus O(N^2)

int maxIndex(vector<int> &v, int start, int last){
    int n = v.size();
    int max = start;
    for(int i = start; i <= last; i++){
        if(v[i] > v[max]) max = i;
    }
    return max;
}

void selection_sort(vector<int> &v){
    int n = v.size();
    for(int i = 0; i <n; i++){
        int last = n - i - 1;
        int max = maxIndex(v, 0, last);
        swap(v[last], v[max]);
    }
}

int main()
{
    vector<int> v = {6, 44, 3, 2, 100};
    // cout<<maxIndex(v, 0, 4);
    selection_sort(v);
    for (auto &val : v)
        cout << val << " ";
}