print("Enter the String: ")
text = input()

print("Enter a Word to Delete: ")
word = input()

text = text.replace(word, "")

print()
print(text)