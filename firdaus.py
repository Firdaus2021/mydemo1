#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
data=pd.read_csv('50_Startups.csv')
x=data.iloc[:,0:-2]
y=data.iloc[:,-1]
from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,train_size=0.80)
from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(xtrain,ytrain)


# In[2]:


from flask import Flask,render_template,request
firdaus=Flask(__name__)
@firdaus.route('/')
def a1():
    return render_template("F123.html")
@firdaus.route('/hello',methods=['GET','POST'])
def a2():
    if (request.method=='POST'):
        RD_Spend=int(request.form['rd'])
        Administration=int(request.form['adm'])
        Marketing_Spend=int(request.form['mar'])
        result=model.predict([[RD_Spend,Administration,Marketing_Spend]])
        return render_template("F123.html",tables=result)
if __name__ == '__main__':
    firdaus.run()


# In[ ]:




