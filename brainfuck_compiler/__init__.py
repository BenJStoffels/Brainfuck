from brainfuck_compiler.config import get_arguments
from brainfuck_compiler.utils import get_input, print_memory
from brainfuck_compiler.characters import remove_unused_characters
from brainfuck_compiler.run import run_inp


def main():
    args = get_arguments()

    inp = get_input(args.get("file"))
    inp = remove_unused_characters(inp)

    if not args.get("debug"):
        memory = run_inp(inp, **args)
        print_memory(memory, args.get("hex"))
    else:
        print("I'm still trying to find time to add the debugging features!\nBe patient...")
