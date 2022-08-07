'''
MIT License

Copyright (c) 2022 Fadi1337

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''
import os, requests,random
from datetime import datetime
banner = '''███████╗ ██████╗ █████╗ ██████╗ ███████╗ ██████╗██████╗  ██████╗ ██╗    ██╗    ██████╗ ████████╗██╗
██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗██╔═══██╗██║    ██║    ██╔══██╗╚══██╔══╝██║ 
███████╗██║     ███████║██████╔╝█████╗  ██║     ██████╔╝██║   ██║██║ █╗ ██║    ██║  ██║   ██║   ██║
╚════██║██║     ██╔══██║██╔══██╗██╔══╝  ██║     ██╔══██╗██║   ██║██║███╗██║    ██║  ██║   ██║   ██║
███████║╚██████╗██║  ██║██║  ██║███████╗╚██████╗██║  ██║╚██████╔╝╚███╔███╔╝    ██████╔╝   ██║   ██║
╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝  ╚══╝╚══╝     ╚═════╝    ╚═╝   ╚═╝                                                                                            
The best tool to get discord token info      (?_^
> Author : Fadi                               |\ )
> github : https://github.com/Fadi002         |/_\\

'''
class Scarecrow_DIG:
    def __init__(self,token):
        self.token = token
        self.headers = {'Authorization': f'{self.token}'}
        self.friendslist = []
        self.server_name_has_admin = []
        self.server_name = []
    def check(self):
        if requests.get("https://discord.com/api/v8/users/@me", headers=self.headers).status_code == 200:
            return True
        else:
            return False
    def get_servers(self):
        data = requests.get("https://discord.com/api/v8/users/@me/guilds",headers=self.headers)
        for i in data.json():
            if i['permissions'] == '4398046511103':
                self.server_name_has_admin.append(i['name'])
            self.server_name.append(i['name'])
        server_have_admin = ''
        for i in self.server_name_has_admin:
            server_have_admin = server_have_admin+"\n"+i
        data = f'''Server info :
───
servers : {str(len(self.server_name))}
servers has admin : {server_have_admin}
───
'''
        return data
    def get_friends(self):
        data = requests.get('https://discord.com/api/v8/users/@me/relationships',headers=self.headers)
        for i in data.json():
            self.friendslist.append(i['user']['username']+"#"+i['user']['discriminator'])
        data = f'''Friends info : 
───
friends : {str(len(self.friendslist))}
───
''' 
        return data
    def token_info(self):
        req = requests.get("https://discord.com/api/v8/users/@me",headers=self.headers)
        bd = ""
        Discord_Employee = 1
        Partnered_Server_Owner = 2
        HypeSquad_Events = 4
        Bug_Hunter_Level_1 = 8
        House_Bravery = 64
        House_Brilliance = 128
        House_Balance = 256
        Early_Supporter = 512
        Bug_Hunter_Level_2 = 16384
        Early_Verified_Bot_Developer = 131072
        flags = req.json()['flags']
        if (flags == Discord_Employee):
            bd += "Staff, "
        if (flags == Partnered_Server_Owner):
            bd += "Partner, "
        if (flags == HypeSquad_Events):
            bd += "Hypesquad Event, "
        if (flags == Bug_Hunter_Level_1):
            bd += "Green Bughunter, "
        if (flags == House_Bravery):
            bd += "Hypesquad Bravery, "
        if (flags == House_Brilliance):
            bd += "HypeSquad Brillance, "
        if (flags == House_Balance):
            bd += "HypeSquad Balance, "
        if (flags == Early_Supporter):
            bd += "Early Supporter, "
        if (flags == Bug_Hunter_Level_2):
            bd += "Gold BugHunter, "
        if (flags == Early_Verified_Bot_Developer):
            bd += "Verified Bot Developer, "
        if (bd == ""):
            bd = "N/A"
        
        username = req.json()['username']+"#"+req.json()['discriminator']
        userID = req.json()['id']
        phone = req.json()['phone']
        email = req.json()['email']
        language = req.json()['locale']
        mfa = req.json()['mfa_enabled']
        avatar_id = req.json()['avatar']
        nitro = False
        res = requests.get('https://discordapp.com/api/v9/users/@me/billing/subscriptions', headers=self.headers)
        nitro_data = res.json()
        nitro = bool(len(nitro_data) > 0)
        avatar_url = f'https://cdn.discordapp.com/avatars/{userID}/{avatar_id}.webp'
        creation_date = datetime.utcfromtimestamp(((int(userID) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC')
        if nitro:
            day1 = datetime.strptime(nitro_data[0]["current_period_end"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
            day2 = datetime.strptime(nitro_data[0]["current_period_start"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
            expday = abs((day2-day1).days)

        
            file_name = ''.join(random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(random.randint(10, 20)))
            os.mkdir('output\\'+file_name+'-shadow-DTI')
            result_info = f'''{banner}
──────────────────────────── TOKEN INFO ────────────────────────────
Basic info :
───
Username : {username}
Account age : {creation_date}
Language : {language}
Badges : {bd}
Avatar : {avatar_url if avatar_id else ""}
token : {self.token}
phone : {phone}
email : {email}
MFA enabled ? (2FA) : {mfa}
───

Nitro info : 
───
has nitro ? : {nitro}
exp. date : {expday if nitro else "0"} day(s)
───

{self.get_servers()}

{self.get_friends()}
────────────────────────────────────────────────────────────────────
all info saved in : output/{file_name}-shadow-DTI
press enter to back ... '''
            with open(f'output\\{file_name}-shadow-DTI\\info.txt','w',encoding='utf-8') as write:
                write.write(result_info)
                write.close()
            with open(f'output\\{file_name}-shadow-DTI\\friends_list.txt','w',encoding='utf-8') as write:
                for i in self.friendslist:
                    write.write(i+'\n')
                write.close()
            with open(f'output\\{file_name}-shadow-DTI\\servers.txt','w',encoding='utf-8') as write:
                for i in self.server_name:
                    write.write(i+'\n')
                write.close()
            with open(f'output\\{file_name}-shadow-DTI\\servers_admin.txt','w',encoding='utf-8') as write:
                for i in self.server_name_has_admin:
                    write.write(i+'\n')
                write.close()
            return result_info