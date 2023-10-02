import streamlit as st
import datetime

from frankfurter import get_currencies_list, get_latest_rates, get_historical_rate
from currency import reverse_rate, round_rate, format_output

# Display Streamlit App Title
st.header('FX Converter')
# Get the list of available currencies from Frankfurter
currencies_list = get_currencies_list()
# If the list of available currencies is None, display an error message in Streamlit App
if currencies_list is None:
    st.error("Error: No data from API was retrieved. Please check your data source.")
# Add input fields for capturing amount, from and to currencies
else:
    pass
amount = st.number_input("Amount to convert", value=50)
from_currency = st.selectbox('From Currency', currencies_list)
to_currency = st.selectbox('To Currency', currencies_list)
# Add a button to get and display the latest rate for selected currencies and amount

if st.button("Get Latest Rate"):
    date = get_latest_rates(from_currency,to_currency)[0]
    rate = get_latest_rates(from_currency,to_currency)[1]
    inverse_rate = reverse_rate(rate)
    # Display a header and text when the button is clicked
    st.header("Latest Conversion Rate")
    st.write(format_output(date, from_currency, to_currency, rate, amount))
# Add a date selector (calendar)
from_date = st.date_input("Select a date")
# Add a button to get and display the historical rate for selected date, currencies and amount



if st.button("Get Historical Rate"):
    # Display a header and text when the button is clicked
    rate = get_historical_rate(from_currency, to_currency, from_date)
    inverse_rate = reverse_rate(rate)

    st.header("Conversion Rate")
    st.write(format_output(from_date, from_currency, to_currency, rate, amount))









