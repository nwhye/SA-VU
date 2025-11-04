package LW6;
import com.scalified.tree.*;
import com.scalified.tree.multinode.*;

public class Main {
    public static void main(String[] args) {

        TreeNode<String> n1 = new ArrayMultiTreeNode<>("100");
        TreeNode<String> n2 = new ArrayMultiTreeNode<>("50");
        TreeNode<String> n3 = new ArrayMultiTreeNode<>("50");
        TreeNode<String> n4 = new ArrayMultiTreeNode<>("25");
        TreeNode<String> n5 = new ArrayMultiTreeNode<>("25");
        TreeNode<String> n6 = new ArrayMultiTreeNode<>("25");
        TreeNode<String> n7 = new ArrayMultiTreeNode<>("25");

        TreeNode<String> root = n1.root();

        n1.add(n2);
        n1.add(n3);
        n2.add(n4);
        n2.add(n5);
        n3.add(n6);
        n3.add(n7);

        for (TreeNode<String> node : root) {
            System.out.println(node.data());
        }
    }
}