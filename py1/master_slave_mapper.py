import subprocess

def get_pods_info_wide(release_name):
    subprocess.run(["oc get pods -l app=", release_name])

# def master_slave_mapper(file1, file2):  # file1 is vector of string
#     IP_to_cache={}    # IP cache to mapper directory from file 2

#     lines = file2.readlines()
#     for line in lines:
#         arr = line.strip().split()
#         IP_to_cache[arr[5]]=arr[0]
    

#     # Initialize dictionaries to store master and slave data
#     master_data = {}
#     slave_data = {}

#     # First pass to identify master and slave data
#     for line in file1:
#         split_line = line.split()  # split the string on the basis of space

#         if split_line[2] == "master":
#             master_pod_ID = split_line[0]  # extracting pod ID
#             master_IP = split_line[1].split(":")[0]  # extracting master IP
#             master_data[master_pod_ID] = master_IP
#         elif "slave" in split_line:
#             slave_pod_ID = split_line[3]  # extracting pod ID
#             slave_IP = split_line[1].split(":")[0]  # extracting slave IP
#             slave_data[slave_pod_ID] = slave_IP

#     # Second pass to map masters to slaves
#     for master_id, master_ip in master_data.items():
#         if master_id in slave_data:
#             master_ip_cache=IP_to_cache[master_ip]
#             slave_ip_cache=IP_to_cache[slave_data[master_id]]
#             print(master_ip + " (" + master_ip_cache + ")" + " -> " + slave_data[master_id] + " (" + slave_ip_cache + ")" )  # printing

# fileOpen = open('./file1.txt','r') 
# fileOpen2 = open('./file2.txt', 'r')

# master_slave_mapper(fileOpen,fileOpen2)


print(get_pods_info_wide("vnan-racclient4"))