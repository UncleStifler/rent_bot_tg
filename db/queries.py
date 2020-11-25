

def districts():
    return 'select * from districts'

def routes(route_type):
    return f'select * from routes where type={route_type}'