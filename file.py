fname = raw_input("Enter file name: ")

try:
    fhand = open(fname)
except Exception as e:
    print ("Unable to open file") + fname + ("\n Encountered exception") + e

for line in fhand:
    line = line.rstrip().upper()
    print line
