# Definition for a binary tree node.
# class TreeNode
#     def __init__(self, x)
#         self.val = x
#         self.left = None
#         self.right = None

class Solution
    def buildTree(self, preorder List[int], inorder List[int]) - TreeNode
        # 验证输入数据有效性
        if(len(preorder)!=len(inorder))
            print(Invalid testcase.);

        # 构建哈希，遍历一次inorder,建立数字与下标的映射，便于快速定位inorder里的根节点
        index = {element i for i, element in enumerate(inorder)}

        def myTree(preorder_left int, preorder_right int, inorder_left int, inorder_right int)
            # 递归
            ## 递归 terminator
            if(preorder_left  preorder_right)
                return None

            ## 递归 CurrentLevelLogic
            ### 在前序中得到根节点数值，在中序遍历中定位root的下标
            preorder_root = preorder_left
            inorder_root = index[preorder[preorder_root]]
            ### 计算左子树中元素数量
            size_left_subtree=inorder_root-inorder_left
            ### 建立树的根节点
            root = TreeNode(preorder[preorder_root])
            ### 构建左右子树并连接到根节点
            root.left = myTree(preorder_left + 1, preorder_left + size_left_subtree, inorder_left, inorder_root - 1)
            root.right = myTree(preorder_left + size_left_subtree + 1, preorder_right, inorder_root + 1, inorder_right)
            return root

        # 返回构建树
        return myTree(0, len(preorder)-1, 0 , len(preorder)-1)