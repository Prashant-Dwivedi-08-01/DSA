#include <bits/stdc++.h>
using namespace std;

int binarySearch(vector<int> arr, int target)
{
    int s = 0;
    int e = arr.size() - 1;
    bool isAsc = (arr[0] < arr[arr.size() - 1]);
    while (s <= e)
    {
        int mid = s + (e - s) / 2;
        if (arr[mid] == target)
            return mid;
        if (isAsc)
        {
            if (arr[mid] < target)
                s = mid + 1;
            else if (arr[mid] > target)
                e = mid - 1;
        }
        else
        {

            if (arr[mid] > target)
                s = mid + 1;
            else if (arr[mid] < target)
                e = mid - 1;
        }
    }
    return -1;
}

int main()
{
    vector<int> arr = {5,7,7,8,8,10};
    cout << binarySearch(arr, 8);
}
