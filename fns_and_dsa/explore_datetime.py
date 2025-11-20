from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formartted_current_date = current_date.strftime("%y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formartted_current_date}")
    
    try:
        number_of_days = int(input("Enter the number of days to add to the current date: "))
    except ValueError:
        print("Error: Enter Valid valid Number")
        return
    
    time_delta = timedelta(days=number_of_days)
    future_date = current_date + time_delta
    calculate_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {calculate_future_date}")
    return

display_current_datetime()