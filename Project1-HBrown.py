def mean(data):
    total = 0
    num = len(data)
    if(num  == 0):
        return(0)
    for item in data:
        total = total + item
    mu = total / (num) 
    return (mu)

def median(data):
    num = len(data)
    if(num  == 0):
        return(0)
    data.sort()
    even = True
    if len(data)%2 == 1:
        even = False
    if even:
        slice_start = (len(data)//2) - 1
        slice_end   = (len(data)//2) + 1
        me      = sum(data[slice_start:slice_end]) / 2
    else:
        me      = data[len(data)//2]
    return (me)

def mode(data):
    num_elements =len(data)
    if(num_elements  == 0):
        return(0)
    hits = []
    for item in data:
        amount = data.count(item)
        values = (amount, item)
        if values not in hits:
           hits.append(values)
    hits.sort(reverse=True)
    if hits[0][0]>hits[1][0]:
        return(hits[0][1])
    else:
        print("No mode")
        return(0)

if __name__ == "__main__":
    data = [2,9,3,4,17,8]
    print("\nmean :", mean(data))
    print("\nmedian :", median(data))
    print("\nmode :", mode(data))
