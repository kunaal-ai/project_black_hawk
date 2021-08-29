# Python program to interchange first and last elements in a list
# Jira Ticket: https://blackhawk.atlassian.net/browse/BLAC-2

class InterchangeElements:
    def interchange(self, list_of_elements):
        list_of_elements[0], list_of_elements[-1] = list_of_elements[-1], list_of_elements[0]
        return list_of_elements

ie_obj = InterchangeElements()
print(ie_obj.interchange([1,2,3,4,5,6,7,8,9,0]))