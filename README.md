# Currency Converter Using Frankfurter API

## Author
**Name:** Cong Tuan Minh Le  
**Student ID:** 25165123

## Description
This Python script provides a set of functions for interacting with the Frankfurter API to perform currency conversion and retrieve currency information. It includes the `get_currencies_list` function to fetch the list of available currencies, the `get_latest_rates` function to obtain the latest exchange rates, and the `get_historical_rates` to retrieve historical exchange rates based on specific dates. The code is designed to be easy to use and integrates with the Frankfurter API for accurate and up-to-date currency conversion needs.

During the development of the app, an issue was encountered with the rate returned by the call to the Frankfurter API. The **GET** call to the API has the default amount of 1, which returns the exact conversion rate from one currency to another. However, when the `amount` parameter is changed, the API returns the rate multiplied by the amount specified. This issue was resolved by setting the default amount to 1 and calculating the converted amount of money in the `format_output` function.

Additional functions could be developed to make multiple calls to the API and plot the conversion rates of currencies into graphs for better visualization or time series analysis. This would enable users to gain deeper insights into currency trends over time.
Please note that the current version of the app focuses on meeting the basic requirements of currency conversion, as specified for the assignment. Future development efforts can explore these enhancements for a more comprehensive currency analysis tool.



## How to Setup
This guide provides a step-by-step description of how to set up the development environment for the Currency Converter App. Ensure that you have Python installed on your system.

**Python Version**  
The Currency Converter App is developed using Python 3.11.4 and Streamlit version 1.26.0 . Please make sure you have an appropriate version of Python installed.

**Package Installation**  
To run the Currency Converter App, you need to install the required packages. You can do this using the Python package manager, pip. Open your terminal or command prompt and follow these steps:

1. Installing `python`:  
The application was developed using a Mac machine, which already has Python pre-installed. However, in case you have a Windows machine, you can visit the official Python website [here](https://www.python.org/downloads/windows/) and click on the "Latest Python 3 Release" link to download the latest Python installer for Windows. The Python package you download includes `datetime` and `json` as built-in modules so additional downloads are unnecessary.

2. Installing `streamlit`:  
To install `streamlit`, use the following command in terminal or command prompt:  
`pip install streamlit`

3. Installing `requests`:  
To install `requests`, use the following command in terminal or command prompt:  
`pip install requests`

## How to Run the Program
1. Ensure you have all the packages installed and an IDE for better understanding of the code.

2. Open the folder `dsp_at2_25165123` containing the files [`api.py`](api.py), [`app.py`](app.py), [`currency.py`](currency.py), [`frankfurter.py`](frankfurter.py) using your IDE (preferably [Visual Studio Code](https://code.visualstudio.com/download)).

3. Run the [`app.py`](app.py) by using the command `streamlit run app.py` in the terminal to view the Streamlit app in your browser.

3. Go to your default browser and start using the app.
## Project Structure
- `dsp_at2_25165123` : The main project folder.
    - [`api.py`](api.py) : Contains functions for making HTTP GET requests to APIs.
    - [`app.py`](app.py) : The Streamlit web application for currency conversion and rate retrieval.
    - [`currency.py`](currency.py) : Functions for currency-related calculations and formatting.
    - [`frankfurter.py`](frankfurter.py) : Functions for interacting with the Frankfurter API.
    - `README.md` : Documentation and project overview.

## Citations
- [Streamlit Documentation](https://docs.streamlit.io)
- [Requests Documentation](https://requests.readthedocs.io)
- [Python Documentation](https://docs.python.org/3/)

