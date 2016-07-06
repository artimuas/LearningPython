def computepay(hours, rate):
    overtime = 0

    if hours > 40:
        overtime = hours - 40

    totalPay = (40 * rate) + (overtime * rate * 1.5)

    return totalPay

hrs = raw_input("Enter Hours: ")
h = float(hrs)

rate = raw_input("Enter Rate: ")
r = float(rate)

print computepay(h, r)
