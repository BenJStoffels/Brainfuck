
def create_brace_map(input_string):
    """Dit maakt een dictionary, waarin opgeslagen wordt welke haakjes bij elkaar horen:
    bijvoorbeeld wanneer er een haakje open staat op plaats 10 en het gesloten haakje dat erbij hoort komt op plaats 20,
    dan is de brace_map {10: 20, 20: 10}. Dit wordt gedaan voor elk paar haakjes.
    """
    brace_map = {}
    current_braces = []

    for i, c in enumerate(input_string):
        if c == "[":
            current_braces.append(i)
        elif c == "]":
            begin_index = current_braces.pop()
            brace_map[begin_index] = i
            brace_map[i] = begin_index

    return brace_map


def get_input(path_to_file):
    """Dit leest de contents van een file, op de locatie path_to_file"""
    with open(path_to_file, "r") as file:
        inp = file.read()

    return inp


def get_hex_disp(byte):
    return "0x" + str(hex(byte))[2:].rjust(2, "0")


def print_memory(memory, disp_hex):
    for byte in memory:
        print(byte if not disp_hex else get_hex_disp(byte), end=" ")
