import streamlit as st
import pickle

st.title("Weather Prediction App..")
pn=st.number_input("Enter precipitation")
maxt=st.number_input("Enter Maximum temperature")
mint=st.number_input("Enter Minimum temperature")
wind=st.number_input("Enter Wind speed")
button=st.button("Predict!")

if button:
    lr=pickle.load(open("wp.pkl","rb"))
    res=lr.predict([[pn,maxt,mint,wind]])[0]
    st.markdown(f"Today weather situation : {res}")