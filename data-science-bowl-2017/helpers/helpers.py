def verify_location(loc):
    loc = data_url + loc
    if os.path.isdir(loc) or os.path.isfile(loc) :
        print('Found and verified location: ' + loc)
    else:
        raise Exception('Failed to verify location: ' + loc)
    return loc
