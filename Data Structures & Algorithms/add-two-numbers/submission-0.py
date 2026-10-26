# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1curr=l1
        l1list=[]
        while l1curr:
            l1list.append(str(l1curr.val))
            l1curr=l1curr.next
        l1str="".join(l1list[::-1])
        l1int=int(l1str)
        l2curr=l2
        l2list=[]
        while l2curr:
            l2list.append(str(l2curr.val))
            l2curr=l2curr.next
        l2str="".join(l2list[::-1])
        l2int=int(l2str)
        intans=l1int+l2int
        ansstr=str(intans)
        head=None
        for digit in ansstr:
           node=ListNode(int(digit))
           node.next=head
           head=node
        return head
        

