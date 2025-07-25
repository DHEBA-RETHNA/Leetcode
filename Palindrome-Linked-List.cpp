/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    bool isPalindrome(ListNode* head) {
      stack<int>s;
      ListNode*th = head;
      while (th != nullptr)
      {
        s.push(th -> val);
        th = th -> next;
      }  
      th = head;
      while (th != nullptr)
      {
        if (th -> val != s.top()) return false;
        s.pop();
        th = th -> next;
      }
      return true;
    }
};