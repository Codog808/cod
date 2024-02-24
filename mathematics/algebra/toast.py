import time

def yo(now, then):
    hours, minutes = now
    th, tm = then
    if th - hours < 0:
        totalh = th-hours
    else:
        totalh = 24 - hours
    if tm - minutes < 0:
        totalm = tm - minutes
    else:
        totalm = 60 - minutes

    totals = (totalh * 60 * 60) + (totalm * 60)
    return totals


def main():
    tim = yo((1, 0), (2,15))
    for i in range(tim//2):
        time.sleep(1)
        print(i, ": ")
        print(i * i)
        print()

main()
