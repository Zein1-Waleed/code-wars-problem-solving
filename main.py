def calculate(firstnum,secnum,*opera):
    # print(opera[0])
    
    def add (firstnum,secnum):
        return firstnum + secnum
    if opera == ():
        return add(firstnum,secnum)
    

    if opera[0] == "add":
        return add(firstnum,secnum)
    elif opera[0] == "add"[0] :
        return add(firstnum,secnum)
    elif opera[0].lower() == "add".lower():
        return add(firstnum,secnum)



    def minus (firstnum,secnum):
        return firstnum - secnum


    if opera[0] == "subtract":
        return minus(firstnum,secnum)
    elif opera[0] == "subtract"[0] :
        return minus(firstnum,secnum)
    elif opera[0].lower() == "subtract".lower():
        return minus(firstnum,secnum)
    


    def multiply (firstnum,secnum):
        return firstnum * secnum
    
    if opera[0] == "multiply":
        return multiply(firstnum,secnum)
    elif opera[0] == "multiply"[0] :
        return multiply(firstnum,secnum)
    elif opera[0].lower() == "multiply".lower():
        return multiply(firstnum,secnum)
    


    
    
print(calculate(10,20))


def addition(*nums):
    total = 0
    for num in nums:
        if num == 10:
            continue
        if num == 5:
            total -=num
        else:
            total += num
    return total



print(addition(10, 20, 30, 10, 15)) # 65
print(addition(10, 20, 30, 10, 15, 5, 100)) # 160



def say_hello(name = "unknown",age = "unknown",country = "unknown"):
    # if name is None:
    #     name = "unknown"
    # if age is None:
    #     age = "unknown"
    # if country is None:
    #     country = "unknown"

    return f"Hello {name} Your Age Is {age} And You Live In {country}"
print(say_hello())