from enum import Enum

class Category(Enum):
    TOOLS = 'tools'
    CONSUMABLES = 'consumables'

print(Category.TOOLS)
print(Category.CONSUMABLES)
