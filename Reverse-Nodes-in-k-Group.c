/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

typedef struct ListNode Node;
Node * reverse(Node * head, int k)
{
    Node * prev = NULL, *nextNode = NULL, *curr = head;
    while(k > 0)
    {
        nextNode = curr -> next;
        curr -> next = prev;
        prev = curr;
        curr = nextNode;
        k--;
    }
    return prev;
}

struct ListNode* reverseKGroup(struct ListNode* head, int k) {
    int count = 0;
    Node * ptr = head, *newFinalHead = NULL;
    Node * ktail = NULL;
    Node * revHead = NULL;
    while (ptr != NULL)
    {
        while (count < k && ptr != NULL)
        {
            ptr = ptr -> next;
            count++;
        }
        if (count == k)
        {
            revHead = reverse(head, k);
            if (newFinalHead == NULL) newFinalHead = revHead;
            if (ktail != NULL) ktail -> next = revHead;
            ktail = head;
            head = ptr;
            count = 0;
        }
    }
    ktail -> next = head;
    return newFinalHead;
}