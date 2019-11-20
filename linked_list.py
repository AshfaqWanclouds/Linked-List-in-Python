# ####################  All the Link list functions define in this file ##############################


from node import Node


class LinkedList:
    def __init__(self):                 # Constructor
        self.head = None
        self.tail = None

    def insert_at_start(self, value):
        newnode = Node(value)
        if self.head is None:           # 1st value inserting in the link list when link list is empty
            self.head = newnode
            self.tail = newnode
        else:                           # when already have node but still want to add at start
            newnode.next = self.head
            self.head = newnode     # updating head pointer

    def insert_at_last(self, value):
        newnode = Node(value)
        if self.tail is None:           # If list is empty then value starting at start and last are the same
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.next = newnode
            self.tail = newnode     # updating tale pointer

    def delete_from_start(self):
        if self.head is not None:       # if tree is not empty
            curr_head = self.head
            self.head = curr_head.next
            print("Node deleted from Start having value = "+str(curr_head.data))
            del curr_head
        else:
            print("List is Empty")

    def delete_from_last(self):
        if self.head is not None:
            second_last_node = self.head
            while second_last_node.next != self.tail:       # finding 2nd last node
                second_last_node = second_last_node.next

            second_last_node.next = None
            print("Node deleted from last having value = "+str(self.tail.data))
            del self.tail
            self.tail = second_last_node            # updating tale pointer

    def search_node(self, value):
        curr = self.head
        if self.head is not None:               # if tree is not empty
            while curr is not None:         # finding value
                if curr.data == value:      # if found break the loop
                    break
                else:
                    curr = curr.next        # not found go to next
            if curr is None:            # iterate whole loop but not found
                print("Value not Found")
            else:                       # value found
                print("From Search_node Returning node having value = "+str(curr.data))
                return curr

    def delete_given_value(self, del_value):
        curr = self.head
        previous = curr
        if self.head is not None:       # if tree is not empty
            while curr is not None:
                if curr.data == del_value:      # if found the node having value which you want to delete
                    break
                else:
                    previous = curr         # previous and current move consectively
                    curr = curr.next
            if curr is None:            # if not found
                print("Value Not Found")
            else:               # found the node
                if curr == self.head:       # if the value match with the header node
                    print("You are trying to delete Start node so ", end=" ")
                    self.delete_from_start()
                elif curr == self.tail:     # if value matches with the tail node
                    print("You are trying to delete Last node so ", end=" ")
                    self.delete_from_last()
                else:                       # value in between the head and tail
                    previous.next = curr.next
                    print("Node deleted having data = "+str(curr.data))
                    del curr

    def print_list(self):
        curr = self.head            # starting from head
        if self.head is not None:
            while curr is not None:     # iterate whole list
                print("      "+str(curr.data), end="    ")      # print
                curr = curr.next        # and move to next
            print("\n")
        else:       # if list is empty
            print("List is empty")
