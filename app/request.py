import smartcar

access_token = 'a5fe6095-b180-42a9-bdbb-406142077c93'

response = smartcar.get_vehicle_ids(access_token)

vid = response['vehicles'][0]

vehicle = smartcar.Vehicle(vid, access_token)

odometer = vehicle.odometer()

print(vid)