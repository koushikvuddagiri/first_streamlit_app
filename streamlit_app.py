import streamlit
streamlit.title ('My parents New Healthy Diner')

breakfast_items = ['Omega 3 & Blueberry Oatmeal', 'Kale, Spinach & Rocket Smoothie', 'Hard-Boiled Free-Range Egg']

streamlit.write('Breakfast Menu:')
for item in breakfast_items:
streamlit.write('-' + item)

