def generate_fibonacci(n):
    """
    Generate the first n Fibonacci numbers.
    
    :param n: The number of Fibonacci numbers to generate
    :return: A list containing the first n Fibonacci numbers
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fibonacci_sequence = [0, 1]
    for i in range(2, n):
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)
    
    return fibonacci_sequence

# Example usage
n = 10
print(f"The first {n} Fibonacci numbers are: {generate_fibonacci(n)}")