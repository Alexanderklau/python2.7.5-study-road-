def safe_float(obj):
    try:
        retval = float(obj)
    except ValueError:
        retval = None
    return retval
