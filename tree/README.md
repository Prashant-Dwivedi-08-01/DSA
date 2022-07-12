## Tree Traversal
1. In-Order: Root in the order `( R-Root-L )`
2. Pre-Order: Root Before the Order `( Root-R-L )`
3. Post-Order: Root After the Order `( R-L-Root )`

## Time Complexity of Each Traversal
All the traversal methods have time complexity of `O(N)`

If we follow the recurrance realtion then `T(N) = 2*T(N/2) + O(1)`. Upon solving this we get `O(N)`. Also, logically we are tracing all the nodes in tree if the binary tree is skewed binary tree in worst case. Thus, in worst case we can think of O(N) time.
