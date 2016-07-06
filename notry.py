astr = raw_input("Hello: ")

try:
    istr = int(astr)
except Exception as e:
    istr = -1

print astr + " " + str(istr)
