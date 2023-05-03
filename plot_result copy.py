import sys
import pandas as pd

csv_file = "result.csv"
if len(sys.argv) > 1:
    csv_file = sys.argv[1]
df = pd.read_csv(csv_file)


# calculate difference between each row and the previous row
df['diff'] = df['float'].diff()

offset = 2124092
print("int offset, float offset ( starting from 2124092)")
for i in range(20):
    print(1000, f"{float(df['diff'][i+offset]):f}")
