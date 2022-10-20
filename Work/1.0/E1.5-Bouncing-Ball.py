startingHeight = 100
bounceFactor = 3/5

bounceHeight = startingHeight
for i in range(10):
    bounceHeight = bounceHeight * bounceFactor
    print(round(bounceHeight))
