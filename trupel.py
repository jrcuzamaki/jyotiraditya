# Define a list to hold the tuples
tuples = []
num_tuples = int(input("How many tuples do you want to enter? "))
for i in range(num_tuples):
    tuple_str = input(f"Enter tuple {i+1}: ")
    tuple_values = tuple(map(int, tuple_str.split()))
    tuples.append(tuple_values)
ascending_order = sorted(tuples)
descending_order = sorted(tuples, reverse=True)
print("Tuples in ascending order:", ascending_order)
print("Tuples in descending order:", descending_order)
