/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        /*struct ListNode *th1 = headA;
        while (th1!=NULL)
        {
            struct ListNode *th2 = headB;
            while (th2 != NULL)
            {
                if (th1 == th2) return th1;
                th2 = th2 -> next;
            }
            th1 = th1 -> next;
        }
        return NULL; tc : O(n2) sc : O(1)*/

        unordered_set<ListNode*>s; //sc : O(n)
        while (headA != nullptr) //tc : O(n)
        {
            s.insert(headA);
            headA = headA -> next;
        }
        while (headB != nullptr) //tc: O(m)
        {
            if(s.count(headB) == 1)
                return headB;
            headB = headB -> next;
        }
        return nullptr; //tc: O(n + m) sc: O(n)

    }
};