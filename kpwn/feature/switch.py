with open("./init", "r") as f:
    file_data = f.read()

setuidgid_offset = file_data.find("setuidgid")
setuidgid_end = file_data[setuidgid_offset+10:].find(" ")

print(file_data[setuidgid_offset+10: setuidgid_offset+10+setuidgid_end])
file_data = file_data.replace(file_data[setuidgid_offset: setuidgid_offset+10+setuidgid_end], "setuidgid 0")

print(file_data)


