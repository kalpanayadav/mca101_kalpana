def increment(num):
    '''
        objective   :   to calculate successor of the provided number
        input       :
                        num : contains number whose successor has to be calculated

        output      :   successor of the provided number
    '''

    '''
        approach    :   adding 1 to given number

    '''

    return num+1

def predecessor(num,temp = 0):
    '''
        objective   :   to calculate predecessor of given number
        input       :
                        num : contains number
                        
        output      :   predecessor of the given number
    '''

    '''
        approach    :   using increment function and using a temp variable

    '''
    
    assert num >= 0
    
    if num == 0:
        return "None"
   
    if num == 1:
        return 0
    if num == increment(temp) :
        return temp
    else :
        temp = increment(temp)
        return predecessor(num,temp)

    return temp




def listRev(list1,revSize = 0, count = 0):
    '''
    objective   : to calculate sum of the elements of the list
    user input  : list containing the element
    output      : sum of element of the list
    
    '''
    
    '''
    approach    : using recursion  
    '''
    revList = list()
    revSize = len(list1)
    assert len(list1) >= 1
    
    if len(list1) == 1:
        return list1[0]
    
    else:
        print(count,revSize)
        revList[count] = list1[predecessor(revSize)]
        count = count + 1
        revSize = revSize - 1
        print(count,revSize)
        listrev(list1,revSize,count)
    
    return revList
    
print(listRev([1,2,3,4,5,6]))
