import datetime
import math



def convert_distance_to_time(current_time,distance):

    hours = distance / 18
    minutes = hours * 60
    hours, minutes = divmod(minutes,60)

    end_time = current_time + datetime.timedelta(hours=hours,minutes =minutes)
    return end_time



























start_of_day = datetime.time(8,00,00)





