hrs = raw_input("Enter Hours: ")
h = float(hrs)

rate = raw_input("Enter Rate: ")
r = float(rate)

overtime = 0

if h > 40:
    overtime = h - 40

totalPay = (40 * r) + (overtime * r * 1.5)

print totalPay
