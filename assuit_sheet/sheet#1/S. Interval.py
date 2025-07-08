entry = float(input())

if 0 <= entry and entry <= 25:
    print("Interval [0,25]")
elif 25 < entry and entry <= 50:
    print("Interval (25,50]")
elif 50 < entry and entry <= 75:
    print("Interval (50,75]")
elif 75 < entry and entry <= 100:
    print("Interval (75,100]")
else:
    print("Out of Intervals")