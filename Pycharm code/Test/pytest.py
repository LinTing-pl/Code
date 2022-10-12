import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
a = {'province': ['广东', '山东', '河南', '四川', '江苏', '河北', '湖南', '安徽', ],
     'population': [1314, 1356, 4747, 472, 2424, 242, 242, 2424, ],
     'city': ['广东', '山东', '河南', '四川', '江苏', '河北', '湖南', '安徽', ], }
cc = pd.DataFrame(a)
print(cc)
d = cc.sort_values(by=['province','city'])
print(cc.describe())
cc.plot(kind="hist")
plt.show()

