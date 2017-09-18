def months(from_month=1, to_month=12):
    """
    Return a generator with months from 01 to 12.
    
    Params
    ------
    from_month: month from where you want to start, included
    to_month: last month that you want to include
    """
    for month in range(from_month, to_month+1):
        if month < 10:
            yield f'0{month}'
        else:
            yield str(month)
