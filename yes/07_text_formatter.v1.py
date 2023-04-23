"""Component 5 -Text formatter- v1
Can add decorations to text
By Rafael Anggawijya"""

symbol_1 = "-"
text = "hello world"
sides = symbol_1 * 3
symobl_2 = "*"

formatted_text = f"{sides}{text}{sides}"
top = symbol_1 * len(formatted_text)
bottom = symobl_2 * len(formatted_text)

print(top)
print(formatted_text)
print(bottom)
