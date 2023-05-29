#!/usr/bin/env python
# coding: utf-8

# In[45]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import ipywidgets as widgets
from ipywidgets import widgets
from ipywidgets import interact
import plotly.graph_objects as go


# In[3]:


df = pd.read_csv(r"C:\Users\GAMES\Downloads\HIRSHI\automation of DA\Placement_Data_Full_Class.csv")


# In[59]:


insights(df).automate_analysis()


# In[57]:


#insights_1.automate_analysis()


# In[58]:


pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

class insights:
    def __init__(self, data):
        self.data = data
        
    def automate_analysis(self):
        bold = '\33[1m'
        not_bold = '\33[m'
        print("\n")
        print("The dataset before cleaning")
        print("The dataset has {} rows and {} columns \n".format(self.data.shape[0],self.data.shape[1]))
        print("\n ---------------------------------------------------------------------\n")
        print(bold + 'Information about the data :' + not_bold)
        print('\n')
        print(self.data.info())
        print("\n ---------------------------------------------------------------------\n")
        
        df = pd.DataFrame(self.data)
        
        print(bold + "Preparing data cleaning ...." + not_bold)
        print('\n')
        self.data = self.data.fillna(0)   # filling the NaN with 0's
        print("Successfully filled the empty spaces and replaced the garbage values to '0'")
        print('\n')
  
        print(bold + "Plots for categorical columns: " + not_bold)
        print('\n')
        
        for i in self.data.columns:
            if len(pd.unique(self.data[i])) > 10:
                if self.data[i].dtypes == object:
                    df = pd.DataFrame((self.data[i].value_counts()/(len(df)*100)).sort_values(ascending=False).head(20))
                    plot1= df.plot(kind='bar',figsize=(12,6))
                    plt.xlabel(i,fontsize=15)
                    plt.ylabel('Frequency',fontsize=15)
                    plt.yscale('log')
                    plt.xticks(fontsize=12)
                    plt.show(plot1)
                    print("\n {} has {} unique values and {} percentage of null values \n".format(i,self.data[i].nunique(),round((self.data[i].isna().sum()/self.data.shape[0])*100,3)))
                    print('\n')
                    print(bold + 'Description of the column :' + not_bold)
                    
                    # descrie data
                    print(df[i].describe(include="all"))
                    print('\n')
                
                
                #for i in self.data.columns:
                if self.data[i].dtypes != object:
                    plt.figure(figsize=(12,9))
                    plot2= sns.displot(self.data[i], bins = 25, kde = False)
                    plt.xlabel(i,fontsize=15)
                    plt.ylabel('Frequency',fontsize=15)
                    plt.yscale('log')
                    plt.xticks(fontsize=12)
                    plt.show(plot2)
                    print("\n {} has {} unique values and {} percentage of null values \n".format(i,self.data[i].nunique(),round((self.data[i].isna().sum()/self.data.shape[0])*100,3)))
                    print('\n')
                    print(bold + 'Description of the column :' + not_bold)
                    
                    # descrie data
                    print(df[i].describe(include="all"))
                    print('\n')
            
            if len(pd.unique(self.data[i])) < 10:
                    df1 = df.groupby([i])[i].count()
                    fig = px.pie(df1, values=i, names=i, title=i)
                    fig.show()
                    print(" {} has {} unique values and {} percentage of null values \n".format(i,self.data[i].nunique(),round((self.data[i].isna().sum()/self.data.shape[0])*100,3)))
                    print(bold + " The unique values are: " + not_bold)
                    for uni in self.data[i]:
                        #print(self.data[i].unique())
                        print(self.data[i].value_counts())
                        break
                    print('\n')
                    print(bold + 'Description of the column :' + not_bold)
                    # descrie data
                    print(df[i].describe(include="all"))
                    print('\n')
        print("\n ---------------------------------------------------------------------\n")
        print('\n')
        print(bold + "Scatter plots : " + not_bold)
        print('\n')
        
        @widgets.interact(Select_x=df.columns.tolist(), Select_y=df.columns.tolist())
        def create_scatter(Select_x, Select_y):
            with plt.style.context("ggplot"):
                fig = plt.figure(figsize=(8,4))

                plt.scatter(x = df[Select_x],
                            y = df[Select_y],
                    #c=iris_df["FlowerType"],
                            s=20
                   )

                plt.xlabel(Select_x.capitalize())
                plt.ylabel(Select_y.capitalize())

                plt.title("%s vs %s"%(Select_x.capitalize(), Select_y.capitalize()))
                    
        print("\n ---------------------------------------------------------------------\n")
        print(bold + 'Correlation matrix :' + not_bold)
        print('\n')
        # correlation matrix and heatmap
        corr = df.corr()
        print(corr)
        print('\n')
        print('\n')
        print(bold + 'Heatmap :' + not_bold)
        print(sns.heatmap(corr, xticklabels=corr.columns, yticklabels=corr.columns , cmap="Blues"))
        
                    
        
        


