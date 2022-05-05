#!/usr/bin/python3


def new_node(num, head=None):

    if type(num) is not int:
        return None

    new_node = dict(next=None, number=num)

    if head is not None:
        node = head
        while node['next'] is not None:
            node = node['next']
        node['next'] = new_node
        node['next'] = dict(next=None, number=num)

    if head is None:
        head = new_node

    return head


""" Verde """


def delete(index, head=None):
    pass


""" Amarillo """


def delete_number(number, head=None):
    pass


""" Rojo """
def swap(index, head=None, up=True):
    
    if head is not None:
        node = head
        for i in range(index):
        	node = node['next']
    index += 1
    node['next'] = self.head


""" Azul """

def change_between_numbers(index_1, index_2, head=None):
    pass


""" Purpura """


def delete_all(head=None):
    pass


head = new_node(10)
new_node(11, head)
new_node(12, head)
new_node(13, head)
new_node(20, head)
swap(1)

print(head)