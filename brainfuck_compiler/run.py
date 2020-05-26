from brainfuck_compiler.utils import create_brace_map
from brainfuck_compiler.characters import handle_character
from brainfuck_compiler.characters import remove_unused_characters


def run_inp(inp, length=30, **config):
    inp = remove_unused_characters(inp)
    brace_map = create_brace_map(inp)

    memory_ptr = 0
    code_ptr = 0
    memory = bytearray(length)

    while code_ptr < len(inp):
        current_char = inp[code_ptr]
        code_ptr, memory_ptr, memory = handle_character(
            current_char, code_ptr, memory_ptr, memory, brace_map, **config)
        code_ptr += 1

    return memory
