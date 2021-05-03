import math;
import csv;

with open("data.csv", newline = '') as f:
    reader = csv.reader(f);
    file_data = list(reader);

data = file_data[0]

# To find Standard Deviation The steps are:

# 1. Find Mean
def mean(data):
    n = len(data);
    total = 0;
    for i in data:
        total += int(i);

    mean = total/n
    return mean;

# 2 Subract Mean from each value
# 3. Sqare each value then

squared_list = [];
for number in data:
    a = int(number) - mean(data) # This is step 2
    a = a**2
    squared_list.append(a); # This is Step 3

# 4. Add all the sqaures
sum = 0;
for i in squared_list:
    sum += int(i);

# 5. Divide the Sum of squares by the number of numbers - 1 (n-1)
result = sum/ (len(data) - 1);

# 6.Do the square root.
standard_deviation = math.sqrt(result)

print(standard_deviation);