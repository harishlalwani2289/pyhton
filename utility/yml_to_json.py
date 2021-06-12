import yaml
import json
import os
import datetime

path = "C:\\Users\\1021053\\Documents\\Spring_Practice\\all"

os.chdir(path)

def DateEncoder(obj):
  if isinstance(obj, (datetime.datetime, datetime.date)):
      return obj.strftime('%Y-%m-%d')

for file in os.listdir():
    print(file)
    if (file.endswith(".yaml")):
        yamlFilePath = "C:\\Users\\1021053\\Documents\\Spring_Practice\\all\\{0}".format(file)
        with open(yamlFilePath) as infle:
            os_list = yaml.load(infle, Loader=yaml.FullLoader)
        jsonFilePath = "C:\\Users\\1021053\\Documents\\Spring_Practice\\all\\json\\{0}.json".format(file[0:file.index(".")])
        with open(jsonFilePath, 'w') as outfile:
            json.dump(os_list, outfile, indent=4, default=DateEncoder)



# os_list = {}
#
# with open("C:\\Users\\1021053\\Documents\\Spring_Practice\\all\\64071.yaml") as infle:
#     os_list = yaml.load(infle, Loader=yaml.FullLoader)
#
# with open("C:\\Users\\1021053\\Documents\\Spring_Practice\\all\\json\\64071.json", 'w') as outfile:
#     json.dump(os_list, outfile, indent=4)
#
# print("JSON file written.")
