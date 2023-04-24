import streamlit 
import subprocess
import pandas as pd
import requests
import snowflake.connector

# Set Streamlit app title
streamlit.title('My Parents New Healthy Diner')

# Display breakfast favorites
streamlit.header('Breakfast Favorites')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

# Display build your own fruit smoothie section
streamlit.header('🍌🥭 Build your own Fruit Smoothie 🥝🍇')

# Load fruit list from URL
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let users pick fruits to include in the smoothie
fruits_selected = streamlit.multiselect("Pick Some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the selected fruits in a table
streamlit.dataframe(fruits_to_show)

# Display Fruityvice Fruit Advice section
streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?', 'Kiwi')
streamlit.write('The user entered:', fruit_choice)

# Fetch fruit information from Fruityvice API
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)

# Install dependencies from requirements.txt file
subprocess.call("pip install -r requirements.txt", shell=True)

# Connect to Snowflake and fetch user information
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)
