#day6.py
def main():
    moves = 0
    instructions = []
    position = 0
    with open('/Users/jonathanshales/Documents/Programming/Advent/2017/Day6/input', 'r') as f:
        for line in f:
            instructions = line.rstrip().split("\t")
            instructions = list(map(int, instructions))
            print(''.join(map(str, instructions)))

main()