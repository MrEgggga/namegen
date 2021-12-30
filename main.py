from namegen import generate_name
import curses
from curses import wrapper

favorites = []
def main(stdscr):
	global favorites
	curses.noecho()
	curses.cbreak()
	stdscr.keypad(True)
	curses.curs_set(0)

	stdscr.addstr('Use UP / DOWN to select a word and RIGHT to add it to your favorites\n')
	stdscr.addstr('Press any button to generate a new set of words and q to quit\n')
	stdscr.refresh()

	selected = 0

	names = []

	for i in range(10):
		names.append(generate_name())

	y, x = stdscr.getmaxyx()

	while True:
		ch = stdscr.getch()
		stdscr.clear()
		if ch == ord('q'):
			break
		elif ch == curses.KEY_UP:
			if selected > 0:
				selected -= 1
		elif ch == curses.KEY_DOWN:
			if selected < len(names) - 1:
				selected += 1
		elif ch == curses.KEY_RIGHT:
			favorites.append(names[selected])
			stdscr.addstr(y - 1, 0, 'Added to favorites')
		else:
			names = []
			for i in range(10):
				names.append(generate_name())
		
		for i in range(10):
			if(i == selected):
				stdscr.addstr(i, 0, names[i] + '\n', curses.A_STANDOUT)
			else:
				stdscr.addstr(i, 0, names[i] + '\n')
		
		stdscr.refresh()

wrapper(main)
print('Favorite names:')
for name in favorites:
	print(name)