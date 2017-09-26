import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn 
from sklearn.preprocessing import StandardScaler
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report,confusion_matrix
# %matplotlib inline 

d1=pd.read_csv("niwe/2013/jun13.txt",sep="\t")
d2=pd.read_csv("niwe/2014/jun14.txt",sep="\t")
scalar = StandardScaler()
print d1.head()
print d2.head()

def clean(data):
	
	for col in data.columns:
		if 'Unnmaed' in col:
			del data[col]

clean(d2)

d2.rename(columns={'Temp':'TEMP'},inplace = True)
	
d1= pd.read_csv("niwe/2013/jun13.txt",sep="\t")
d1=d1.append(d2)
clean(d1)
print(d1)
X=d1[['10mSD', '10mWS','30mSD', '30mWS','50mSD',
       '50mWS','TEMP','Date','Time']]

y=d1[['50mDIR']]
scalar = StandardScaler()       
scalar.fit(X)
Features= scalar.transform(X)

df_feat = pd.DataFrame(Features,columns=X.columns)

X=df_feat

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=100)

knn = KNeighborsClassifier()
knn.fit(X_train,y_train)

pred  =  knn.predict(X_test)
pred = pred.tolist()
roundy=y_test['50mDIR'].tolist()

j=0
for i in roundy:
    roundy[j]=round(i,2)
    j=j+1

y_test=roundy
