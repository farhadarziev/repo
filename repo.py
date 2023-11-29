total_weight = 713
box_weights = [0, 0, 0]
box_kilometr = [0, 0, 0]

for i in range(3):
    box_kilometr[i] = int(input())
    box_weights[i] = int(input())

while sum(box_weights) != total_weight:
    print("the cargo is not found")

    for i in range(3):
        box_kilometr[i] = int(input())
        box_weights[i] = int(input())

print("The cargo is found")