import streamlit as st
import os
import tempfile
## title
st.markdown("<h1 style='text-align: center;'>AI Voice Assistant</h1>", unsafe_allow_html=True)

image_path = 'https://moh2006.000webhostapp.com/images/sarah.jpg'

html_code = f"""
<div style="display: flex; justify-content: center;">
    <img src="{image_path}" alt="Centered Image" style="width: 300px; height: 300px;">
</div>
"""

# Display the HTML with the image
st.markdown(html_code, unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Now, you can talk with your files:PDF,DOCX,TXT</h1>", unsafe_allow_html=True)
# Custom CSS to center the link
st.markdown(
    """
    <style>
    .centered-link {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Create a container with the centered-link class
st.markdown(
    """
    <div class="centered-link">
        <a href="https://github.com/mohjaddoa/talk_2_files/" target="_blank">https://github.com/mohjaddoa/talk_2_files/</a>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)
# selecting multiple files
uploaded_files = st.file_uploader("Choose files: PDF,DOCX,TXT", accept_multiple_files=True,type=['pdf', 'txt', 'docx'])
# voice_button=st.button("voice query")
## this is loop for saveing all files content on temp,and get fils path
if uploaded_files:
    paths = get_paths(uploaded_files)
    # st.write(paths)
    set_text = files_to_text(paths)
    text_spliting = text_spliter(set_text)
    vector_data = text2vectors(text_spliting,'documents','OpenAIEmbeddings')
    with st.spinner('processing ....'):
        time.sleep(5)
    st.markdown("<h3 style='text-align: center;'>enter your query : by voice </h3>", unsafe_allow_html=True)
    query = st.text_input("enter your query ...")
    
                   






    
 
