"""Exercise 2.

Figure out which line of the above program is still not properly guarded.
See if you can construct a text file which causes the program to fail and then
modify the program so that the line is properly guarded and test it to make
sure it handles your new text file.
"""

# pylint: disable=R1732
file_handler = open("../Chapter 7. Files/mbox-short.txt", encoding="utf_8")
# pylint: enable=R1732
for line in file_handler:
    words = line.split()
    if len(words) <= 2:  # was 0
        continue
    if words[0] != "From":
        continue
    print(words[2])
