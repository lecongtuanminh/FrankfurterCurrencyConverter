import requests

def get_url(url: str):
    """
    Function that will call a provide GET API endpoint url and return its status code and either its content or error message as a string

    Parameters
    ----------
    url : str
        URL of the GET API endpoint to be called

    Returns
    -------
    int
        API call response status code
    str
        Text from API call response
    """
    try:
        # Send a GET request to the provided URL
        response = requests.get(url)
        
        # Get the status code from the response
        status_code = response.status_code
        
        # Check if the request was successful (status code 200)
        if status_code == 200:
            # Return the status code and the content of the response
            return status_code, response.text
        else:
            # If the request was not successful, return the status code and an error message
            return status_code, f"Error: Request failed with status code {status_code}"
    
    except requests.exceptions.RequestException as e:
        # Handle any exceptions that may occur during the request
        return 500, f"Error: {str(e)}"


