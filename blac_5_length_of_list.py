# Python program to find length of list
# Jira Ticket: https://blackhawk.atlassian.net/browse/BLAC-5

class ListOperations:
    def find_list_length(self, user_list):
        print(len(user_list))


obj = ListOperations()
obj.find_list_length(['This','is','new','project'])
