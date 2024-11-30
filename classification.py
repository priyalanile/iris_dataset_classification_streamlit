import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier


#Decorator function @st.cache to ensure data doesn't need to be loaded everytime.
@st.cache_data
def load_data():
    iris = load_iris()
     
    df = pd.DataFrame(iris.data, columns=iris.feature_names) #input features
    df['species']=iris.target #target feature

    return df, iris.target_names

df, target_names = load_data()

model=RandomForestClassifier()
model.fit(df.iloc[:,:-1], df['species'])

st.title("IRIS Dataset ML Classification using Streamlit")
st.sidebar.title("Input Features")

sepal_length = st.sidebar.slider("Sepal Length", 
                                 float(df['sepal length (cm)'].min()), 
                                 float(df['sepal length (cm)'].max())
                                 )

sepal_width = st.sidebar.slider("Sepal Width", 
                                 float(df['sepal width (cm)'].min()), 
                                 float(df['sepal width (cm)'].max())
                                 )

petal_lenth = st.sidebar.slider("Petal Length", 
                                 float(df['petal length (cm)'].min()), 
                                 float(df['petal length (cm)'].max())
                                 )

petal_width = st.sidebar.slider("Petal Width", 
                                 float(df['sepal width (cm)'].min()), 
                                 float(df['sepal width (cm)'].max())
                                 )

input_data = [[sepal_length,sepal_width,petal_lenth,petal_width]]

#prediction:
prediction = model.predict(input_data)

print("prediction is:",prediction)

predicted_species = target_names[prediction[0]]
print("predicted species is",predicted_species)

st.write("Author: Priyal Nile")
st.write("Prediction")
st.write(f"The predicted species is:{predicted_species}")