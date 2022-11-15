items = ['hot dog', 'coffee', 'pizza', 'sandwich']

def add_item(name):
    items.append(name)

def remove_item(name):
    items.remove(name)

def edit_item(name, newName):
    index = items.index(name)
    items[index] = newName

def reverse_items():
    items.reverse()

add_item('shoke')
remove_item('coffee')
edit_item('hot dog', 'ice dog')
reverse_items()
print(items)