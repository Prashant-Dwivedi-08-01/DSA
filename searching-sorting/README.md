
# Sorting

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

## **Bubble Sort** 
Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.

Unoptimized: We do N passes irrespecitive of fact that array may be sorted even before N pass. 
Optimized: We do only required number of passes + 1 pass where we mesure if any swap is being done or not. If no swap then we do not go any furthur

**Time:** O(n<sup>2</sup>) in worst case where array is in rever order of sorting
<img src = "https://user-images.githubusercontent.com/63506466/151709588-c922c97b-b2a4-4b5a-a2ca-7ecf2daef4ed.png" width="600">

## **Insertion Sort**
The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed at the correct position in the sorted part.
Simple Logic: One half of array(left half) is sorted and we need to pick one element from right and "INSERT" 
it in left half at proper location.

**Time**: O(n<sup>2<sup>)
   
<img src = "https://user-images.githubusercontent.com/63506466/151711435-3ef870f6-87d5-48ec-8d1d-249e39049cd1.png" width="600">
         
## **Selection Sort**
The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.
1) The subarray which is already sorted. 
2) Remaining subarray which is unsorted.
         
<img src = "https://user-images.githubusercontent.com/63506466/151711961-76b66202-81bb-4de2-9e65-31265c1f41f6.png" width="600">


         
         
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
