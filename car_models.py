import numpy as np
import streamlit as st
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LinearRegression


def multi_lin_reg(car_df,Present_Price,	Kms_Driven,	Fuel_Type,	Seller_Type,	Transmission,	Owner,	Age):

    model_df = car_df.drop(columns = "Car_Name")
    X = model_df.drop(columns = "Selling_Price")
    y = model_df.Selling_Price 
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 42, test_size=0.20)

    multi_reg = LinearRegression()
    multi_reg.fit(X_train, y_train)

    y_train_pred = multi_reg.predict(X_train)
    y_test_pred = multi_reg.predict(X_test)

    # Classifify wine quality using the 'predict()' function.
    prediction = multi_reg.predict([[Present_Price,	Kms_Driven,	Fuel_Type,	Seller_Type,	Transmission,	Owner,	Age]])
    scores = round(multi_reg.score(X_train, y_train)* 100, 3)
    return prediction, scores



def app(car_df):
    df = car_df
    fuel_dict = {"Petrol":0, "Diesel":1, "CNG":2}
    seller_dict = {"Dealer":0, 'Individual':1}
    trans_dict = {"Manual":0, "Automatic":1}

    df.Fuel_Type = df["Fuel_Type"].map(fuel_dict)
    df.Seller_Type = df['Seller_Type'].map(seller_dict)
    df.Transmission = df["Transmission"].map(trans_dict)

    df["Age"] = 2025-car_df['Year']
    df.drop(columns = "Year", inplace = True)


    st.markdown(
        "<p style='color:red;font-size:25px'>This app uses <b>Linear Regression</b> for Car Price Predicton.",
        unsafe_allow_html=True)
    
    st.subheader("Select Values:")

    PresentPrice = st.slider('Select Present Price (lin lacs) value', float(df['Present_Price'].min()), float(df['Present_Price'].max()), 0.1)

    KmsDriven = st.slider('Select Kms Driven value', float(df['Kms_Driven'].min()),float(df['Kms_Driven'].max()), 0.1)

    st.write(fuel_dict)
    FuelType = st.slider('Select Fuel Type', int(df['Fuel_Type'].min()), int(df['Fuel_Type'].max()), 0 )

    st.write(seller_dict)
    SellerType = st.slider('Select Seller Type', int(df['Seller_Type'].min()), int(df['Seller_Type'].max()), 0)

    st.write(trans_dict)
    Transmissions = st.slider('Select Transmission Type', int(df['Transmission'].min()), int(df['Transmission'].max()), 0)
    
    Owners = st.slider('Select No of Owner/s', int(df['Owner'].min()), int(df['Owner'].max()), 0)

    V_Age = st.slider('Select Vehicle Age', float(df['Age'].min()), float(df['Age'].max()), 0.1)


    if st.button("Predict Vehilce Price "):
        prediction, score = multi_lin_reg(df, PresentPrice, KmsDriven, FuelType, SellerType, Transmissions, Owners, V_Age)
        st.write(f"Price of vehicle: {prediction*100000}")
        st.write(f"The accuracy of predicted price is {score:.3f}%""")
