# This is a test.
# We will take into account anything that comes along.
# I'll use some random code for testing Codereabbit.

def fibonacci(n: int) -> float:
    fib_seq = [0, 1]  # Initialize with the first two Fibonacci numbers
    for i in range(2, n):  # Loop to generate the sequence
        next_value = fib_seq[i] + fib_seq[i-1]  
        fib_seq.append(next_value)

    
    return fib_seq  


# lets's test the function