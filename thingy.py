t_inside = 1
t_outside = 1
t_desired = 1

def send_alert_to_open_window():
    return 0

def enable_ac():
    return 0

def enable_heating():
    return 0

def ultrasonic():
    return 0

while True:
    if t_inside < t_outside:
        if t_inside < t_desired:
            # It's warmer outside and you want it warmer inside
            send_alert_to_open_window()
        else:
            # It's warmer outside and you want it cooler inside
            enable_ac()
            ultrasonic()
    else:
        if t_inside < t_desired:
            # It's cooler outside and you want it warmer inside
            enable_heating()
        else:
            # It's cooler outside and you want it cooler inside
            send_alert_to_open_window()
            ultrasonic()