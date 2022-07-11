N, M = map(int, input().split())
week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
year = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

M += sum(year[:N])
print(week[M%7])

