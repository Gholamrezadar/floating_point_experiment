import matplotlib.pyplot as plt
import sys
import pandas as pd

csv_file = "result.csv"
if len(sys.argv) > 1:
    csv_file = sys.argv[1]
df = pd.read_csv(csv_file)

plt.plot(df['int'], df['float'], label="float")

plt.xlabel("int")
plt.ylabel("float")
plt.title("int reinterpretation to float")
plt.xlim(0, 22e8)
# plt.ylim(0, 22e8)
plt.legend()
plt.show()
