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
current_date = get_latest_rates(from_currency,to_currency)[0]
current_rate = get_latest_rates(from_currency,to_currency)[1]
inverse_current_rate = reverse_rate(current_rate)
if st.button("Get Latest Rate"):
    # Display a header and text when the button is clicked
    st.header("Latest Conversion Rate")
    st.write(f"The conversion rate on {current_date} from {from_currency} to {to_currency} was {round_rate(current_rate)}. So {amount} in {from_currency} correspond to {amount*current_rate} in {to_currency}. The inverse rate was {round_rate(inverse_current_rate)}")
# Add a date selector (calendar)
from_date = st.date_input("Select a date")

# Add a button to get and display the historical rate for selected date, currencies and amount

historical_rate = get_historical_rate(from_currency, to_currency, from_date)
inverse_historical_rate = reverse_rate(historical_rate)

if st.button("Get Historical Rate"):
    # Display a header and text when the button is clicked
    st.header("Conversion Rate")
    st.write(f"The conversion rate on {from_date} from {from_currency} to {to_currency} was {round_rate(historical_rate)}. So {amount} in {from_currency} correspond to {amount*historical_rate} in {to_currency}. The inverse rate was {round_rate(inverse_historical_rate)}")










