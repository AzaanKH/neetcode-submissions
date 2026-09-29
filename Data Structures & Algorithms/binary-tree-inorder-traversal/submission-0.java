/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    private List<Integer> inOrderTree;
    
    public List<Integer> inorderTraversal(TreeNode root) {

        inOrderTree = new ArrayList<>();
        inOrder(root);
        return inOrderTree;
    }
    private void inOrder(TreeNode node) {
        if (node == null) {
            return;
        }
        inOrder(node.left);
        inOrderTree.add(node.val);
        inOrder(node.right);
    }     
}