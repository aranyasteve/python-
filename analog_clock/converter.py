a = int(input("Hello, How many lines you wish to write? "))
l = []
for i in range(a):
    i = i+1
    b = input(f"Enter what you wish to write in line number {i}")
    l.append(b+"\n")

print(l)
b = open("text.txt", "w")
b.writelines(l)
# b.write(f"{b[j]}\n")

print("Your request is done")
b.close()




