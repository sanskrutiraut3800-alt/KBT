import streamlit as st

st.title("Student Form")
st.markdown(
    """
    <style>
    div.stButton > button {
        background-color: pink ;
        color: white;
        
    }
    </style>
    """,unsafe_allow_html=True
)
with st.form("student_form"):
    name = st.text_input("Enter Name")
    roll_no = st.text_input("Enter Roll Number")
    student_class = st.text_input("Enter Class")

    submit = st.form_submit_button("Submit")

if submit:
    st.success("Form Submitted Successfully!")
    st.write("Name:", name)
    st.write("Roll No:", roll_no)
    st.write("Class:", student_class)