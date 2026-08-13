with open("notes.txt", "a") as files:
    files.write("\nI learned file handling.")

with open("notes.txt", "a") as files:
    files.write("\nAppend mode adds data")


with open("notes.txt", "a")  as files:
    files.write("\nPython is becoming easier")

with open("notes.txt", "r") as files:
    print(files.read())