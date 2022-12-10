def get_freq():
    all_freq={}
    str=input("enter the string ")
    #print(type(str))
    for i in str:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1
    print(all_freq)
get_freq()
