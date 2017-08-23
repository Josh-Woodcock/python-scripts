import os

totalSize = 0
for filename in os.listdir('C:\\delicious'):
    totalSize = totalSize + os.path.getsize(os.path.join('C:\\delicious', filename))

print(totalSize)
