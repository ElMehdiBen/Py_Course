import json

file = open("data.json", "r")

dict = file.read() # en format str

dict = json.loads(dict) # en format dict

print(dict["name"], dict["number"])

dict["date"] = "6-sep-2021"

f = open("data_result.json", "w")
f.write(json.dumps(dict))
f.close()