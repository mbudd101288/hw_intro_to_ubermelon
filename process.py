log_file = open("um-server-01.txt")
# creates a variable that is accessing all of the information in a particular file

def generate_sales_reports(log_file, spec_day):
    """looks through a given file and prints 
        the info on a designated day of the week"""
    for line in log_file:
        line = line.rstrip()
        day = line[0:3]
        if day == spec_day:
            print(line)


generate_sales_reports(log_file, "Wed")