# In[42]:


# Scatter plot with diff columns - choosing in HTML
# render HTML


# In[43]:


print(df.describe(include='all'))


# In[8]:


df


# In[46]:


pip install termcolor


# In[54]:


bold = '\33[1m'
print(bold + "hello")


# In[104]:


for i in df.columns:
    print(df[i].value_counts()/len(df)*100)


# In[218]:


for i in df.columns:
    if len(pd.unique(df[i])) < 10:
        df1 = df.groupby([i])[i].count()
        fig = px.pie(df1, values=i, labels = i, title=i)
        fig.show()


# In[ ]:





# In[179]:


df


# In[245]:


corr = df.corr()


# In[246]:


corr


# In[251]:


sns.heatmap(corr, xticklabels=corr.columns, yticklabels=corr.columns , cmap="Blues")


# In[276]:


df['ssc_p'].plot(kind='box', title='Marks of students')


# In[ ]:



        # DATA CLEANING:
        
        # replacing NaN
        #self.data = self.data.dropna(axis = 0, how = 'any') # drop the rows if any one value is NaN
        #missing_values = ['??','**']
        #self.data = self.data.replace(missing_values,np.NaN)  # changing all the missing values and other ??? *** values to NaN
        
        
        
                
        
        '''print(bold + 'Description of the columns :' + not_bold)
        print('\n')
        # descrie data
        for i in self.data.columns:
            print(df[i].describe())
            print('\n')'''
        
        
        
                
        # outliers:
        # finding quantiles:
        #Q1 = self.data.quantile(0.25)
        #Q3 = self.data.quantile(0.75)
        #IQR = Q3 - Q1
        #print("Visualize the outliers using Box plot...")
        
        ''''for i in self.data.columns:
            if self.data[i].dtypes == object:
                df = pd.DataFrame(self.data[i].value_counts().sort_values(ascending=False).head(20))
                plt.boxplot(self.data[i])
                
        for i in self.data.columns:
            if self.data[i].dtypes != object:
                plt.boxplot(self.data[i])'''
            
            
        #anything not in the range of (Q1 - 1.5 IQR) and (Q3 + 1.5 IQR) is an outlier, and can be removed
        #self.data = self.data[~((self.data < (Q1 - 1.5 * IQR)) |(self.data > (Q3 + 1.5 * IQR))).any(axis=0)]
        #print("Outliers are removed..!!..")
        
        
      


# In[44]:


widgets.Dropdown(
    options=['1', '2', '3'],
    value='2',
    description='Number:',
    disabled=False,
    
)


# In[47]:


x = df.columns.tolist()
target = df['gender']

@interact
def read_values(
    x_drop = widgets.Dropdown(
        description="Select :", options=x
    )
     
):

    fig = px.scatter(df, x = x_drop, y = target)
    go.FigureWidget(fig.to_dict()).show()


# In[51]:


@widgets.interact(feature1=df.columns.tolist(), feature2=df.columns.tolist())
def create_scatter(feature1, feature2):
    with plt.style.context("ggplot"):
        fig = plt.figure(figsize=(8,4))

        plt.scatter(x = df[feature1],
                    y = df[feature2],
                    #c=iris_df["FlowerType"],
                    s=20
                   )

        plt.xlabel(feature1.capitalize())
        plt.ylabel(feature2.capitalize())

        plt.title("%s vs %s"%(feature1.capitalize(), feature2.capitalize()))


# In[ ]:




