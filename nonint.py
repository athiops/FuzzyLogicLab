hot = 0.7
humid = 0.6

joint_min = min(hot, humid)
joint_product = hot * humid

print("Joint membership using min:", joint_min)
print("Joint membership using product:", joint_product)