# Python program to swap two elements with each other using replace function
# Jira Ticket: https://blackhawk.atlassian.net/browse/BLAC-4

class SwapWithEachother:

    def swap_two_elements(self, user_list, element_a, element_b):
        list_as_a_string = ", ".join(user_list)
        replaced_and_new_list = list_as_a_string.replace(element_a, ".").replace(element_b,element_a).replace(".",element_b).split(', ')
        print(user_list)
        print(replaced_and_new_list)

obj = SwapWithEachother()
obj.swap_two_elements( ['Good', 'This', 'best', 'for', 'Leet','Test'], 'e','G')
