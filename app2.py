import streamlit as st
st.title("welcome to basic streamlit app ")

age =st.slider("select your age ", 1,100)
city=st.selectbox("select your city",["Delhi ","mumbai","nashik","goa"])

if st.button("show button"):
   st.write("age",age)
   st.write("city",city)