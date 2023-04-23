"""Component 5 -Text formatter- v1
Can add decorations to text
Update: changed code to a function
By Rafael Anggawijya"""


def text_formatter(symbol_1, side_symbol, symbol_2, text):
    sides = side_symbol * 3
    formatted_text = f"{sides}{text}{sides}"
    top = symbol_1 * len(formatted_text)
    bottom = symbol_2 * len(formatted_text)

    return f"{top}\n{formatted_text}\n{bottom}"


# Main routine

text1 = input("Enter statement you want to to format: ")
symbol1 = input("Enter the symbol you want to add: ")
symbol2 = input("Enter another symbol you want to add: ")
side_symbols = input("Enter a side symbol you want to add: ")
print(text_formatter(symbol1, side_symbols,symbol2, text1))
