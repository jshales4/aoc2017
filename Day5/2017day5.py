#day5.py
def main():
    moves = 0
    instructions = []
    position = 0
    with open('/Users/jonathanshales/Documents/Programming/Advent/2017/Day5/input', 'r') as f:
        for line in f:
            instructions.append(int(line.rstrip()))
        instructions.append("out")
        while instructions[position]!="out":
            instructions[position]+=1
            position += instructions[position]-1
            moves+=1
    print(moves)
    f.close()
    moves = 0
    instructions = []
    position = 0
    with open('/Users/jonathanshales/Documents/Programming/Advent/2017/Day5/input', 'r') as f:
        for line in f:
            instructions.append(int(line.rstrip()))
        instructions.append("out")
        while instructions[position]!="out":
            if instructions[position]>=3:
                instructions[position]+=-1
                position += instructions[position]+1
            else: 
                instructions[position]+=1
                position += instructions[position]-1
            moves+=1
        print(moves)
        f.close() 

main()