from blessed import Terminal
from time import sleep

t = Terminal()
term = t

if term.does_styling:
    with term.location(x=0, y=term.height - 1):
        print('Progress: [=======>   ]')
        sleep(1.0)
print(term.bold("60%"))


print(t.bold('Hi there!'))
print(t.bold_red_on_bright_green('It hurts my eyes!'))

with t.location(0, t.height - 1):
    print(t.center(t.blink('press any key to continue.')))

with t.cbreak():
    inp = t.inkey()
print('You pressed ' + repr(inp))

