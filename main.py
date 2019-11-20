# ########################################### Importing Linked List#######################################
from linked_list import LinkedList

# ######################################### Object of linked list #########################################
link_list_object = LinkedList()

# ######################################## Inserting value in the list ####################################
link_list_object.insert_at_start(1)
link_list_object.insert_at_start(0)
link_list_object.insert_at_start(2)
link_list_object.insert_at_start(3)
link_list_object.insert_at_start(4)
link_list_object.insert_at_start(5)
link_list_object.insert_at_start(6)

# ####################################### Printing list before Deletion ###################################
print("Printing List Before DELETION:")
link_list_object.print_list()

# ######################################### Deleting some value ##########################################
link_list_object.delete_given_value(3)
link_list_object.delete_from_last()
link_list_object.delete_from_start()

# ########################################### Printing list after deletion ################################
print("Printing List After DELETION:")
link_list_object.print_list()

find = link_list_object.search_node(2)
if(find!= None):
    print("We recieve this node as a result of search "+str(find.data))