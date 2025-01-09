import re


def text_analysis(text):
    # Find all words
    words = re.findall(r'\b\w+\b', text)
    num_words = len(words)
    
    # Find all sentences
    sentences = re.split(r'[.!?]', text)
    num_sentences = len([s for s in sentences if s.strip() != ''])
    
    # Find all unique words
    unique_words = set(words)
    num_unique_words = len(unique_words)
    
    # Find all numbers
    numbers = re.findall(r'\b\d+\b', text)
    num_numbers = len(numbers)
    
    return {
        'num_words': num_words,
        'num_sentences': num_sentences,
        'num_unique_words': num_unique_words,
        'num_numbers': num_numbers
    }

# Adição de loop infinito
a = 10
b = 100
while a < b:
    print("Maitha Tech!")

# nomes de variáveis 
a = 

# Example usage
text = "Hello world! This is a test. There are 2 sentences and 3 numbers: 1, 2, and 3."
analysis = text_analysis(text)
print(analysis)

def check_true(_condition: str) -> bool:
    if _condition == "answer":
        return True
    else:
        return False
    
def check_true(_condition: float) -> bool:
    if _condition < 10:
        return False
    else:
        return True
    
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7