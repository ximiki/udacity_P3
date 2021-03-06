"""
Your task is to check the "productionStartYear" of the DBPedia autos datafile for valid values.
The following things should be done:
- check if the field "productionStartYear" contains a year
- check if the year is in range 1886-2014
- convert the value of the field to be just a year (not full datetime)
- the rest of the fields and values should stay the same
- if the value of the field is a valid year in range, as described above,
  write that line to the output_good file
- if the value of the field is not a valid year, 
  write that line to the output_bad file
- discard rows (neither write to good nor bad) if the URI is not from dbpedia.org
- you should use the provided way of reading and writing data (DictReader and DictWriter)
  They will take care of dealing with the header.

You can write helper functions for checking the data and writing the files, but we will call only the 
'process_file' with 3 arguments (inputfile, output_good, output_bad).
"""
import csv
import pprint

INPUT_FILE = 'autos.csv'
OUTPUT_GOOD = 'autos-valid.csv'
OUTPUT_BAD = 'FIXME-autos.csv'

def print_SendToGood(output_good1, YOURDATA, header):
    with open(output_good1, "w") as g:
        writer = csv.DictWriter(g, delimiter=",", fieldnames= header)
        writer.writeheader()
        for row in YOURDATA:
            writer.writerow(row)


def print_SendToBad(output_bad1, YOURDATA, header):
    with open(output_bad1, "w") as b:
        writer = csv.DictWriter(b, delimiter=",", fieldnames= header)
        writer.writeheader()
        for row in YOURDATA:
            writer.writerow(row)

def process_file(input_file, output_good, output_bad):

    M_good = []
    M_bad = []
    
    with open(input_file, "r") as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames


        for row in reader:
            if (row['URI'][7:14] == "dbpedia"):
                #print row['URI'][7:14] 
                check_year = row['productionStartYear'][:4]
                if check_year == "NULL":
                    M_bad.append(row)
                elif int(check_year) >= 1886 and int(check_year) <= 2014:
                    row['productionStartYear'] = check_year
                    M_good.append(row)
                else:
                    M_bad.append(row)
    
    print_SendToGood(output_good, M_good, header)
    print_SendToBad(output_bad, M_bad, header)
        

def test():

    process_file(INPUT_FILE, OUTPUT_GOOD, OUTPUT_BAD)


if __name__ == "__main__":
    test()