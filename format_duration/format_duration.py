from datetime import timedelta


def format_duration(seconds):
    conversion = timedelta(seconds=seconds)
    year = int(conversion.days / 365)
    days = conversion.days - (365 * year)
    hours = int(conversion.seconds / 3600)
    minutes = int((conversion.seconds - (3600 * hours)) / 60)
    sec = conversion.seconds - (hours * 3600) - (minutes * 60)


    formated = f"Year {year}, Days {days}, Hours {hours}, Mins {minutes}, seconds {sec}"

    print(formated)
    #return formated
