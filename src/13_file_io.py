"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
# https://www.geeksforgeeks.org/reading-writing-text-files-python/

file1 = open('foo.txt', 'r')
print(file1.readlines())
file1.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
file2 = open('bar.txt', 'w')
L = ["I play Minecraft \n", "I play Dota 2 \n", "I play CS:GO \n"]
file2.writelines(L)
file2.close()

