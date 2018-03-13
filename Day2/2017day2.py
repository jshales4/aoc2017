#day2.py
def main():
    sum_1 = 0
    sum_2 = 0
    with open('/Users/jonathanshales/Documents/Programming/Advent/2017/Day2/input', 'r') as f:
        for line in f:
            int_list = [int(x) for x in line.split("\t")]
            max=int_list[0]
            min=int_list[0]
            for i in range(len(int_list)):
                if int_list[i]<min:
                    min=int_list[i]
                if int_list[i]>max:
                    max=int_list[i]
                for p in range(len(int_list)-i):
                    if (int_list[i]/int_list[i+p]==(int(int_list[i]/int_list[i+p])))or int_list[i+p]/int_list[i]==int(int_list[i+p]/int_list[i]):
                        if int_list[i]>int_list[i+p]:
                            sum_2+=(int_list[i]/int_list[i+p])
                        elif int_list[i+p]>int_list[i]:
                            sum_2+=(int(int_list[i+p])/int(int_list[i]))
            sum_1+=max-min
    print(sum_1, sum_2)   

main()