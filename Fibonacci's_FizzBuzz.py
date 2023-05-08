def fibs_fizz_buzz(n):
    fib_sequence=[1, 1]
    for i in range(n-2):
        fib_sequence.append(fib_sequence[-1]+fib_sequence[-2]) #Making next fib number
    for i in range(len(fib_sequence)):
        if fib_sequence[i]%3==0 and fib_sequence[i]%5==0:
            fib_sequence[i]="FizzBuzz"
        elif fib_sequence[i]%3==0:
            fib_sequence[i]="Fizz"
        elif fib_sequence[i]%5==0:
            fib_sequence[i]="Buzz"
    return fib_sequence[:n]
