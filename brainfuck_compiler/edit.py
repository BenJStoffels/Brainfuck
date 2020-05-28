import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from brainfuck_compiler.utils import save_input, get_hex_disp
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

        self.memoryFrame = tk.Frame(self.root)
        self.createMemory()
        self.memoryFrame.pack(side=tk.TOP, padx=20, fill='x')

        self.buttonsFrame = tk.Frame(self.root)
        self.saveButton = tk.Button(
            self.buttonsFrame, command=self.save, text='save')
        self.runButton = tk.Button(
            self.buttonsFrame, command=self.run, text='run')

        self.saveButton.pack(side=tk.RIGHT, padx=20)
        self.runButton.pack(side=tk.RIGHT, padx=0)

        self.buttonsFrame.pack(side=tk.TOP, pady=10, fill='x')

        self.text = ScrolledText(self.root)
        self.text.insert(tk.END, self.input_string)
        self.text.pack()

    def createMemory(self):
        self.memorySubFrame = tk.Frame(self.memoryFrame)
        for i, value in enumerate(self.memory):
            text = str(value) if not self.config.get(
                "hex") else get_hex_disp(value)
            label = tk.Label(self.memorySubFrame, text=text)
            label.grid(row=1, column=i)
            self.memorySubFrame.columnconfigure(i, weight=1)

        self.memorySubFrame.pack(side=tk.TOP, padx=0, fill=tk.BOTH)

    def updateMemory(self):
        self.memorySubFrame.destroy()
        self.createMemory()

    def save(self):
        self.input_string = self.text.get("1.0", tk.END)
        save_input(self.file, self.input_string)

    def run(self):
        self.memory = run_inp(self.input_string, **self.config)
        self.updateMemory()

    def main(self):
        self.root.mainloop()
