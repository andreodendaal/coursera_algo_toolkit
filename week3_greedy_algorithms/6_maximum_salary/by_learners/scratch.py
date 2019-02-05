if int(a[i][0]) == int(a[i + 1][0]) and int(a[i]) > int(a[i + 1]):
    a[i], a[i + 1] = a[i + 1], a[i]

elif int(a[i][0]) != int(a[i + 1][0]) and int(a[i]) < int(a[i + 1]):
    a[i], a[i + 1] = a[i + 1], a[i]