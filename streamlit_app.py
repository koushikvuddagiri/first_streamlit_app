import streamlit as st

# Set the title of the web page
st.title('My Parents New Healthy Diner')

# Define the breakfast menu items
breakfast_items = ['Omega 3 & Blueberry Oatmeal', 'Kale, Spinach & Rocket Smoothie', 'Hard-Boiled Free-Range Egg']

# Display the breakfast menu items using a bullet point list
st.write('Breakfast Menu:')
for item in breakfast_items:
    st.write('- ' + item)
