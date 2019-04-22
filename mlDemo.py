from sklearn import tree

smooth = 1
uneven = 0
apple = 1
orange = 0

orchard = [[150, smooth],
         [130, smooth],
         [180, uneven],
         [160, uneven]]

result = [apple, apple, orange, orange]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(orchard, result)

weight = input("Entre com o peso: ")
surface = input("Entre com a superficie (1 para lisa, 0 para irregular): ")

resultUser = clf.predict([[weight, surface]])

if resultUser == 1:
    print("É uma maça")
else:
    print("É uma laranja")