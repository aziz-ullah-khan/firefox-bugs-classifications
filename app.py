import streamlit as st
from joblib import load


bug_clf = load('bug_clf.joblib') # load the model
# sidebar
st.sidebar.info('You can check Firefox bug type online!')
add_selectbox = st.sidebar.selectbox("How would you like to predict?", ("Online", "+"))

st.title("Predicting Firefox bug type")
st.header('This application is predicting the type of firefox bug.')
if add_selectbox == "Online":
    bug = [st.text_area('Enter bug text')]
    output = ""
    
    if st.button("Predict"):
        output = bug_clf.predict(bug)
        output = str(output[0]) # since its a list, get the 1st item
        st.success(f"The bug type is {output}")
        st.balloons()
else:
    st.success('More features are comming soon!')