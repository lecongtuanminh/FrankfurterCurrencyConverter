
def round_rate(rate):
    """
    Function that will round an input float to 4 decimals places.

    Parameters
    ----------
    rate: float
        Rate to be rounded

    Returns
    -------
    float
        Rounded rate
    """
    return round(rate, 4)

def reverse_rate(rate):
    """
    Function that will calculate the inverse rate from the provided input rate.
    It will check if the provided input rate is not equal to zero.
    If it not the case, it will calculate the inverse rate and round it to 4 decimal places.
    Otherwise it will return zero.

    Parameters
    ----------
    rate: float
        FX conversion rate to be inverted

    Returns
    -------
    float
        Inverse of input FX conversion rate
    """
    if rate != 0:
        inverse_rate = 1 / rate
        return round(inverse_rate, 4)
    else:
        return 0
    
def format_output(date, from_currency, to_currency, rate, amount):
    """
    Function that will calculate the inverse rate from the provided input rate.
    It will check if the provided input rate is not equal to zero.
    If it not the case, it will calculate the inverse rate and round it to 4 decimal places.
    Otherwise it will return zero.

    Parameters
    ----------
    rate: float
        FX conversion rate to be inverted

    Returns
    -------
    float
        Inverse of input FX conversion rate
    """
    formatted_output= f"The conversion rate on {date} from {from_currency} to {to_currency} was {round_rate(rate)}. So {round_rate(amount)} in {from_currency} correspond to {round_rate(amount*rate)} in {to_currency}. The inverse rate was {round_rate(reverse_rate(rate))}"

    return formatted_output
   