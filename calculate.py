from datetime import datetime

def calculate_date_difference(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            if len(lines) < 2:
                raise ValueError("The file must contain at least two lines with dates.")

            try:
                # Parse the dates from the first two lines
                date1 = datetime.strptime(lines[0].strip(), '%Y-%m-%d')
                date2 = datetime.strptime(lines[1].strip(), '%Y-%m-%d')
            except ValueError as ve:
                raise ValueError("Invalid date format. Dates must be in 'yyyy-mm-dd' format.") from ve

            # Calculate the difference
            difference = date1 - date2
            return difference.days
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except PermissionError:
        print(f"Error: Permission denied when trying to read the file '{file_path}'.")
        return None
    except ValueError as ve:
        print(f"Error: {ve}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

if __name__ == "__main__":
    file_path = 'data.txt'  # Path to the data file
    days_difference = calculate_date_difference(file_path)
    if days_difference is not None:
        print(f"The difference between the two dates is {days_difference} days.")