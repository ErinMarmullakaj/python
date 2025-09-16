# import streamlit as st
#
# col1, col2, col3, col4, col5 = st.columns(5, gap="small", vertical_alignment="center")
# with col1:
#     st.header("col1")
#
#     st.write("This is column 1")
#
# with col2:
#     st.header("col2")
#     st.write("This is column 2")
#
# with col3:
#     st.header("col3")
#     st.write("This is column 3")
#
# with col4:
#     st.header("col4")
#     st.write("This is column 4")
#
# with col5:
#     st.header("col5")
#     st.write("This is column 5")

# st.sidebar.header("Sidebar")
#
# st.sidebar.write("This is a sidebar ")
# st.sidebar.selectbox("Choose one option", ["Option 1","Option 2","Option 3" ])
# st.sidebar.radio("GO to", ["Home", "Data", "Settings"])


import streamlit as st

with st.form("my_form", clear_on_submit=True):
    name = st.text_input("Name")
    age = st.slider("Age", min_value=0, max_value=100)
    email = st.text_input("Email")
    bio = st.text_area("Bio")
    terms = st.checkbox("I agree to the terms and ...")

    submit_button = st.form_submit_button(label="Submit")

if submit_button:
    st.write(f"Name: {name}")
    st.write(f"Age: {age}")
    st.write(f"Email: {email}")
    st.write(f"DESC: {bio}")

    if terms:
        st.write("You agreed to the terms")
    else:
        st.write("You didn't agree to the terms")