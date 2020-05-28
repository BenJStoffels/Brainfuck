# Brainfuck
I wrote a brainfuck interpreter and some scripts

## How to use it
It is really simple to get started, you can run `python brainfuck.py delen.bf.txt` to run my brainfuck script for dividing by 10
If you want to run your own scripts, run the command `python brainfuck.py path/to/file.bf`. However, I recommend you just add them to the same folder, that will make it easier to run them.

## Features
I recommend you run `python brainfuck.py --help` to get help on all the features there are, but here is a short description.
`-x` to display memory in hex.
`-a` to display output in ascii value, standard is off, because I just like it when there are just numbers in the output, but you can turn it on if you want to.
`-l LENGTH` to set the length of the memory, the default is 30.
`-n` to create a new file, note that this only works when edit mode is turned on. There is no use in creating a new file and running it, because it's going to be empty.
`-e` to edit a file, or create a new one, see above, from there you can run it but the output will still be in the terminal.
`-d` is something for the future, I want to make a debug mode, where you can step trough the code, and add breakpoints, and so on and on and on. I will do this in the next commit hopefully.
