import numpy as np 


zero_array = np.zeros((2,3))      # zeros   rows=2, cols=3
one_array = np.ones((3,))        # ones   rows=3, cols=1
empty_array = np.empty((2,2))      # uninitialized (faster)   rows=2, cols=2
arange_array = np.arange(0, 10, 2)  # like range, returns array   rows=5, cols=1
linspace_array = np.linspace(0, 1, 5) # 5 evenly spaced values   rows=5, cols=1
eye_array = np.eye(4)            # identity matrix   rows=4, cols=4
full_array = np.full((2,2), 7)    # fill with 7s


print("Zero Array:\n", zero_array)
print("One Array:\n", one_array)
print("Empty Array:\n", empty_array)
print("Arange Array:\n", arange_array)
print("Linspace Array:\n", linspace_array)
print("Identity Matrix:\n", eye_array)
print("Full Array:\n", full_array)
