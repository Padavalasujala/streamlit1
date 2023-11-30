import streamlit as st 
st.set_page_config(page_title="My world",page_icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSnZ72152R-8jrVAPfb0HkU2P9sb72SAiJiJQ&usqp=CAU")
mymenu=st.sidebar.selectbox("MY MENU",("Home","Downloads","Contacts"))
st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSnZ72152R-8jrVAPfb0HkU2P9sb72SAiJiJQ&usqp=CAU")
st.title("Onlei technologies")
st.header("BY SUJALA")
st.text('This is streamlit Python')
if(mymenu=="Home"):
    st.markdown("<center><h1>Welcome</h1></center>",unsafe_allow_html=True)
    st.video("https://youtu.be/Bpc8YM1dINY?t=7")
elif(mymenu=="Contacts"):
    with st.form("my form"):
        name=st.text_input("enter name")
        dob=st.date_input("choose date of date of birth")
        marks=st.slider("choose marks")
        k=st.form_submit_button("submit form")
        if k:
            st.write("Name:" ,name,"dob:",dob,"marks:",marks)
elif(mymenu=="Downloads"):
    st.header("Downloads")
    st.download_button("Download Now","This is this the download data","textvirty1.txt")