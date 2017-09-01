import seaborn as sn
import pandas as pd
import matplotlib.pyplot as plt

array = [[727,  8  ,53,  25,  39,    5 , 4 , 13 , 82,  44],
 [  7 ,821 ,  6 , 10,   5    ,2  ,4   ,2  ,22  ,121],
 [ 46  , 0 ,652,  66 ,107   ,43  ,40,  30  , 9  , 7],
 [ 14  , 2  ,61 ,577 ,113,  125  ,40 , 32  ,13  ,23],
 [  7  , 0  ,46  ,39 ,812 ,   15 , 20 , 49  , 6  , 6],
 [  3  , 1 , 47 ,150  ,66  ,649  ,17  ,49  , 4   ,14],
 [  1  , 3,  49 , 69  ,80   , 27 ,751  ,2 ,  9  , 9],
 [  9  , 0,  22 , 47  ,65   ,38 , 8 ,791 ,  3  , 17],
 [ 32 , 19 , 8  ,21  ,15    ,1 , 6   ,8 ,859  ,31],
 [ 19  ,30,   8  ,14,   5   , 0,   2  , 9,  20 ,893]]

df_cm = pd.DataFrame(array, range(10),
                  range(10))
plt.figure(figsize = (10,7))
sn.set(font_scale=1.4)#for label size
sn.heatmap(df_cm, annot=True,annot_kws={"size": 12})# font size
plt.show()
