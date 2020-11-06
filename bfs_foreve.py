# 545 Boundary of binary tree.


# Definition for a binary tree node.
import math
from queue import deque
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        queue = deque()
        leftOrRight = deque()
        queue.append(root)
        leftOrRight.append(0)
        answer = []
        ansFlag = deque()
        while queue:
            length = len(queue)
            temp = []
            for i in range(length):
                this = queue.popleft()
                thisLR = leftOrRight.popleft()
                temp.append(this.val)
                if length == 1:
                    ansFlag.append(thisLR)
                if this.left is not None:
                    queue.append(this.left)
                    leftOrRight.append(1)
                if this.right is not None:
                    queue.append(this.right)
                    leftOrRight.append(2)
            answer.append(temp)
        print(leftOrRight)
        print(queue)
        print(ansFlag)
        lastLine = answer[-1]

        left = []
        right = []
        for line in answer[:-1]:
            if len(line) == 1:
                flag = ansFlag.popleft()
                if flag == 0 or flag == 1:
                    left.append(line[0])
                else:
                    right.append(line[0])
            else:
                left.append(line[0])
                right.append(line[-1])
        print(left, right)
        return (left + lastLine + right[::-1])
