# Python program to copy or cloning a list
# Jira Ticket: https://blackhawk.atlassian.net/browse/BLAC-7

class CopyList:
    def copy_list_to_newone(self, user_list):
        new_list = user_list[:]
        print(new_list)
        print(user_list)



obj = CopyList()
obj.copy_list_to_newone([1,2,3,4,5,6])