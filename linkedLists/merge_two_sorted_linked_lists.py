# 21. Merge Two Sorted Lists
def merge_sorted_linked_lists(l1, l2):
    if l1 == None: return l2
    if l2 == None: return l1
    
    if l1.val < l2.val:
        new_list = l1
        l1 = l1.next
    else:
        new_list = l2
        l2 = l2.next
    temp = new_list
    
    while l1 and l2:
        if l1.val < l2.val:
            temp.next = l1
            l1 = l1.next
        else:
            temp.next = l2
            l2 = l2.next
        temp = temp.next
    if l1:
        temp.next = l1
    if l2:
        temp.next = l2
    return new_list