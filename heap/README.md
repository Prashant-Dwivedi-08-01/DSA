#Heap

### Min heap

A Min-Heap is a complete binary tree in which the value in each internal node is smaller than or equal to the values in the children of that node. 
Mapping the elements of a heap into an array is trivial: if a node is stored at index k, then its left child is stored at index 2k + 1 and its right child at index 2k + 2.

```
            5                      13
         /      \               /       \  
       10        15           16         31 
      /                      /  \        /  \
    30                     41    51    100   41
```

### Max heap
A Max-Heap is a complete binary tree in which the value in each internal node is greater than or equal to the values in the children of that node.
Mapping the elements of a heap into an array is trivial: if a node is stored a index k, then its left child is stored at index 2k + 1 and its right child at index 2k + 2.

![image](https://user-images.githubusercontent.com/63506466/150747552-035dc07c-bfe0-46dc-b1f0-5cb924de7d92.png)

For any position in array Arr[i]:
* Arr[(i-1)/2] Returns the parent node.
* Arr[(2*i)+1] Returns the left child node.
* Arr[(2*i)+2] Returns the right child node.

### Insert in Heap
![3  Heap ( Insertion )](https://user-images.githubusercontent.com/63506466/150747665-3fdca91a-dca4-48bb-afd7-7cb9cfd9848d.jpg)

* Insertion in heap takes O(log(n)) in worst case

### Delete in Heap
![4  Heap ( Deletion )](https://user-images.githubusercontent.com/63506466/150749758-3c98ec70-c2b9-44f5-9f1e-a09e0e68a9d9.jpg)
