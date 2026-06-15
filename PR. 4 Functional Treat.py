print("Welcome to the Data Analyzer and Transformer Program")
dataset = []
summary = {}

def update_summary():
    global summary
    if not dataset:
        summary = {}
        return

    summary = {
        "Total Elements": len(dataset),
        "Minimum": min(dataset),
        "Maximum": max(dataset),
        "Average": sum(dataset) / len(dataset)
    }

def display_values(*args):
    print("Values entered:")
    for value in args:
        print(value, end=" ")
    print()

def dataset_summary(**kwargs):
    print("Dataset Characteristics:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

while True:
    print("Main Menu:")
    print("1. Input Data")
    print("2. Display Data Summary")
    print("3. Calculate Factorial")
    print("4. Filter Data by Threshold")
    print("5. Sort Data")
    print("6. Display Dataset Statistics")
    print("7. Exit Program\n")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            data_input = input("Enter data for a 1D array (separated by spaces): ")
            words = [w for w in data_input.split() if w.strip()]
            if not words:
                print("No data entered. Please try again.\n")
                continue
            dataset = [int(x) for x in words]
            update_summary()
            display_values(*dataset)
            print("Data input successful!\n")

        case 2:
            if dataset:
                print(f"Data Summary: {dataset}\n")
                dataset_summary(
                    Total_Elements=len(dataset),
                    Minimum=min(dataset),
                    Maximum=max(dataset),
                    Sum=sum(dataset),
                    Average=sum(dataset)/len(dataset)
                )
                print()
            else:
                print("No data available. Please input data first.\n")

        case 3:
            def factorial(n):
                if n == 0 or n == 1:
                    return 1
                else:
                    return n * factorial(n - 1)
            num = int(input("Enter a non-negative integer to calculate its factorial: "))
            if num < 0:
                print("Factorial is not defined for negative numbers.\n")
                continue
            result = factorial(num)
            print(f"Factorial of {num} is {result}\n")

        case 4:
            if dataset:
                threshold = int(input("Enter a Threshold value: "))
                filtered_data = list(filter(lambda x: x > threshold, dataset))
                print(f"Data above the threshold: {filtered_data}\n")
            else:
                print("No data available. Please input data first.\n")

        case 5:
            print("Choose sorting option ")
            print("1. Ascending")
            print("2. Descending")
            option = int(input("Enter your choice: "))
            match option:
                case 1:
                    if dataset:
                        ascending_data = sorted(dataset)
                        print(f"Sorted Data in Ascending order: {ascending_data}\n")
                    else:
                        print("No data available. Please input data first.\n")
                case 2:
                    if dataset:
                        descending_data = sorted(dataset, reverse=True)
                        print(f"Sorted Data in Descending order: {descending_data}\n")
                    else:
                        print("No data available. Please input data first.\n")
                case _:
                    print("Invalid Input")

        case 6:
            if dataset:
                print(f"Data Summary: {dataset}\nTotal Elements: {len(dataset)}\nMinimum value: {min(dataset)}\nMaximum value: {max(dataset)}\nSum of all values: {sum(dataset)}\nAverage value: {sum(dataset) / len(dataset)}\n")
            else:
                print("No data available. Please input data first.\n")

        case 7:
            print("Thank you for using the Data Analyzer and Transformer program. Goodbye!")
            break

        case _:
            print("Invalid choice. Please try again.\n")