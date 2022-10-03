"""CP1404: Prac 4 total income | Wesley Gilsenan"""

FILENAME = "subject_data.txt"



def main():
    data = get_data()
    print_data(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    database = []
    for line in input_file:
        #print(line)  # See what a line looks like
        #print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        #print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        #print(parts)  # See if that worked
        #print("----------")
        database.append(parts)
    input_file.close()
    return database


def print_data(data):
    for subject in data:
        print(f" {subject[0]} is taught by {subject[1]:5} and has {subject[2]} students")


main()