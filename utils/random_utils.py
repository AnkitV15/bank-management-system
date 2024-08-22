import random

def random_num_gen(self,length = 11):
    # Generate a random number with a specified number of digits.
    
    if length < 1:
        raise ValueError("lenght must be atleast 1")
    
    min_value = 10**(length - 1)
    max_value = 10**length - 1
    return random.randint(min_value,max_value)