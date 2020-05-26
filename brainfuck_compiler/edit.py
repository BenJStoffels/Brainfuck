import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from brainfuck_compiler.utils import save_input
from brainfuck_compiler.run import run_inp


class EditWindow:
    def __init__(self, input_string, file="", **config):
        self.input_string = input_string
        self.config = config
        self.memory = bytearray(config.get("length", 30))
        self.file = file
        self.setup_window()

    def setup_window(self):
        self.root = tk.Tk()
        self.root.title("Brainfuck editor")

        self.buttonsFrame = tk.Frame(self.root)
        self.saveButton = tk.Button(
            self.buttonsFrame, command=self.save, text='save')
        self.runButton = tk.Button(
            self.buttonsFrame, command=self.run, text='run')

        self.saveButton.pack(side=tk.RIGHT, padx=20)
        self.runButton.pack(side=tk.RIGHT, padx=0)

        self.buttonsFrame.pack(side=tk.TOP, pady=50, fill='x')

        self.text = ScrolledText(self.root)
        self.text.insert(tk.END, self.input_string)
        self.text.pack()

    def save(self):
        self.input_string = self.text.get("1.0", tk.END)
        print(self.input_string)
        save_input(self.file, self.input_string)

    def run(self):
        self.memory = run_inp(self.input_string, **self.config)
        print(self.memory)

    def main(self):
        self.root.mainloop()
