import streamlit as st
import pandas as pd
import numpy as np

st.title("Add a listing here")
st.markdown('---')
with st.form("Input form"):
    #price
    price = int(st.number_input('Insert your monthly rent in USD here'))
    #bedno
    bedno = int(st.number_input('Insert the number of bedrooms here'))
    #bathno
    bathno = int(st.number_input('Insert the number of bathrooms here'))
    #dataavilable
    date = st.date_input('Insert the date available here')
    #streenameandNo
    address = st.text_input('Insert the street address and/or Apt no here')
    #city
    city = st.selectbox("Your city is?", ['Portland','Beavorton','Tigard','West Linn','Tualatin','King City','Damascus','Gresham','Sherwood','Lake Osewgo'])
    #state
    state = st.selectbox('Your state is?', ['Oregon'])
    #zipcode
    zipcode = int(st.number_input('Your zipcode? (5 digits)', max_value=99999))
    #phonenumber
    phone = st.text_input('Your phone to contact? (Enter numbers only, no special characters)')
    #url
    url = st.text_input("This property's URL?")
    #sqft
    sqft = int(st.number_input("Input the square footage here"))
    #type(condo)
    t = st.selectbox('Type of Home',['Single Family House','Townhouse','Condo','Apartment','Loft','Multiplex','Mobile Home','Duplex','Corporate Housing'])
    #deposit
    deposit = int(st.number_input('Input your deposit here'))
    #applicationfee
    appfee = int(st.number_input('Input your application fee here'))
    #washerDryer
    washer = st.selectbox('Will you provide washer/dryer?',['Yes','No'])
    #pets
    pets = st.selectbox('Will you allow pets?',['Allow all pets','No Pets','Cats Only','Dogs Only'])
    #parking
    parking = st.selectbox('Will you provide parking?',["On street","Off street",'No parking'])
    
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.markdown('---')
        st.write("===== Your have entered: =====")
        st.write("Price: $" + str(price))
        st.write("Beds: " + str(bedno) + " Baths: " + str(bathno))
        st.write("Available Date: " + str(date))
        st.write("Address: " + address + ", " + city + ", " + state + ", " + str(zipcode))
        st.write("Phone Number: " + phone)
        st.write("Property URL: " + url)
        st.write("SQFT: " + str(sqft))
        st.write("Type: " + t)
        st.write("The deposit is: " + str(deposit) + ", The application fee is: " + str(appfee))
        st.write("Other Details: " + "washer/dryer: " + washer + ", pets: " + pets + ", parking: " + parking)

with st.form("Confirm"):
    st.write("Please confirm the above details, are these accurate?")
    submitted = st.form_submit_button("I Confirm.")
    if submitted:
        try:
            df = pd.read_csv("listings.csv")
            df.loc[len(df.index)] = [price,
                                     bedno,
                bathno,
                date,
                address,
                city,
                state,
                zipcode,
                phone,
                url,
                t,
                deposit,
                appfee,
                washer,
                pets,
                parking,]
            df.to_csv('listings.csv',index=False)
        except pd.errors.EmptyDataError:
            df = pd.DataFrame({
                "price":price,
                "bed":bedno,
                "bath":bathno,
                "date":date,
                "street":address,
                "city":city,
                "state":state,
                "zipcode":zipcode,
                "phone":phone,
                "url":url,
                "type":t,
                "deposit":deposit,
                "app":appfee,
                "washer":washer,
                "pets":pets,
                "parking":parking,
            }, index=[0])
            df.to_csv("listings.csv", index=False)