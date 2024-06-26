# Checking the accuracy of 4 ml algorithms
# K-Nearest Neighbors (KNN), Support Vector Machine(SVM), Decision Tree(DT), and Random Forest(RF) 

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split import seaborn as sns
from sklearn.preprocessing import StandardScaler

data=pd.read_csv("/content/Framingha.csv") data.head()
data.info()
data.isnull().sum()
data_dup=data.duplicated().any()
print(data_dup)

data = data.drop_duplicates()
data.shape
data.describe()
data.hist(figsize=(15,8))
plt.tight_layout()
data.corr()
plt.figure(figsize=(17,10))
sns.heatmap(data.corr(),annot=True)
plt.show()

data.columns data['target'].value_counts()
sns.countplot(data['target'])
plt.xticks([0,1],['No-Disease','Disease'])
data['sex'].value_counts()
sns.countplot(data['sex'])
plt.xticks([0,1],['Female','Male'])
plt.show()

sns.distplot(data['age'])
sns.countplot(x='chest_pain_type', hue='target',data=data)
plt.xticks([0,1,2,3],['typical angina','atypical angina','non-anginal pain','asymptomatic'])
plt.xticks(rotation=75)
plt.legend(labels=['No-Disease','Disease'])
plt.show()

sns.countplot(x='sex',hue='target',data=data)
plt.xticks([0,1],['Female','Male'])
plt.legend(labels=['No-Disease','Disease'])
plt.show()
sns.distplot(data['age'])
plt.show()

data.columns
sns.countplot(data['chest_pain_type'])
plt.xticks([0,1,2,3],['typical angina','atypical angina','non-anginal pain','asymptomatic'])
plt.xticks(rotation=75)
plt.show()

sns.countplot(x='chest_pain_type', hue='target',data=data)
plt.xticks([0,1,2,3],['typical angina','atypical angina','non-anginal pain','asymptomatic'])
plt.xticks(rotation=75)
plt.legend(labels=['No-Disease','Disease'])
plt.show()

data.columns
cate_val=[]
cont_val=[]

for column in data.columns:
if data[column].nunique() <=10:
  cate_val.append(column)
else:
  cont_val.append(column)

cate_val cont_val
data.hist(cate_val,figsize=(10,6))
plt.tight_layout()
plt.show()

data.columns data['chest_pain_type'].unique()
cate_val.remove('sex')
cate_val.remove('target')
data=pd.get_dummies(data,columns=cate_val)
data.head()
st=StandardScaler()
data[cont_val]=st.fit_transform(data[cont_val])
X=data.drop('target',axis=1)
Y=data['target']
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=0)
X_train
Y_train
data

from sklearn import svm svm=svm.SVC()
svm.fit(X_train,Y_train)
from sklearn.metrics import accuracy_score Y_pred2=svm.predict(X_test) svma=accuracy_score(Y_test,Y_pred2)
print(svma)
Y_test
Y_pred2

from sklearn import metrics import numpy as np
from sklearn.metrics import confusion_matrix cm=metrics.confusion_matrix(Y_test,Y_pred2) print(cm) sns.heatmap(cm/np.sum(cm),fmt='.2%',annot=True) from sklearn.neighbors import KNeighborsClassifier knn=KNeighborsClassifier() knn.fit(X_train,Y_train) Y_pred3=knn.predict(X_test) accuracy_score(Y_test,Y_pred3)
score=[]
for k in range(1,40):
  knn=KNeighborsClassifier(n_neighbors=k)
  knn.fit(X_train,Y_train)
  Y_pred=knn.predict(X_test)
  score.append(accuracy_score(Y_test,Y_pred))
  score knn=KNeighborsClassifier(n_neighbors=1)
  knn.fit(X_train,Y_train)
  Y_pred3=knn.predict(X_test)
knna= accuracy_score(Y_test,Y_pred3)
print(knna) data=pd.read_csv('/content/Framingha.csv')
data.shape
data=data.drop_duplicates()
data.shape X=data.drop('target',axis=1)
Y=data['target']
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)

from sklearn.tree import DecisionTreeClassifier
dt=DecisionTreeClassifier()
dt.fit(X_train,Y_train)
Y_pred4=dt.predict(X_test)
dta=accuracy_score(Y_test,Y_pred4)
print(dta)

from sklearn.ensemble import RandomForestClassifier
rf=RandomForestClassifier()
rf.fit(X_train,Y_train)
Y_pred5=rf.predict(X_test)
rfa=accuracy_score(Y_test,Y_pred5)
print(rfa)
cmm=metrics.confusion_matrix(Y_test,Y_pred5)
print(cmm)

sns.heatmap(cmm/np.sum(cmm),fmt='.2%',annot=True)
final_data = pd.DataFrame({'Models':['SVM','KNN','DT','RF'],'ACC':[svma,knna,dta,rfa]})
final_data
colors=['red','orange','yellow','green']
plt.bar(final_data['Models'],final_data['ACC'],color=colors)
plt.title("accuracy of different models") plt.xlabel("Algorithms")
plt.ylabel("Accuracy")
plt.show() X=data.drop('target',axis=1)
Y=data['target']
X.shape

from sklearn.ensemble import RandomForestClassifier rf=RandomForestClassifier()
rf.fit(X,Y)
new_data=pd.DataFrame({
'age': 57,
'sex': 0, 'chest_pain_type':3 , 'resting_bp_s':160 , 'cholesterol':180 , 'fasting_blood_sugar':0 , 'resting_ecg':0 , 'max_heart_rate':156 , 'exercise_angina':0 , 'oldpeak': 1,
'ST_slope': 2
}, index=[1])

p=rf.predict(new_data) if p[0]==0:
print('NO-HEART DISEASE')
else: print('DISEASED')

import pickle filename='trained_model.sav'
pickle.dump(rf,open(filename,'wb'))
loaded_model=pickle.load(open('trained_model.sav','rb'))
new_data=pd.DataFrame({
'age': 57,
'sex': 0, 'chest_pain_type':3 , 'resting_bp_s':160 , 'cholesterol':180 , 'fasting_blood_sugar':0 , 'resting_ecg':0 , 'max_heart_rate':156 , 'exercise_angina':0 , 'oldpeak': 1,
'ST_slope': 2
}, index=[1])
#changing the input_data to numpy array input_data_as_numpy_array=np.asarray(new_data)

#reshape the array as it is prediction for one instance input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)

p=loaded_model.predict(input_data_reshaped)

if p[0]==0:
print('NO-HEART DISEASE')
else: print('DISEASED')
