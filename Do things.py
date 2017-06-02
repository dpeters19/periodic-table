from build_elements import build_elements

# Test with matplotlib
import matplotlib.pyplot as plt

elements = build_elements()

plt.plot([x.atomic_radius for x in elements], 'b-')
plt.title("Radius of Elements by Atomic Number")
plt.ylabel("Radius of element")
plt.xlabel("Element number")
plt.show()
