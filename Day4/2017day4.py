#day4.py NOTE This solution works for all instances in which each 'word' is less than 10 characters. If one is greater than 10 characters increment the 10 on line 15 to 100, or any multiple of 10**n for positive n
def main():
    valids = 0
    valids2 = 0
    rows = 0
    with open('/Users/jonathanshales/Documents/Programming/Advent/2017/Day4/input', 'r') as f:
        for line in f:
            digitized_list = []
            list = line.rstrip().split(" ")
            if len(list)== len(set(list)):
                valids+=1
            for r in list:
                sum=0
                for char in r.lower():
                    sum+=10**(ord(char) - 96)
                digitized_list.append(sum)
            if len(digitized_list)==len(set(digitized_list)):
                valids2+=1

    print(valids)
    print(valids2) 

main()