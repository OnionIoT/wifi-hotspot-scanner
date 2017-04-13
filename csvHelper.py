import csv
import os

def write(filename, data, headers=None):
    # open the file for editing
    with open(filename, 'w') as file:
        # if headers are supplied, assume dictionaries are used for row data
        if headers is not None:
            writer = csv.DictWriter(file, headers=headers)
            # if the file doesn't exist, add a header row
            if not os.path.isfile(filename):
                writer.writeheader()
        # else treat list elements as values
        else:
            writer = csv.writer(file)
        
        # write the data to the file
        for row in data:
            writer.writerow(row)
        