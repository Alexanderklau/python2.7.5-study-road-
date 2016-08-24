def safe_float(object):
    try:
        retval = float(object)
    except (ValueError,TypeError),diag:
        retval = str(diag)
        return  retval
