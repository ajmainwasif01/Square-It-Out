def create_squares(start, end):
    return [num ** 2 for num in range(start, end + 1)]

def separate_odd_even(numbers):
    odd_numbers = [num for num in numbers if num % 2 != 0]
    even_numbers = [num for num in numbers if num % 2 == 0]
    return odd_numbers, even_numbers

if __name__ == "__main__":
    print("Welcome to 'Square it Out!'")
    
    start = int(input("Enter the starting number of the range: "))
    end = int(input("Enter the ending number of the range: "))
    
    squared_values = create_squares(start, end)
    print(f"\nList of squared values: {squared_values}")
    
    odd_values, even_values = separate_odd_even(squared_values)
    print(f"\nOdd values: {odd_values}")
    print(f"Even values: {even_values}")
