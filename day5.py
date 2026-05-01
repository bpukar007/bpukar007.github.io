def divide(a, b):
    try: 
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    
def get_client_rate(rate):
    try:
        rate = int(rate)
        if rate <= 0:
            raise ValueError("Rate must be a positive.")
        return "Your rate is $" + str(rate) + " per hour."
    except ValueError as e:
        return "Error: " + str(e)

print(divide(100, 4))
print(divide(100, 0))
print(get_client_rate(25))
print(get_client_rate(-5))
print(get_client_rate("abc"))

