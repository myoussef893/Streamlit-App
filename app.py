import streamlit as st 
import csv
def page_1(): 
    st.title('Add New Product')
    
    with st.form(key ='add product form',clear_on_submit=True,):
        image = st.camera_input('Item Photo:',key='photo')
        product_name = st.text_input('Product name:')
        product_price= st.number_input('Wholsale Price:')/12
        submit = st.form_submit_button('Save')
 
    try:
        if submit: 
            with open(f'./product_img/{product_name}.jpg','wb') as file :
                file.write(image.getbuffer())

            with open('data.csv','a',encoding='utf-8') as file: 
                writer = csv.writer(file)
                writer.writerow([f'./product_img/{product_name}.jpg',product_name,product_price])
                st.success(f'Successfully Saved {product_name} 🎉',icon='🎉')
                    

                
    except AttributeError: 
        st.warning('Take a Photo First.',icon='⚠️')


def page_2(): 
    st.title('Page 2')
    with open('data.csv','r') as f: 
       rd =  csv.reader(f)
       for i in rd: 
           st.image(i[0])
           st.text(i[1])
           st.text(i[2])

pg = st.navigation([
    st.Page( page_1, title='Page 1', icon='1️⃣'),
    st.Page( page_2, title='Page 2', icon='2️⃣')
])

pg.run()