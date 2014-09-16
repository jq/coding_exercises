/* PROBLEM STATEMENT:

   The lowest common ancestor (LCA) of two nodes is the deepest node
   common to the lineage of both nodes. For example, in this tree...

   R
   / \
   /   \ 
   A     B
   / \     \
   X    Y     Z
   C  D  L M   G  H


   ... the LCA of nodes A and B is the root R.
   ... the LCA of nodes X and Y is the node A.
   ... the LCA of nodes A and Z is the root R.

   Please implement a method that returns the lowest common ancestor
   of two nodes given.

   You may not assume any organization for the tree, i.e. the tree 
   is _not_ a BST. However, the nodes do have a parent reference.

*/

import java.util.*;


public class LowestCommonAncestor {
   public static class Node {
      int val;
      Node left;
      Node right;
      Node parent;
      public Node(Node parent, int val) {
         this.parent = parent;
         this.val = val;
      }
   }


   public Node lowestCommonAncestor(Node foo, Node bar) {
      Set<Node> visited = new HashSet<>();
      return lowestCommonAncestor(foo, bar, visited);
   }

   public Node lowestCommonAncestor(Node foo, Node bar, Set<Node> visited) {
      if (foo == null || bar == null) {
         throw new IllegalArgumentException("foo/bar is required");
      }
      if (foo.parent == bar.parent) {
         return foo.parent;
      }

      if (isChild(foo.parent, bar, visited)) {
         return foo.parent;
      }

      return lowestCommonAncestor(foo.parent, bar);
   }

   private boolean isChild(Node parent, Node child, Set<Node> visited) {
      if (child == null) {
         return false;
      }
      if (visited.contains(parent)) {
         return false;
      }
      if (parent.left == child || parent.right == child) {
         return true;
      }
      if (parent.left != null) {
         if (isChild(parent.left, child, visited)) {
            return true;
         }
      }
      if (parent.right != null) {
         if (isChild(parent.right, child, visited)) {
            return true;
         }
      }
      visited.add(parent);
      return false;
   }

}
