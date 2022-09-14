def fizzBuzz(n):
    for i in range(1,n+1):
        mod3 = i % 3
        mod5 = i % 5
        if (mod3 == 0) and (mod5 == 0):
            print("FizzBuzz")
        elif (mod3 == 0) and not (mod5==0):
            print("Fizz")
        elif (mod5 == 0) and not (mod3==0):
            print("Buzz")
        else:
            print(i)
        
    
if __name__ == '__main__':
    n = int(input().strip())
    fizzBuzz(n)
