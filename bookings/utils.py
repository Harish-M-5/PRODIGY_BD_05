from datetime import date

def calculate_total_price(room, check_in, check_out):
    days = (check_out - check_in).days
    return days * float(room.price_per_night)
