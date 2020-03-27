import time

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        new = BinarySearchTree(value)
        if not self.value:
            return new
        if value < self.value:
            if not self.left:
                self.left = new
            else:
                # recursion (do same thing with that left node)
                self.left.insert(value)
        else:
            if not self.right:
                self.right = new
            else:
                # recursion (do same thing with that right node)
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        if not self.value:
            return False
        if target == self.value:
            return True
        else:
            if target < self.value:
                if not self.left:
                    return False
                else:
                    return self.left.contains(target)
            else:
                if not self.right:
                    return False
                else:
                    return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if not self.value:
            return None
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        if not self.value:
            return
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)


start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()


# iterate through first names file, adding each name to a tree
# then iterate through second names file, and using the contains method of the bst
# if it finds the same name in the file as it has in the tree
# add/append that name to the duplicates array

duplicates = []  # Return the list of duplicates in this data structure

tree = BinarySearchTree('middle alphabet')

for i in names_1:
    tree.insert(i)

for j in names_2:
    if tree.contains(j):
        duplicates.append(j)


# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
