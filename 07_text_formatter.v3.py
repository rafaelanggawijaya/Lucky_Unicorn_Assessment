"""Component 5 -Text formatter- v1
Can add decorations to text
Changed: Changed main routine for test
By Rafael Anggawijya"""


def text_formatter(symbol_1, side_symbol, symbol_2, text):
    sides = side_symbol * 3
    formatted_text = f"{sides}{text}{sides}"
    top = symbol_1 * len(formatted_text)
    bottom = symbol_2 * len(formatted_text)

    return f"{top}\n{formatted_text}\n{bottom}"

# Main routine


print(text_formatter("-", "-", "*", "Welcome to Lucky Unicorn The Game") + "\n")
print(text_formatter("!", "$", "!", "Congratulations You Got a Unicorn!") + "\n")
print(text_formatter("!", "D", "!", "Tough Luck You got a Donkey") + "\n")
print(text_formatter("z", "Z", "z", "You Got a Zebra") + "\n")
print(text_formatter("h", "H", "h", "You Got a Horse") + "\n")
print(text_formatter("*", "-", "-", "Goodbye") + "\n")
