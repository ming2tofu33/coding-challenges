import sys

for line in sys.stdin:
    line = line.rstrip('\n')
    if line == '#': 
        break

    letter, sentence = line.split(' ', 1) 
    letter = letter.lower()
    cnt = sum(1 for ch in sentence if ch.lower() == letter)
    print(letter, cnt)
