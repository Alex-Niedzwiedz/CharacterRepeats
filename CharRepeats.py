def CharRepeat(string):

    length = len(string)
    repeat=[]

    for i in range(length):
        for x in range(i+1,length):
            if string[i]==string[x] and repeat.count(string[i])==0:
                repeat.append(string[i])
    return repeat

def main():
    string="alexanderea"
    print("The repeating letters are:" , CharRepeat(string))
main()