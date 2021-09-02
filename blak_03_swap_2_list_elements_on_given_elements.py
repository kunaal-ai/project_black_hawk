# Python program to swap two elements in a list on given positions
# Kira Ticket: https://blackhawk.atlassian.net/browse/BLAC-3

class SwapTwoElements:

    def swap_elemtns_on_given_positions(self, pos_1, pos_2, lista):
        lista[pos_1],  lista[pos_2] = lista[pos_2], lista[pos_1]
        print(lista)

obj = SwapTwoElements()
obj.swap_elemtns_on_given_positions(1,2,['a','b','c','d'])