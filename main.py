import requests
from requests.auth import HTTPBasicAuth

response = requests.get(url="http://192.168.1.1/maintenance/tools_system.htm",
                        auth=HTTPBasicAuth("admin", "admin"))
print(response.status_code)

response = requests.request(method="GET", url="http://192.168.1.1/maintenance/tools_system.htm",
                            auth=HTTPBasicAuth("admin", "admin"))
print(response.status_code)

response = requests.request(method="GET", url="http://192.168.1.1/Forms/tools_system_1",
                            auth=HTTPBasicAuth("admin", "admin"))
print(response.status_code)
