
# EX3
# Name: Or Ron
# ID: 203712146
# Program:
# The program reads and analyzes a medical database file which is written in
# Of SQL commands and converts it to CVS format.


import re

# # # # # # # func is_insert  # # # # # # #
# the function gets a line from file and return
# true if 'INSERT INTO' is found in line and
# false if it does'nt 
# # # # # # # # # # # # # # # # # # #
def is_insert(line):
   return 'INSERT INTO' in line or False


# # # # # # # func is_create  # # # # # # #
# the function gets a line from file and return
# true if 'CREATE TABLE' is found in line and
# false if it does'nt 
# # # # # # # # # # # # # # # # # # #
def is_create(line):
    return 'CREATE TABLE' in line or False

# # # # # # # func get_values  # # # # # # #
# the function gets a line from file and return
# line in csv format
# # # # # # # # # # # # # # # # # # #
def get_values(line):
    line1 = line.partition(' VALUES ')[2]
    line1 = line1.replace('),','\n')
    line1 = line1.replace(');', ' ')
    line1 = line1.replace(')', ' ')
    line1 = line1.replace('(',' ')
    return line1

# # # # # # # func get_table_name  # # # # # # #
# the function gets a line from file and return
# line in csv format
# # # # # # # # # # # # # # # # # # #
def get_table_name(line):
    match = re.search('`([0-9_a-zA-Z]+)`', line)
    if match:
        return match.group(1)


# # # # # # # func read_next_column  # # # # # # #
# the function gets a line from file and check
# if this line is a new column under 'CREAT TABLE'
# # # # # # # # # # # # # # # # # # #
def read_next_column(line):
    match = re.search('\s\s`([0-9_a-zA-Z]+)`', line)
    if match:
        return match.group(1)
    else:
        return " "

# # # # # # # func main  # # # # # # #
# The function reads and analyzes a medical database file which is written in
# Of SQL commands and converts it to CVS format.
# # # # # # # # # # # # # # # # # # #
def main():
    with open("demo.sql", 'rb') as f:
        found_table = False
        for line in f.readlines():
            try:
                line = line.decode("utf-8")
            except UnicodeDecodeError:
                line = str(line)
            if is_create(line):
                found_table = True
                table_name = get_table_name(line)
                open(table_name + '.csv', 'w')
            else:
                if found_table:
                    with open(table_name + '.csv', 'a') as outcsv:
                        if not is_insert(line):
                            result = read_next_column(line)
                            if result != ' ':
                                outcsv.write(result + ",")
                        else:
                            outcsv.write("\n")
                            values = get_values(line)
                            outcsv.write(values)

if __name__ == '__main__':
    main()
