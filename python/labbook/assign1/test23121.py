def fizzbuzz(a):
    for x in range(1,a+1):
        if x%3==0 and x%5==0:
            print("FizzBuzz")
        elif x%3==0 and x%5!=0:
            print("Fizz")
        elif x%5==0 and x%3!=0:
            print("Buzz")
        else:
            print(x)  
a=20
fizzbuzz(a)      