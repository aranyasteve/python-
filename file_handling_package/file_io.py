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
file = open('abc.txt', 'w+')
name = ['Aranya\n', 'Ram\n', 'Arvind']
file.writelines(name)
# print(file.tell())
file.seek(0, 0)
# print(file.tell())
print(file.readline())
print(file.readlines())
# print(data)
file.close()
