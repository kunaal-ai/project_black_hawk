# Python program to reverse a list items
# Jira Ticket: https://blackhawk.atlassian.net/browse/BLAC-6

class ReverseListItems:

    def reverse_list_original_items(self, user_list):
        # This method will change actual values order in the list, we will loose the actual order
        print(f"original list {user_list} ")
        user_list.reverse()
        print(f"Using reverse method complete changed the original list {user_list}")
        print(f"Orignal list is changed {user_list}")

    def reverse_list_but_not_original(self, user_list):
        # will not change the actual order of list items, create a new list. consumes more memory
        print(f"Orignal list {user_list}")
        new_list = user_list[::-1]
        print(f"Reversed saving as a new list {new_list}")
        print(f"Orignal still as it is {user_list}")

obj=ReverseListItems()
obj.reverse_list_original_items(['A','B','C','D'])
obj.reverse_list_but_not_original([1,2,3,4,5])