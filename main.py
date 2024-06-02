

from functions import Node, LinkedList

## Linked List yaratamiz
llist = LinkedList()

## Uchta node (tugun) yaratamiz
llist.head = Node('Monday')
tuesday = Node('Tuesday')
wednesday = Node('Wednesday')

## Tugunlarni bog'laymiz
llist.head.next = tuesday
tuesday.next = wednesday

## Linked Listni konsolga chiqaramiz:
llist.printList()
print("\n\n\n\n\n")

## List boshiga yangi tugun qo'shamiz
llist.push('Sunday')
llist.push('Monday')
# llist.printList()

## List o'rtasiga element qo'shamiz
# llist.insert(llist.head.next.next, 'Seshanba Kechasi')
# llist.printList()

## List oxiriga tugun qo'shamiz
llist.append('Thursday')
llist.append('Friday')
# llist.printList()

## Element o'chiramiz
llist.deleteNode('Tuesday')
llist.printList()