import streamlit as st 


st.title("Submition form")



st.text_input('Enter your full name')

st.text_input('Enter your qulifation')

st.text_input('Enter your experence')

# redio button
genre = st.radio(
        "Select gender",
        ('male', 'female','other'))

 # print the text of genre
st.write(f"you select:{genre}")


    
      # add a file uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
   
   # button
if st.button("submit"):
    st.write(" submition successfully")
    
    
    
   