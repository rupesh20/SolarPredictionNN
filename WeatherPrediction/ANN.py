import pandas as pd
import numpy as np 
import sklearn
from keras.layers import Dense
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

d1= pd.read_csv("Bihta2010.csv")
d2= pd.read_csv("Bihta2011.csv")
d3= pd.read_csv("Bihta2012.csv")
d4= pd.read_csv("Bihta2013.csv")
d5= pd.read_csv("Bihta2014.csv")
frames = [d1,d2,d3,d4,d5]
l1 = ['Fill Flag 5','Fill Flag 4','Fill Flag 3',
      'Fill Flag 2','Fill Flag 1','Fill Flag 0',
      'Version','Snow Depth Units','Wind Speed',
      'Wind Direction Units','Precipitable Water Units']

def clean(data,l):
    for i in l:
        del data[i]
def Preprocessing(X_features,Y_Target):
	d1=pd.concat(frames)
	d1.reset_index(drop=True,inplace=True)

	frame = [Y_Target,d1['Solar Zenith Angle']]
	Y_Target = pd.concat(frame)
	Y_Target.drop([0,1])
	del Y_Target['Solar Zenith Angle']
	Y_Target.columns = ['SZA']
	Y_Target.drop([0,1],inplace=True)
	Y_Target.reset_index(drop=True,inplace=True)

	x=d1['Temperature'].tolist()
	y =d1['Relative Humidity'].tolist()
	z =d1['Clearsky DNI'].tolist() 

	X_features['Temperature'] = x
	X_features['Relative'] = y
	X_features['Clearsky DNI'] = z
	X_features.drop([0,1],inplace=True)
	X_features.reset_index(drop=True,inplace=True)

	le = LabelEncoder()
	for column in X_features.columns:
    if X_features[column].dtype == type(object):
        X_features[column] = le.fit_transform(X_features[column])

    Y_Target['SZA']=lb.fit_transform(Y_Target['SZA'])

	X_features.to_csv('Feature.csv',sep='\t')
	Y_Target.to_csv('Target.csv',sep='\t')


def SVM():
	
	x=pd.read_csv('Feature.csv',sep='\t')
	y=pd.read_csv('Target.csv',sep='\t')
	del x['Unnamed: 0']
	del y['Unnamed: 0']

	X_train,X_test,y_train,y_test = train_test_split(X_features[:43800],
										Y_Target,test_size=0.3,random_state=100)

if __name__ == '__main__':
	
	X_features = pd.DataFrame(index=None,columns=['Clearsky DNI',
								'Relative ','Temperature'])
	Y_Target = pd.DataFrame(index=None,columns=['Solar Zenith Angle'])
	for i in frames:
		clean(i,l1)

	for i in frames:
		i.columns=i.loc[1]	

	#Preprocessing(X_features,Y_Target)	

	SVM()