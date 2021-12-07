# make loop until input is /end
text = ""
finalText = ""
all_inputs = []
while text != '/end':
    text = input("Add text: ")
    if text != '/end':
        all_inputs.append(text)

for t in all_inputs:
    finalText = finalText + ' ' + t

print(" ".join(all_inputs))
# print every input after /end
