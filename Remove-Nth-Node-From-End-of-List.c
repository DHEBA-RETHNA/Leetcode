/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    if (head -> next == NULL)
    {
        free(head);
        head = NULL;
        return head;
    }
    struct ListNode *end = head;
    while(n--) end = end -> next;
    if (end == NULL)
    {
        struct ListNode *temp = head;
        head = head -> next;
        free(temp);
        temp = NULL;
        return head;
    }
    struct ListNode *prev = NULL, *curr = head;
    while(end)
    {
        prev = curr;
        curr = curr -> next;
        end = end -> next;
    }
    prev -> next = curr -> next;
    free(curr);
    curr = NULL;
    return head;
}