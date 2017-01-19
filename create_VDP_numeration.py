"""create_vdp_numeration.py - create .csv file to be used with
Adobe InDesign "Data Merge" feature."""

import sys

try:
    file_name = input('File name?: ')
    csvfile = open(file_name, 'w')
    
    csvfile.write('number')

    """For duplex print jobs create an additional column in the csv file called
    "dummy" which will later be assigned to a page without numeration."""
    two_sides = input('Duplex? (y/n) ')
    if two_sides.lower() == 'y':
        csvfile.write(',dummy')
    csvfile.write('\n')

    # get user input for the number start and end of the sequence of numbers
    start = input('Start of seq.: ')
    end = input('End of seq.: ')

    # leading - end number will be used to calculate leading zeros in the loop
    leading = len(end)
    
    # loop from start to end number, write to file
    if start.isnumeric() and end.isnumeric():
        for i in range(int(start), int(end) + 1):

            """calculate number of leading zeros by substracting length
            of the current number from the leading variable"""
            zeros = (leading - len(str(i))) * '0'
            csvfile.write(zeros + str(i) + '\n')
    else:
        print('Start and end must be numeric.')
    csvfile.close()

except IOError as e:
    csvfile.write(str(e))
    csvfile.close()
except OSError as e:
    csvfile.write(str(e))
    csvfile.close()
