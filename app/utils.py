import requests 
import datetime 
 
 
def main(start_date, end_date=None):
    """
    Main function which hits the nasa api and retrieves the information needed 
    :param start_date: {str} start date in the format "YYYY-MM-DD"
    :param end_date: {str} end date in the format "YYYY-MM-DD"

    :return: {list} sorted list of the asteroids 
    :return: {str} Prompt telling the user that the date is invalid.  
    """
    url = "https://api.nasa.gov/neo/rest/v1/feed"
    if not is_valid_date(start_date):
        return 'Invalid Start date'

    if not is_valid_date(end_date):
        return "Invalid end date"

    if is_valid_end_date(start_date, end_date):
        params = {'API_KEY': "5ymTOYp1gHkK4UBagKOpxH5KtpiWADuHYrIJZHrF", 'start_date': start_date, 'end_date': end_date}
        res = requests.get(url, params=params)
        if res.status_code != 200: 
            return "Could not connect to https://api.nasa.gov/neo/rest/v1/feed"
        data = res.json()

        data = data['near_earth_objects']
        asteroid_list = get_obj_list(data)
        return sort_list(asteroid_list)
    else: 
        return 'Invalid end date'


def get_obj_list(data):
    """
    Function to create a list of all the objects approaching earth within the given dates 
    :param data: {dict} Dictionary of the date fetched from the NASA api 

    :return obj_list: {list} list of all the asteroids approaching earth 
    """
    obj_list = []
    for date in data.keys():
        obj_data = data[date]

        for obj in obj_data:
            temp_dict = {}

            temp_dict['name'] = obj['name']
            temp_dict['size_est'] = obj['estimated_diameter']['kilometers']
            temp_dict['date_and_time'] = obj['close_approach_data'][0]['close_approach_date_full']
            temp_dict['min_dist'] = obj['close_approach_data'][0]['miss_distance']['kilometers']
            obj_list.append(temp_dict)
    
    return obj_list


def sort_list(obj_list):
    """
    Function to sort the list according the closest distance to earth 
    :param obj_list: {list} unsorted list of the asteroids 

    :return: {list} sorted list of the asteroids 
    """
    return sorted(obj_list, key=lambda x: float(x['min_dist']))


def is_valid_end_date(start_date, end_date):
    """
    Function to check if the start and end dates are in the correct format and the end date is within the 7 day limit 
    :param start_date: {str} start date in the format "YYYY-MM-DD"
    :param end_date: {str} end date in the format "YYYY-MM-DD"

    :return: {bool} True or False based on the validity of the dates 
    """
    if end_date == None:
        return True

    start_year, start_month, start_day = list(map(int, start_date.split('-')))
    end_year, end_month, end_day = list(map(int, end_date.split('-')))
    s_date = datetime.date(start_year, start_month, start_day)
    e_date = datetime.date(end_year, end_month, end_day)
    diff = (e_date - s_date).days
    return 0 <= diff <= 7


def is_valid_date(date):
    """
    Function to check if the date is valid or not
    :param date: {str} date in the format "YYYY-MM-DD"

    :return: {bool} if the date is valid or not
    """
    t_list = list(map(int, date.split('-')))
    
    if len(t_list) != 3: 
        return False
    
    year, month, day = t_list
    
    try:
        newDate = datetime.datetime(int(year), int(month), int(day))
        return  True
    except ValueError:
        return False
