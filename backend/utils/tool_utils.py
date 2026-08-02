from datetime import datetime as dt, timedelta as td

def timeDifference(oldTime: str, newTime: str) -> int:

    parseDate = lambda dateStr: dt.strptime(dateStr, "%Y-%m-%d %H:%M")

    dt_oldTime = parseDate(oldTime)
    dt_newTime = parseDate(newTime)

    return dt_newTime - dt_oldTime


