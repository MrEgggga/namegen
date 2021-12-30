# namegen

This is a pretty janky name generator program I made using Markov chains. You can use this program in two ways:

- Run `main.py` to start an interactive name generator, where the program gives you 10 names at a time and you pick your favorites; when you quit, 
the program shows you which names you picked as favorites.
- Import `namegen.py` and use the `generate_name(min_len = 3, max_len = 20)` function, which takes two optional arguments:
  - `min_len`: the minimum length of the name
  - `max_len`: the maximum length of the name

This program should work with just about any version of Python, including both Python 2 and Python 3.

If you want to edit the list of names, simply edit `names-1880.txt`. There should be one name per line. The default list, as the filename suggests, is a list of the most common names for people born in 1880, but unfortunately I can't find the repository I got it from.
