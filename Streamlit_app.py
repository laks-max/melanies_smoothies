import streamlit as st
from snowflake.snowpark.context import get_active_session
# Write directly to the app
st.title(":cup_with_straw: Customize Your Smoothie! :cup_with_straw:")
st.write(
"""Choose the fruits you want in your custom Smoothie!
""")
from snowflake.snowpark.functions import col

name_on_order=st.text_input('Name_on_smoothie:')
st.write('The name on your smoothie will be:',name_on_order)

cnx=st.connection("snowflake")
session =cnx.session()
import requests  
smoothiefroot_response = requests.get("[https://my.smoothiefroot.com/api/fruit/watermelon](https://my.smoothiefroot.com/api/fruit/watermelon)")  
st.text(smoothiefroot_response)
