class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else lists

    def merge2Lists(self, l1, l2):
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l1
                l1 = point.next.next
            point = point.next
        if not l1:
            point.next=l2
        else:
            point.next=l1
        return head.next


sol=Solution()

node1=ListNode(1)
node11=ListNode(4)
node1.next=node11
node12=ListNode(5)
node11.next=node12
node2=ListNode(1)

node21=ListNode(3)
node2.next=node21
node22=ListNode(4)
node21.next=node22
node3=ListNode(2)
node31=ListNode(6)
node3.next=node31

nodelast=sol.mergeKLists([node1,node2,node3])
while True:
    if nodelast:
        print(nodelast.val)
        nodelast=nodelast.next
    else:
        break
