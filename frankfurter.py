from api import get_url
import json

BASE_URL = "https://api.frankfurter.app"

def get_currencies_list():
    """
    Function that will call the relevant API endpoint from Frankfurter in order to get the list of available currencies.
    After the API call, it will perform a check to see if the API call was successful.
    If it is the case, it will load the response as JSON, extract the list of currency codes and return it as Python list.
    Otherwise it will return the value None.

    Parameters
    ----------
    None

    Returns
    -------
    list
        List of available currencies or None in case of error
    """
    try:
        status_code, response_text = get_url(f"{BASE_URL}/currencies")

        if status_code == 200:
            # Parse the JSON response to get the list of currencies
            currencies_data = json.loads(response_text)
            currencies_list = list(currencies_data.keys())
            return currencies_list
        else:
            # If the request was not successful, return None
            return None
    
    except Exception as e:
        # Handle any exceptions that may occur during the request
        print(f"Error: {str(e)}")
        return None

def get_latest_rates(from_currency, to_currency):
    """
    Function that will call the relevant API endpoint from Frankfurter in order to get the latest conversion rate between the provided currencies. 
    After the API call, it will perform a check to see if the API call was successful.
    If it is the case, it will load the response as JSON, extract the latest conversion rate and the date and return them as 2 separate objects.
    Otherwise it will return the value None twice.

    Parameters
    ----------
    from_currency : str
        Code for the origin currency
    to_currency : str
        Code for the destination currency
    amount : float
        The amount (in origin currency) to be converted

    Returns
    -------
    str
        Date of latest FX conversion rate or None in case of error
    float
        Latest FX conversion rate or None in case of error
    """
    try:
        # Send a GET request to the conversion rate endpoint
        status_code, response_text = get_url(f"{BASE_URL}/latest?from={from_currency}&to={to_currency}")
        
        # Check if the request was successful (status code 200)
        if status_code == 200:
            # Parse the JSON response to get the conversion rate and date
            data = json.loads(response_text)
            date = data['date']
            rate = data['rates'][to_currency]
            return date, rate
        else:
            # If the request was not successful, return None for both date and rate
            return None, None
    
    except Exception as e:
        # Handle any exceptions that may occur during the request
        print(f"Error: Try selecting another currency")
        return None, None

def get_historical_rate(from_currency, to_currency, from_date):
    """
    Function that will call the relevant API endpoint from Frankfurter in order to get the conversion rate for the given currencies and date
    After the API call, it will perform a check to see if the API call was successful.
    If it is the case, it will load the response as JSON, extract the conversion rate and return it.
    Otherwise it will return the value None.

    Parameters
    ----------
    from_currency : str
        Code for the origin currency
    to_currency : str
        Code for the destination currency
    amount : float
        The amount (in origin currency) to be converted
    from_date : str
        Date when the conversion rate was recorded

    Returns
    -------
    float
        Latest FX conversion rate or None in case of error
    """

    
    try:
        # Send a GET request to the historical rate endpoint
        status_code, response_text = get_url(f"{BASE_URL}/{from_date}?from={from_currency}&to={to_currency}")
        
        # Check if the request was successful (status code 200)
        if status_code == 200:
            # Parse the JSON response to get the conversion rate
            data = json.loads(response_text)
            rate = data['rates'][to_currency]
            return rate
        else:
            # If the request was not successful, return None
            return None
    
    except Exception as e:
        # Handle any exceptions that may occur during the request
        print(f"Error: {str(e)}")
        return None

