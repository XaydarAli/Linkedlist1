

from functions import Node, LinkedList

## Linked List yaratamiz
students = LinkedList()

## Uchta node (tugun) yaratamiz
students.head = Node('Alijon')
student1 = Node('Shamshod')
student2 = Node('Bobur')

## Tugunlarni bog'laymiz
students.head.next = student1
student1.next = student2

print("Students linked listning dastlabki holati.\n")
students.printList()

print("**********************************************************")
print("List boshiga yangi tugun qo'shganimizning holatlari.(Push)")
students.push('Alibek')
students.printList()
print("\n")
students.push('Tony')
students.printList()
print("\n")
students.push('Stark')
students.printList()
print("\n")
students.push('Jarvis')
students.printList()
print("\n")
students.push('Bruce')
students.printList()
print("************************************************")
print("Linked listda insertni qo'llaymiz endi.")
students.insert(students.head.next.next, 'Steve Rogers')
students.printList()
print("*******************************************")

print("List oxiriga tugun qo'shamiz")
students.append('Piter Parker')
students.printList()
print("\n")
students.append('Harry Potter')
students.printList()
print("*******************************")
print("Element o'chiramiz")
students.deleteNode('Alibek')
students.printList()