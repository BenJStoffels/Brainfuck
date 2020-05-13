import sys


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


def print_memory(memory):
    for byte in memory:
        print(byte, end=" ")


def remove_unused_characters(input_string):
    """Dit haalt alle tekens weg die geen tekens zijn die in een brainfuck programma horen."""
    return "".join(filter(lambda c: c in "<>+-.,[]", input_string))


def main():
    # Dit zorgt ervoor dat je een text-bestand hebt ingegeven
    if not len(sys.argv) > 1:
        raise EnvironmentError(
            "Please enter the file with your Brainfuck code!")

    inp = get_input(sys.argv[1])
    inp = remove_unused_characters(inp)

    brace_map = create_brace_map(inp)

    # memory_ptr houd bij waar in de memory je zit.
    memory_ptr = 0
    # code_ptr houd bij waar in de code je zit.
    code_ptr = 0
    # dit is de memory
    memory = bytearray(30)

    # main loop: voor elk teken in de input_string
    while code_ptr < len(inp):
        current_char = inp[code_ptr]
        if current_char == "<":
            memory_ptr -= 1
        elif current_char == ">":
            memory_ptr += 1
        elif current_char == "+":
            try:
                memory[memory_ptr] += 1
            # als je in een bytearray (memory) een getal groter dan 255 probeert te zetten, komt er een error:
            except ValueError:
                # dat betekent dat je weer naar 0 moet gaan
                memory[memory_ptr] = 0
        elif current_char == "-":
            try:
                memory[memory_ptr] -= 1
            # zelfde met negatieve getallen.
            except ValueError:
                # dan moet je weer naar 255
                memory[memory_ptr] = 255
        elif current_char == ".":
            print(chr(memory[memory_ptr]), end="")
        elif current_char == ",":
            inputString = input("input: ")
            # dit test of je input een getal is, zo kan je ook letterlijk de waarde ingeven, en hoef je niet alle ascii-codes te kennen.
            if inputString.isnumeric():
                memory[memory_ptr] = int(inputString) & 0b11111111
            else:
                # dit slaagt wel de ascii-code op als je geen getal hebt ingegeven
                memory[memory_ptr:memory_ptr +
                       len(inputString)] = bytes(inputString, "utf-8")
        elif current_char == "[":
            # je moet naar de bijhorende sluitende haak springen als je op nul staat
            if memory[memory_ptr] == 0:
                # die werd opgeslagen in de brace_map
                code_ptr = brace_map[code_ptr]
        elif current_char == "]":
            # als het niet nul is aan het einde van de loop, moet je terug naar het begin
            if memory[memory_ptr] != 0:
                # ook deze werd gewoon in de brace_map gezet
                code_ptr = brace_map[code_ptr]
        else:
            # Nomraal gezien gebeurt dit nooit, want we hebben de ongebruikte tekens al weggedaan,
            # maar je weet nooit wat voor vreemde errors je krijgt als je het vergeet te controleren
            print("something went horribbly wrong, I'm really sorry.")

        # volgende teken (ik denk dat dit voorzich spreekt, maar toch voor de zekerheid)
        code_ptr += 1

    print()
    # hier zie je enkel de bytes in hexadecimaal, ik ga dit nog veranderen.
    print_memory(memory)


# wanneer je dit bestand runt, zorg dat je een text-bestand meegeeft.
if __name__ == "__main__":
    main()
