#Sadia I 501051334
#s1
import csv
with open(r'C:\Users\itssa\OneDrive\Desktop\Data.csv', mode='r') as fileCSV:
    fCSV = csv.reader(fileCSV)
    for line in fCSV:
        print(line)

#s2
with open(r'C:\Users\itssa\OneDrive\Desktop\Data.csv', 'r') as fileCSV:
    fCSV = csv.reader(fileCSV)
    next(fileCSV)
    years = []
    sales = []
    for row in fCSV:
        years.append(int(row[0]))
        sales.append(sum(map(int, row[1:])))
        #open stats file as zip
    with open('stats.txt', 'w') as output:
        for year, sale in zip(years, sales):
            if year >= 2012 and year <= 2021:
                output.write(f'{year}: {sale}\n')

#s3
import matplotlib.pyplot as plt

# Read data from stats.txt file
with open('stats.txt', 'r') as f:
    data = [line.strip().split(': ') for line in f]

# Extract year and sales data from data list
years = [int(row[0]) for row in data]
sales = [int(row[1]) for row in data]

# Plot the data using a bar plot
plt.bar(years, sales)
plt.xlabel('Year')
plt.ylabel('Total Sales (Millions)')
plt.title('Total Sales by Year')
plt.show()

#step 4
# Initialize variables
sales_2021 = 0
sales_2022 = 0

# Loop through each row of data and add up the total sales for the first 6 months of each year
with open(r'C:\Users\itssa\OneDrive\Desktop\Data.csv', 'r') as fileCSV:
    fCSV = csv.reader(fileCSV)
    next(fCSV)
    for row in fCSV:
        year = int(row[0])
        sales = sum(map(int, row[1:7]))
        if year == 2021:
            sales_2021 += sales
        elif year == 2022:
            sales_2022 += sales

# Calculate sales growth rate and estimated sales for the last 6 months of 2022
sgr = (sales_2022 - sales_2021) / sales_2022
estimated_sales_2022 = [sales_2021 + sales_2021 * sgr * i for i in range(7, 13)]

# Write the results to the stats.txt file
with open('stats.txt', 'a') as output:
    output.write(f'Total sales in first 6 months of 2021: {sales_2021}\n')
    output.write(f'Total sales in first 6 months of 2022: {sales_2022}\n')
    output.write(f'Sales Growth rate: {sgr:.2%}\n')
    output.write('Estimated sales for the last six months in 2022:\n')
    for i in range(len(estimated_sales_2022)):
        output.write(f'{i + 7} 2022: {estimated_sales_2022[i]:.0f}\n')

#step 5
import matplotlib.pyplot as plt

# Estimated sales for last six months of 2022
estimated_sales = [-9335757, -10790570, -12245382, -13700195, -15155007, -16609820]

# Months for last six months of 2022
months = ['Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Create a horizontal bar graph
plt.barh(months, estimated_sales)

# Add labels and title
plt.xlabel('Sales')
plt.ylabel('Month')
plt.title('Estimated Sales for Last Six Months of 2022')

# Show the plot
plt.show()



