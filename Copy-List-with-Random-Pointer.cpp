/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
    /*unordered_map<Node *, Node *>m;
    Node *th = head;
    while (th != nullptr)
    {
        m[th] = new Node(th -> val);
        th = th -> next;
    }
    th = head;
    while (th != nullptr)
    {
        m[th] -> next = m[th -> next];
        m[th] -> random = m[th -> random];
        th = th -> next;
    }
    return m[head]; // tc:O(N) sc:O(N)*/

    if(head == nullptr) return nullptr;
    Node * th = head;
    while (th != nullptr)
    {
        Node *nn = new Node(th -> val);
        nn -> next = th -> next;
        th -> next = nn;
        th = nn -> next;
    }
    th = head;
    while (th != nullptr)
    {
        th -> next -> random = th -> random ? th -> random -> next : nullptr;
        th = th -> next -> next;
    }
    Node *res = head -> next;
    Node *th1 = head, *th2 = head -> next;
    while (th1 != nullptr)
    {
        th1 -> next = th2 -> next;
        th2 -> next = th1 -> next ? th1 -> next -> next : nullptr;
        th1 = th1 -> next;
        th2 = th2 -> next;
    }
    return res;
    }
};