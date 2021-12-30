from namegen import generate_name
import curses
from curses import wrapper

# Names the user picked as their favorite
favorites = []

def main(stdscr):
	global favorites
	
	# do some things to make the UI work
	curses.noecho()
	curses.cbreak()
	stdscr.keypad(True)
	curses.curs_set(0)

	stdscr.addstr('Use UP / DOWN to select a word and RIGHT to add it to your favorites\n')
	stdscr.addstr('Press any button to generate a new set of words and q to quit\n')
	stdscr.refresh()

	# Index of the currently selected name
	selected = 0

	# Array of current names
	names = []

	for i in range(10):
		names.append(generate_name())

	# We use these to put the "Added to favorites" alert at the bottom of the screen
	y, x = stdscr.getmaxyx()

	while True:
		# Get a keypress
		ch = stdscr.getch()
		stdscr.clear()
		# Quit
		if ch == ord('q'):
			break
		# Change selected name
		elif ch == curses.KEY_UP:
			if selected > 0:
				selected -= 1
		elif ch == curses.KEY_DOWN:
			if selected < len(names) - 1:
				selected += 1
		# Add to favorites
		elif ch == curses.KEY_RIGHT:
			favorites.append(names[selected])
			# Print alert at the bottom of the screen
			stdscr.addstr(y - 1, 0, 'Added to favorites')
		# Regenerate names
		else:
			names = []
			for i in range(10):
				names.append(generate_name())
		
		# Render names; render selected name as highlighted
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
