print("\n제14장 넘파이(NUMPY)와 MATPLOTLIB\n")

print("#P.3")
import matplotlib.pyplot as plt
X = [     1,      2,      3,      4,      5,      6,      7]
Y = [15.6, 14.2, 16.3, 18.2, 17.1, 15.0, 19.2]
plt.plot(X, Y)
plt.show()

print("\n#P.4")
X = [ "Mon", "Tue", "Wed", "Thu", "Fri",  "Sat", "Sun" ] 
Y = [15.6, 14.2, 16.3, 18.2, 17.1, 15.0, 19.2]
plt.plot(X, Y)
plt.xlabel("day"); plt.ylabel("temperature")
plt.show()

#응 냅다 쥬피터