import useful_functions as af
scores=[88,92,79,93,85]
mean=af.mean(scores)
curved=af.add_five(scores)
mean_c=af.mean(curved)
print("Scores ;",scores)
print("Original Mean :",mean)
print("New Mean :",mean_c)
print(__name__)
print(af.__name__)