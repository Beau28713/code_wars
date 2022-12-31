import datetime
from statistics import median


def stat(strg: str) -> str:

    if len(strg) > 0:
        time_list = split_format_string(strg)

        times = [datetime.time.fromisoformat(x) for x in time_list]

        time_deltas = [
            datetime.timedelta(hours=x.hour, minutes=x.minute, seconds=x.second)
            for x in times
        ]

        average = find_average(time_deltas)
        range = find_range(time_deltas)
        med = find_med(time_deltas)
        answer = f"Range: {range} Average: {average} Median: {med}"

        return answer

    else:
        return ""


def find_average(time_deltas: list) -> str:
    return f"{datetime.timedelta(seconds=sum(x.seconds for x in time_deltas) // len(time_deltas))}".replace(
        ":", "|"
    ).zfill(
        8
    )


def find_range(time_deltas: list) -> str:
    return f"{max(time_deltas) - min(time_deltas)}".replace(":", "|").zfill(8)


def find_med(time_deltas: list) -> str:
    str_med = str(median(time_deltas)).zfill(8)

    if "." in str_med:
        dec_loc = str_med.find(".")
        return str_med[:dec_loc].replace(":", "|").zfill(8)
    else:
        return str_med.replace(":", "|").zfill(8)


def split_format_string(strg: str) -> list[str]:
    str_list = strg.split(",")

    for key, tm in enumerate(str_list):
        str_list[key] = str_list[key].replace("|", ":").strip()

    new_split = [y.split(":") for y in str_list]

    for d in new_split:
        for t in d:
            if len(t) <= 1:
                v = t.zfill(2)
                d[d.index(t)] = v

    return [":".join(x) for x in new_split]
