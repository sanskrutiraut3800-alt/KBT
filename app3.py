import streamlit as st
st.title("basic calculator")

num1=st.number_input("enter first number", step=1, format="%d")
num2=st.number_input("enter second number",step=1,format="%d")


Operation=st.selectbox("choose op",["add","sub","mul","div"])
if st.button("calculate"):
    if Operation == "add":
        st.write(num1+num2)

    elif Operation == "sub":
        st.write(num1-num2)

    elif Operation =="mul":
        st.write(num1*num2)

    elif Operation == "div":
       
            st.write(num1*num2)

    else :
            st.write("cannot divided by zero")    

          

