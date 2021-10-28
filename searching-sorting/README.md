## **Binary Search**
1. Pattern:-> 
```
a) Sorted Array is given
b) Predicate Function viz. Upto n'th index sab kuch true and then sab false aisa kuch.
   Here, we can use binary search to find the first occurance                                      
   Eg:https://leetcode.com/problems/first-bad-version
```
2. Code
```cpp
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
        if (arr[mid] < target)
            s = mid + 1;
        else if (arr[mid] > target)
            e = mid - 1;

    }
    return -1;
}
```

## **Sorting**
1. Cyclic Sort: Cyclic Sort is Applicable when number are in Range 1 to N. Here, sorting is done based on conept that, each index holds vaue equal to index.
2. Here, if negative numbers or numbers greater than the length of array are present then simply ignore them, remaning numbers will be definitely on it's right place
```
Example: a = [3, 4, -1, 1]
         after sorting a = [1, -1, 3, 4], here 1, 3, and 4 are at proper places rest ignore
```
```cpp
void cyclic_sort(vector<int> &v){
    int present_index = 0;
    while(present_index < v.size()){
        int correct_index = v[present_index] - 1; //Here Correct Index  if basically, we are sayinbg that what is the correct index for the number at i. Correct Index of Number at i is (that number) - 1;
        if(v[present_index] != v[correct_index]){
            swap(v[present_index], v[correct_index]);
        }
        else{
            present_index++;
        }
    }
}

```