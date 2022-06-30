
# Sorting

1. Cyclic Sort: Cyclic Sort is Applicable when number are in Range 1 to N. Here, sorting is done based on conept that, each index holds vaue equal to index.
2. Here, if negative numbers or numbers greater than the length of array are present then simply ignore them, remaning numbers will be definitely on it's right place
```
Example: a = [3, 4, -1, 1]
         after sorting a = [1, -1, 3, 4], here 1, 3, and 4 are at proper places rest ignore
```
```py
def cyclic_sort(arr):
    present_index = 0
    while present_index < len(arr):
        correct_index_for_value_at_present_index = arr[present_index] -1
        
        if arr[present_index] == arr[correct_index_for_value_at_present_index]:
            present_index += 1
        else:
            temp = arr[present_index]
            arr[present_index] = arr[correct_index_for_value_at_present_index]
            arr[correct_index_for_value_at_present_index] = temp

arr = [3,5,2,1,4,7,6,-1,-4,23]
cyclic_sort(arr)
print(arr)
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
         
## Selection Sort
The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.
1) The subarray which is already sorted. 
2) Remaining subarray which is unsorted.
         
<img src = "https://user-images.githubusercontent.com/63506466/151711961-76b66202-81bb-4de2-9e65-31265c1f41f6.png" width="600">

## Merge Sort Algo
         
* The elements are split into two sub-arrays (n/2) again and again until only one element is left.
* Merge sort uses additional storage for sorting the auxiliary array.
* Merge sort uses three arrays where two are used for storing each half, and the third external one is used to store the final sorted list by merging the other two and each array is then sorted recursively.
* At last, all sub-arrays are merged to make it ‘n’ element size of the array.
         
 <img src = "https://user-images.githubusercontent.com/63506466/155659960-bdebe093-617a-4d6b-bc13-fd9b81fdb227.png" width="600">

         
## Quick Sort

Here we a pivot element and our JOB is to place Pivot element at it's right position. After doing this we divide our array into two halfs and then we make recursive calls for each halfs to sort them seperately as Pivot is already at right place

Now To bring Pivot at right place we simply traverse array from both start and end and swap when we get any element which violtes the rule i.e an element is smaller but is present to right of pivot, this should be sent to left and vice versa.
         
 <img src = "https://user-images.githubusercontent.com/63506466/155757103-8aae8b59-fb9b-4758-90f9-1857b3bfae44.png" width="600">
        
## Comparing the Sorting Algorithms
<table><thead><tr><th><strong>Algorithm</strong></th><th colspan="3"><strong>Time Complexity</strong></th><th>&nbsp;</th></tr><tr><th>&nbsp;</th><th>&nbsp; <strong>Best</strong></th><th><strong>Average</strong></th><th><strong>Worst</strong></th><th>&nbsp;</th></tr></thead><tbody><tr><td><a target="_blank" rel="noopener noreferrer nofollow" href="http://geeksquiz.com/selection-sort/">Selection Sort</a></td><td>Ω(n^2)</td><td>θ(n^2)</td><td>O(n^2)</td><td>&nbsp;</td></tr><tr><td><a target="_blank" rel="noopener noreferrer nofollow" href="http://geeksquiz.com/bubble-sort/">Bubble Sort</a></td><td>Ω(n)</td><td>θ(n^2)</td><td>O(n^2)</td><td>&nbsp;</td></tr><tr><td><a target="_blank" rel="noopener noreferrer nofollow" href="http://geeksquiz.com/insertion-sort/">Insertion Sort</a></td><td>Ω(n)</td><td>θ(n^2)</td><td>O(n^2)</td><td>&nbsp;</td></tr><tr><td><a target="_blank" rel="noopener noreferrer nofollow" href="http://geeksquiz.com/heap-sort/">Heap Sort</a></td><td>Ω(n log(n))</td><td>θ(n log(n))</td><td>O(n log(n))</td><td>&nbsp;</td></tr><tr><td><a target="_blank" rel="noopener noreferrer nofollow" href="http://geeksquiz.com/quick-sort/">Quick Sort</a></td><td>Ω(n log(n))</td><td>θ(n log(n))</td><td>O(n^2)</td><td>&nbsp;</td></tr><tr><td><a target="_blank" rel="noopener noreferrer nofollow" href="http://geeksquiz.com/merge-sort/">Merge Sort</a></td><td>Ω(n log(n))</td><td>θ(n log(n))</td><td>O(n log(n))</td><td>&nbsp;</td></tr><tr><td><a href="https://www.geeksforgeeks.org/bucket-sort-2/">Bucket Sort</a></td><td>Ω(n+k)</td><td>θ(n+k)</td><td>O(n^2)</td><td>&nbsp;</td></tr><tr><td><a href="https://www.geeksforgeeks.org/radix-sort/">Radix Sort</a></td><td>Ω(nk)</td><td>θ(nk)</td><td>O(nk)</td><td>&nbsp;</td></tr><tr><td>Count Sort</td><td>Ω(n+k)</td><td>θ(n+k)</td><td>O(n+k)</td><td>&nbsp;</td></tr></tbody></table>
         
## **Binary Search**
1. Pattern:-> 
```
a) Sorted Array is given
b) Predicate Function viz. Upto n'th index sab kuch true and then sab false aisa kuch.
   Here, we can use binary search to find the first occurance                                      
   Eg:https://leetcode.com/problems/first-bad-version
```
2. Code
```py
def binary_search(arr, target):
    s = 0
    e = len(arr)-1
    while(s <= e):
        mid = s + (e-s)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            s = mid + 1
        else:
            e = mid - 1
    return -1

arr = [1,2,5,7,8,10]
idx = binary_search(arr, 10)
print(idx)

```

3. Binary Search in Rotated Sorted Array

https://leetcode.com/problems/search-in-rotated-sorted-array/

![Binary Search in Sorted Rotated Array](https://user-images.githubusercontent.com/63506466/176592626-3615af8c-2eb5-4d04-a667-c3599b29a3dc.png)

  
         
