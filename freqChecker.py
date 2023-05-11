from dateutil.parser import parse
import pandas as pd
import matplotlib.pyplot as plt

with open('leopard_screen.csv', 'r') as file:
    unedited = file.readlines()

times = []
for line in unedited:
    time = line.split(';')[1]
    times.append(parse(time.strip()))

print('done reading')

date_time = pd.to_datetime(times)

print('done converting to pd')

data = {'Timestamps': date_time, 'Count': [1 for each in date_time]}

df= pd.DataFrame(data)
print(df.head())

df = df.resample('S', on="Timestamps").Count.sum()
#plt.hist(df)
plt.title('Leopard Screen')
#plt.xlabel("Frequency")
#plt.ylabel("Data points")
#plt.show()
plt.plot(df)
plt.gcf().autofmt_xdate()
plt.show()
