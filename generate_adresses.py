import random

def generate_addresses(n,max_coordinate_value):
    
    addresses = [(random.randint(1, max_coordinate_value), random.randint(1, max_coordinate_value)) for _ in range(n)]
    return addresses
    