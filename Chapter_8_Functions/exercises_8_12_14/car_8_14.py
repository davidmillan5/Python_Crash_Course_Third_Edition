def car_profile(manufacturer, model, **car_info):
    """Function to create a car profile"""
    car_info['manufacturer']= manufacturer
    car_info['model'] = model
    return car_info


mercedes_info = car_profile('mercedes','cla 250+', color = 'red', year = 2025, kind = 'electric')
print(mercedes_info)