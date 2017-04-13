import csv
import os

def write(filename, data, headers=None):
    # check if file does not exist so we know to write headers
    # must be checked before the file open, or it will create a blank file if it doesn't exist
    if os.path.isfile(filename):
        fileExists = True
    else:
        fileExists = False   
    # open the file for editing
    with open(filename, 'a') as file:
        # if headers are supplied, assume dictionaries are used for row data
        if headers is not None:
            writer = csv.DictWriter(file, fieldnames=headers)
            # if the file doesn't exist, add a header row
            if not fileExists:
                writer.writeheader()
                print "Wrote headers to " + filename
        # else treat list elements as values
        else:
            writer = csv.writer(file)
        
        # write the data to the file
        for row in data:
            writer.writerow(row)
        
    print "Saved to " + filename