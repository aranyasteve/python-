"""
File type 
1 > Plain text
2 > Binary File
Mode of plain text
w, w+
r, r+
a, a+
Mode of binary file
wb, wb+
rb, rb+
ab, ab+
"""
file = open('abc1.txt', 'r+')
# file.seek(0, 0)you cannot go to the top even of you use the seek mode
file.write("Aranya\n")
file.seek(0, 0)

print(file.read())
file.close()
