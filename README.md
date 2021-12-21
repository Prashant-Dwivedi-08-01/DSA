## dsa-cheat-sheet - Missc

## **Heap**
1. Heap is Formed from Full Binary Tree i.e complete till level h-1 and then filled form left to right at level h
2. At any index i in array, it's child is 2*i and (2*i+1) and parent is floor(i/2).
3. Time taken to insert value in Heap in O(log(N)) i.e O(log(height of Tree)) and in worst case element may be leaf node i.e hight = log(n).
4. Priority Queue in C++ in example of heap.

## **Binary Tree**
1. If we need to showcase end of nodes then we can make a -1 node at the end of each leaf which would help in some questions,https://leetcode.com/problems/same-tree/
<img src = "Tree.jpg" width=500>

Code for that is, this would give the vector with -1 for leaf nodes.
```cpp
  void inOrder(TreeNode* root, vector<int> &v){
        if(root){
            inOrder(root->left,v);
            v.push_back(root->val);
            inOrder(root->right,v);
        }
        v.push_back(-1);
    }
```
One More Better way to traverse the two trees is.
Here we traverse both the trees together, first Right Subtree in both trees and then left subtree in both the trees.
```cpp
  bool isSameTree(struct TreeNode* p, struct TreeNode* q){
    if(!p && !q) return true;
    if((!p && q) || (p && !q)) return false;
    return (p->val && q->val) && isSameTree(p->left,q->left) && isSameTree(p->right,q->right); 
}

```
One Similar Problem is Symmetric tree: https://leetcode.com/problems/symmetric-tree/

2. Returning from Traversal Methods

 <img src="https://user-images.githubusercontent.com/63506466/146869295-f04597cf-214e-4349-b5f3-60ba09dac71d.png" width=500 >


```py
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        presentDepth = 1
        maxDepth = 0
        return self.inOrder(root, presentDepth, maxDepth)
    
    def inOrder(self, root, presentDepth, maxDepth):
        if(root):
            maxDepth = self.inOrder(root.left, presentDepth+1,maxDepth)
            if(presentDepth > maxDepth):
                maxDepth = presentDepth
            maxDepth = self.inOrder(root.right, presentDepth+1,maxDepth)
        return maxDepth
        
```


