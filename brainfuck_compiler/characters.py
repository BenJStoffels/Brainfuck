def remove_unused_characters(input_string):
    """Dit haalt alle tekens weg die geen tekens zijn die in een brainfuck programma horen."""
    return "".join(filter(lambda c: c in "<>+-.,[]", input_string))


def print_char(byte, print_ascii):
    print(chr(byte) if print_ascii else byte)


def handle_character(input_character, code_ptr, memory_ptr, memory, brace_map, ascii=False, **kwargs):
    """Wat er moet gebeuren bij elk character"""
    if input_character == "<":
        memory_ptr -= 1
    elif input_character == ">":
        memory_ptr += 1
    elif input_character == "+":
        try:
            memory[memory_ptr] += 1
        # als je in een bytearray (memory) een getal groter dan 255 probeert te zetten, komt er een error:
        except ValueError:
            # dat betekent dat je weer naar 0 moet gaan
            memory[memory_ptr] = 0
    elif input_character == "-":
        try:
            memory[memory_ptr] -= 1
        # zelfde met negatieve getallen.
        except ValueError:
            # dan moet je weer naar 255
            memory[memory_ptr] = 255
    elif input_character == ".":
        print_char(memory[memory_ptr], ascii)
    elif input_character == ",":
        inputString = input("input: ")
        # dit test of je input een getal is, zo kan je ook letterlijk de waarde ingeven, en hoef je niet alle ascii-codes te kennen.
        if inputString.isnumeric():
            memory[memory_ptr] = int(inputString) & 0b11111111
        else:
            # dit slaagt wel de ascii-code op als je geen getal hebt ingegeven
            memory[memory_ptr:memory_ptr +
                   len(inputString)] = bytes(inputString, "utf-8")
    elif input_character == "[":
            # je moet naar de bijhorende sluitende haak springen als je op nul staat
        if memory[memory_ptr] == 0:
            # die werd opgeslagen in de brace_map
            code_ptr = brace_map[code_ptr]
    elif input_character == "]":
        # als het niet nul is aan het einde van de loop, moet je terug naar het begin
        if memory[memory_ptr] != 0:
            # ook deze werd gewoon in de brace_map gezet
            code_ptr = brace_map[code_ptr]
    else:
        # Nomraal gezien gebeurt dit nooit, want we hebben de ongebruikte tekens al weggedaan,
        # maar je weet nooit wat voor vreemde errors je krijgt als je het vergeet te controleren
        print("something went horribbly wrong, I'm really sorry.")
    return code_ptr, memory_ptr, memory
