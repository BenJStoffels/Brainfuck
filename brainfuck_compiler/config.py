import argparse


def get_arguments():
    """Kijkt wat je als argumenten hebt ingegeven by het runnen van het pythonscript.
    Geeft ook vanzelf handige errormessages, and een help pagina.
    Als je de helppagina wilt gebruiken type in uw powershell: python brainfuck.py -h"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "file",
        help="The brainfuck script you want to run"
    )
    parser.add_argument(
        "-l", "--length",
        help="the length of the memory (30)",
        type=int
    )
    parser.add_argument(
        "-x", "--hex",
        help="display the memory in hex", action="store_true"
    )
    parser.add_argument(
        "-a", "--ascii",
        help="display the output in ascii", action="store_true"
    )
    parser.add_argument(
        "-e", "--edit",
        help="edit file", action="store_true"
    )
    parser.add_argument(
        "-n", "--new",
        help="create new file", action="store_true"
    )
    parser.add_argument(
        "-d", "--debug",
        help="werkt nog niet.", action="store_true"
    )
    return get_config(parser.parse_args())


def get_config(args):
    return {
        "file": args.file,
        "length": args.length if args.length else 30,
        "hex": args.hex,
        "ascii": args.ascii,
        "edit": args.edit,
        "new": args.new and args.edit,
        "debug": args.debug
    }
