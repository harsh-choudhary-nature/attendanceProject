def max_list(list1):
    n=len(list1)
    check=-100000
    for i in range(0,n):
        if list1[i]>check:
            check=list1[i]
    return check
def min_list(list1):
    n=len(list1)
    check=100000
    for i in range(0,n):
        if list1[i]<check:
            check=list1[i]
    return check
def comp_histogram(list1,num_bins=3):
    maximum,minimum=max_list(list1),min_list(list1)
    bin_size=(maximum-minimum)/num_bins
    dict1={}
    while minimum<maximum:
        key1=str(round(minimum,2))+"to"+str(round((minimum+bin_size),2))
        dict1[key1]=0
        for i in range(0,len(list1)):
            if round(minimum,2)<=list1[i] and list1[i]<round((minimum+bin_size),2):
                dict1[key1]+=1
        minimum=minimum+bin_size
    return dict1
