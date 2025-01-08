import warnings
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression



def app(car_df):
    warnings.filterwarnings('ignore')

    df = car_df
    fuel_dict = {"Petrol":0, "Diesel":1, "CNG":2}
    seller_dict = {"Dealer":0, 'Individual':1}
    trans_dict = {"Manual":0, "Automatic":1}

    df.Fuel_Type = df["Fuel_Type"].map(fuel_dict)
    df.Seller_Type = df['Seller_Type'].map(seller_dict)
    df.Transmission = df["Transmission"].map(trans_dict)

    df["Age"] = 2025-car_df['Year']
    df.drop(columns = ["Car_Name", "Year"], inplace = True)

    st.title("Visualise the Vehicle Price Prediction Web app ")

    if st.checkbox("Show the correlation heatmap"):
        st.subheader("Correlation Heatmap")
        fig, ax = plt.subplots(figsize=(4, 3))
        sns.heatmap(df.corr(), annot=True, ax=ax)
        bottom, top = ax.get_ylim()
        ax.set_ylim(bottom + 0.5, top - 0.5)
        st.pyplot(fig)
    

    if st.checkbox("Show Regression Graph"):
        option = st.selectbox("Select Column to see regression against Target Variable.", 
                              options= [ 'Present_Price', 'Kms_Driven', 'Fuel_Type', 'Seller_Type', 'Transmission', 'Owner', 'Age'], index= None)
        if option != None:
            
            X = df[[option]]
            y = df["Selling_Price"]

            x_train,  x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            lin_reg = LinearRegression()
            lin_reg.fit(x_train, y_train)

            fig, ax = plt.subplots(figsize=(10, 6))
            plt.scatter(X, y, color="g", label="Actual Data") 
            plt.plot(X, lin_reg.predict(X), color="b", label="Regression Line")  
            plt.title("Simple Linear Regression")
            plt.xlabel("Feature")
            plt.ylabel("Target")
            plt.legend()
            st.pyplot(fig)




