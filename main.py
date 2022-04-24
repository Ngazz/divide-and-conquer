


def DAC_Max(a, index,b=1):
    max=-1
    if (index >=1-2):
        if (a[index]>a[index+1]):
            return a[index]
        else:
            return a[index+1]

    max=DAC_Max(a,index+1,1)
    if (a[index]>max):
        return a[index]
    else:
        return max

def DAC_Min(a,index,b=1):
    min=0
    if(a[index]<a[index+1]):
        return a[index]
    else:
        return a[index+1]

    min=DAC_Min(a,index+1,1)
    if(a[index]<min):
        return a[index]
    else:
        return min

if __name__=='__main__':
    min,max=0,-1
    a=[7,250,50,8,14,12,14]

    max=DAC_Max(a,0,7)
    min=DAC_Min(a,0,7)

    print("the minimum element in the array is: ", min)
    print("the maximum element in the array is: ",max)