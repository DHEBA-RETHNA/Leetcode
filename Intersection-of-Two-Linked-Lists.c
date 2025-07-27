/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

/*typedef struct ListNode node;
int length(node *head)
{
    int count = 0;
    while (head != NULL)
    {
        ++count;
        head = head -> next;
    }
    return count;
}*/

struct ListNode *getIntersectionNode(struct ListNode *headA, struct ListNode *headB) {
    /*int l1 = length(headA);// O(n)
    int l2 = length(headB);// O(n)
    while (l1 > l2)
    {
        headA = headA -> next;
        l1--;
    }
    while (l2 > l1)
    {
        headB = headB -> next;
        l2--;
    }
    while (headA != headB)
    {
        headA = headA -> next;
        headB = headB -> next;
    }
    return headA;//tc : O(n + m) sc : O(1)*/

    struct ListNode *th1 = headA, *th2 = headB;
    while (th1 != th2)
    {
        th1 = th1 == NULL ? headB : th1 -> next;
        th2 = th2 == NULL ? headA : th2 -> next;
    }
    return th1; //O(n)
}