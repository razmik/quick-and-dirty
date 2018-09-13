import json
import datetime
import os
from os import listdir
from os.path import isfile, join, isdir

folder_path = 'data'

filenames = [f for f in listdir(folder_path) if isfile(os.path.join(folder_path, f))]

# Placeholder for json objects
json_obj_array = []

for filename in filenames:

    filepath = os.path.join(folder_path, filename)

    # Read the json combined document line by line
    with open(filepath) as fp:
        line = fp.readline()
        cnt = 1
        while line:
            loaded_json = json.loads(line.strip())
            json_obj_array.append(loaded_json)
            line = fp.readline()
            cnt += 1

    app_removed_users = []
    for count, json_obj in enumerate(json_obj_array):

        # device_id = json_obj['user_dim']['device_info']['resettable_device_id']

        events = json_obj['event_dim']
        for event in events:

            event['utc_time'] = datetime.datetime.fromtimestamp(int(event['timestamp_micros'][:10])).strftime('%Y-%m-%d %H:%M:%S')

            if event['name'] == 'app_remove':
                app_removed_users.append(json_obj)
                break

"""
Now you can find all the users and their activities (who have deleted their app : app-remove) from;
app_removed_users
"""

# TODO

print('completed.')
