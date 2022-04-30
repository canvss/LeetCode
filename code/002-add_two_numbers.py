# _*_ coding: utf-8 _*_
# created by Stephen•Liu on 2022/4/30 13:11

# Definition for singly-linked list.
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1 = []
        s2 = []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        li = []
        tmp = 0
        for i in range(len(s1) if len(s1)>len(s2) else len(s2)):
            try:
                t1 = s1[i]
            except:
                t1 = 0
            try:
                t2 = s2[i]
            except:
                t2 = 0
            sum = t1+t2
            if tmp:
                sum += tmp
            if sum >=10:
                sum -= 10
                tmp = 1
            else:
                tmp = 0
            li.append(sum)
        if tmp:
            li.append(tmp)
        tmp = None
        for i in range(len(li)-1, -1, -1):
            tmp = ListNode(li[i],tmp)
        return tmp


s4 = ListNode(4)
s3 = ListNode(3, s4)
s2 = ListNode(2, s3)

t4 = ListNode(6)
t3 = ListNode(7, t4)
t2 = ListNode(2, t3)

result = Solution().addTwoNumbers(s2,t2)
while result:
    print(result.val)
    result = result.next

