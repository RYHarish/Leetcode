/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {

    private ListNode removeZeros(ListNode h){
        ListNode c = h;
        while(c.next.next != null){
            c = c.next;
        }
        if(c.next.val == 0){
            c.next = null;
        }
        return h;
    }

    private int length(ListNode h){
            int count = 0;
            ListNode c = h;
            while(c != null){
                c = c.next;
                count++;
            }
            return count;
        }

    private ListNode sum(ListNode l1, ListNode l2){
        int carr = 0;
        ListNode temp = new ListNode(0, null);
        ListNode ans = temp;
        while(l2 != null){
            int x = l1.val + l2.val;
            if(x + carr >= 10 ){
                temp.val = x - 10 + carr;
                carr = 1;
            }
            else{
                temp.val = x + carr;
                carr = 0;
            }
            temp.next = new ListNode(carr, null);
            temp = temp.next;
            l1 = l1.next;
            l2 = l2.next;
        }
        return ans;
    }

    private ListNode pad(ListNode l, int diff){

        ListNode temp = l;
        while(temp.next != null){
            temp = temp.next;
        }
        while(diff>0){
            temp.next = new ListNode(0, null);
            diff--;
            temp = temp.next;
        }
        return l;
    }

    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int len_l1 = length(l1);
        int len_l2 = length(l2);
        int diff = 0;
        if(len_l1 > len_l2){
            diff = len_l1 - len_l2;
            l2 = pad(l2, diff);
            return removeZeros(sum(l1, l2));
        }
        else{
            diff = len_l2 - len_l1;
            l1 = pad(l1, diff);
            return removeZeros(sum(l2,l1));
        }
    }
}