#day1.py
def main():
    instructions =open('/Users/jonathanshales/Documents/Programming/Advent/2017/Day1/input', 'r')
    data = instructions.read().rstrip()
    sum_1 = 0
    sum_2 = 0
    for x in range(len(data)):
        part2=int((x+(len(data))/2)%(len(data)))
        if data[x] == data[(x+1)%len(data)]:
            sum_1 += int(data[x])
        if data[x] == data[part2]:
            sum_2 += int(data[x])
    # if data[0]==data[len(data)-1]:
    #     sum += int(data[0])
    print(sum_1)
    print(sum_2)


main()