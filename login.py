import requests
import json
from datetime import datetime, timedelta
import nemreader

class meter():
    def __init__(self, NMI:int, email:str, password:str):
        self.nmi = NMI
        CADSiteLogin_url = 'https://customer.portal.sapowernetworks.com.au/meterdata/CADSiteLogin'
        CADSiteLogin_form_data = {
            "loginPage:SiteTemplate:siteLogin:loginComponent:loginForm": "loginPage:SiteTemplate:siteLogin:loginComponent:loginForm",
            "loginPage:SiteTemplate:siteLogin:loginComponent:loginForm:username": email,
            "loginPage:SiteTemplate:siteLogin:loginComponent:loginForm:password": password,
            "loginPage:SiteTemplate:siteLogin:loginComponent:loginForm:loginButton": "Login",
            "com.salesforce.visualforce.ViewState": "i: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",
            "com.salesforce.visualforce.ViewStateMAC": "AGV5SnViMjVqWlNJNkluSnNhMVpyTFVOZmVFZFRhV0ZqZUdkMVNrWTFhblpTUzNJMmJUQlZkWFE0UVc5UlJXeHFSMFJZYWtGY2RUQXdNMlFpTENKMGVYQWlPaUpLVjFRaUxDSmhiR2NpT2lKSVV6STFOaUlzSW10cFpDSTZJbnRjSW5SY0lqcGNJakF3UkRJNE1EQXdNREF4VVVwaGVWd2lMRndpZGx3aU9sd2lNREpITUVrd01EQXdNREJvTkVkSFhDSXNYQ0poWENJNlhDSjJabk5wWjI1cGJtZHJaWGxjSWl4Y0luVmNJanBjSWpBd05USTRNREF3TURBeVJrRjFTbHdpZlNJc0ltTnlhWFFpT2xzaWFXRjBJbDBzSW1saGRDSTZNVGMwTWpFeU5qVTBNVFUzTVN3aVpYaHdJam93ZlE9PS4uX2tjay1SVjlmUHdjYmFzSEsyc05ZQXU0TTlZNjdORzJBTlpkOWhXaS1Obz0="
        }

        CADSiteLogin_response = requests.post(CADSiteLogin_url, data=CADSiteLogin_form_data)
        CADSiteLogin_response_data = CADSiteLogin_response.text

        if(CADSiteLogin_response.status_code == 200):
            print("login successfull")
        else:
            print("login fail")

        self.sid = CADSiteLogin_response_data[CADSiteLogin_response_data.find("sid="):CADSiteLogin_response_data.find("&",CADSiteLogin_response_data.find("sid="))]

        cadenergydashboard_url = f"https://customer.portal.sapowernetworks.com.au/meterdata/CADRequestMeterData?selNMI={NMI}"
        cadenergydashboard_headers = {
            "Cookie": self.sid
        }

        cadenergydashboard_response = requests.get(cadenergydashboard_url, headers=cadenergydashboard_headers)
        cadenergydashboard_response_data = cadenergydashboard_response.text

        cadenergydashboard_raw = cadenergydashboard_response_data[cadenergydashboard_response_data.find('{"name":"downloadNMIData"'):cadenergydashboard_response_data.find('"}',cadenergydashboard_response_data.find('{"name":"downloadNMIData"'))+2]
        downloadNMIData = json.loads(cadenergydashboard_raw)

        self.method = downloadNMIData['name']
        self.csrf = downloadNMIData['csrf']
        self.auth = downloadNMIData['authorization']
    def getdata(self, filepath:str, startdate:datetime = datetime.today() - timedelta(2), enddate:datetime = datetime.today()):
        downloadNMIData_data = {
            "action": "CADRequestMeterDataController",
            "method": self.method,
            "data": [
                self.nmi,
                "SAPN",
                startdate.strftime("%a, %d %b %Y %H:%M:%S GMT"),
                enddate.strftime("%a, %d %b %Y %H:%M:%S GMT"),
                "Customer Access NEM12",
                "Detailed Report (CSV)",
                0
            ],
            "type": "rpc",
            "tid": 5,
            "ctx": {
                "csrf": self.csrf,
                "vid": "06628000004kHU7",
                "ns": "",
                "ver": 35,
                "authorization": self.auth
            }
        }
        downloadNMIData_headers = {
            "referer": "https://customer.portal.sapowernetworks.com.au/meterdata/apex/cadenergydashboard"
        }
        downloadNMIData_url = "https://customer.portal.sapowernetworks.com.au/meterdata/apexremote"

        downloadNMIData_response = requests.post(downloadNMIData_url, headers=downloadNMIData_headers, json=downloadNMIData_data)
        downloadNMIData = json.loads(downloadNMIData_response.text)
        filename = downloadNMIData[0]['result']['filename']
        self.data = downloadNMIData[0]['result']['results']

        if filepath[-1] != "\\":
            filepath += "\\"
        
        with open(filepath + filename, "w") as text_file:
            text_file.write(self.data)
        self.dataframes = nemreader.output_as_data_frames(filepath + filename, split_days=True, set_interval=None, strict=False)
        return filepath + filename

meterdata = meter(20021737816, "bfulham@bradyfulham.com", "Bfltdb02")
filepath = meterdata.getdata("D:\\Users\\Bfulh\\Desktop\\sapn data\\data", datetime.today() - timedelta(2), datetime.today())