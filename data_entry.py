from datetime import datetime
def get_date(prompt, allow_default=False):
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime("%d-%m-%Y")
    
    try:
        valid_date = datetime.strptime(date_str, "%d-%m-%Y")
        return valid_date.strftime("%d-%m-%Y")
    except ValueError:
        print("Invalid date format. Please enter the date in dd-mm-yyyy format.")
        return get_date(prompt, allow_default)

def get_amount():
    pass

def get_category():
    pass

def get_description():
    pass