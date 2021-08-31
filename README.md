# dsa-cheat-sheet

## **Heap**
1. Heap is Formed from Full Binary Tree i.e complete till level h-1 and then filled form left to right at level h
2. At any index i in array, it's child is 2*i and (2*i+1) and parent is floor(i/2).
3. Time taken to insert value in Heap in O(log(N)) i.e O(log(height of Tree)) and in worst case element may be leaf node i.e hight = log(n).
4. Priority Queue in C++ in example of heap.

## **Binary Tree**
1. If we need to showcase end of nodes then we can make a -1 node at the end of each leaf which would help in some questions, eg: Leet code Problem 100. Same Trees
<img src = "Tree.png">
Code for that is, this would give the vector with -1 for leaf nodes.
```
  void inOrder(TreeNode* root, vector<int> &v){
        if(root){
            inOrder(root->left,v);
            v.push_back(root->val);
            inOrder(root->right,v);
        }
        v.push_back(-1);
    }
```
