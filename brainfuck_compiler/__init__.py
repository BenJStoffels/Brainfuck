from brainfuck_compiler.config import get_arguments
from brainfuck_compiler.utils import get_input, print_memory
from brainfuck_compiler.run import run_inp
from brainfuck_compiler.edit import EditWindow


def main():
    args = get_arguments()

    inp = get_input(args.get("file"))

    if args.get("edit"):
        edit_window = EditWindow(inp, **args)
        edit_window.main()
    elif args.get("debug"):
        print("Debugging file...")
    else:
        memory = run_inp(inp, **args)
        print_memory(memory, args.get("hex"))
