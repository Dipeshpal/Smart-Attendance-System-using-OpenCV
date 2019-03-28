import os
import glob
for root,dirs, files in os.walk('Dipesh Paul 0827CS151066'):
    i = 0
    for file in files:
        if file.endswith('.jpg'):
            i = i+1
print(i)
i = i-1
os.remove('Dipesh Paul 0827CS151066/frame'+str(i)+'.jpg')

