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
import os
if os.path.exists('output'):
    pass
else:
    os.mkdir('output')
if os.name == 'nt':os.system('title Scarecrow - Discord Token Info ')
from time import sleep
death = """               ...
             ;::::;
           ;::::; :;
         ;:::::'   :;
        ;:::::;     ;.
       ,:::::'       ;           OOO\\
       ::::::;       ;          OOOOO\\
       ;:::::;       ;         OOOOOOOO
      ,;::::::;     ;'         / OOOOOOO
    ;:::::::::`. ,,,;.        /  / DOOOOOO                  ██████╗ ████████╗██╗
  .';:::::::::::::::::;,     /  /     DOOOO                 ██╔══██╗╚══██╔══╝██║ 
 ,::::::;::::::;;;;::::;,   /  /        DOOO                ██║  ██║   ██║   ██║
;`::::::`'::::::;;;::::: ,#/  /          DOOO               ██║  ██║   ██║   ██║
:`:::::::`;::::::;;::: ;::#  /            DOOO              ██████╔╝   ██║   ██║
::`:::::::`;:::::::: ;::::# /              DOO              ╚═════╝    ╚═╝   ╚═╝
`:`:::::::`;:::::: ;::::::#/               DOO
 :::`:::::::`;; ;:::::::::##                OO
 ::::`:::::::`;::::::::;:::#                OO
 `:::::`::::::::::::;'`:;::#                O
  `:::::`::::::::;' /  / `:#
   ::::::`:::::;'  /  /   `#

press enter to continue
"""
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
banner_tools = f'''{banner}
─────────────── MENU ───────────────
[1] Get token info
[2] Theme changer 
[3] about
[4] exit
────────────────────────────────────

'''
change_theme = f'''{banner}
────────── Change Theme ──────────
[1] scarecrow default
[2] scarecrow water
[3] scarecrow fire
[4] scarecrow neon
──────────────────────────────────

'''
about = f'''{banner}
───────────── About ─────────────
This tool made for educational purposes only
Author : Fadi
github : https://github.com/Fadi002

─────────────────────────────────

'''
config_theme = '''Scarecrow_def'''

class Scarecrow_Theme:
    def __init__(self):
        pass
    def water(self,text):
        os.system(""); faded = ""
        green = 10
        for line in text.splitlines():
            faded += (f"\033[38;2;0;{green};255m{line}\033[0m\n")
            if not green == 255:
                green += 15
                if green > 255:
                    green = 255
        return faded

    def fire(self,text):
        os.system(""); faded = ""
        green = 250
        for line in text.splitlines():
            faded += (f"\033[38;2;255;{green};0m{line}\033[0m\n")
            if not green == 0:
                green -= 25
                if green < 0:
                    green = 0
        return faded
    
    def brazil(self,text):
        os.system(""); faded = ""
        red = 0
        for line in text.splitlines():
            faded += (f"\033[38;2;{red};255;0m{line}\033[0m\n")
            if not red > 200:
                red += 30
        return faded
    def purplepink(self,text):
        os.system(""); faded = ""
        red = 40
        for line in text.splitlines():
            faded += (f"\033[38;2;{red};0;220m{line}\033[0m\n")
            if not red == 255:
                red += 15
                if red > 255:
                    red = 255
        return faded
    def get_theme(self,text):
        dirr = os.path.exists('settings')
        if dirr:
            pass
        else:
            os.mkdir('settings')
        file = os.path.exists('settings\\theme')
        if file:
            pass
        else:
            open('settings\\theme','w').write(config_theme)
        read_config =  open('settings\\theme','r').read()
        if read_config == 'Scarecrow_def':
            return self.brazil(text)
        elif read_config == 'Scarecrow_water':
            return self.water(text)
        elif read_config == 'Scarecrow_fire':
            return self.fire(text)
        elif read_config == 'Scarecrow_neon':
            return self.purplepink(text)
        else:
            open('settings\\theme','w').write(config_theme)
            return self.brazil
    def banner(self):
        print(self.get_theme(banner))
    
    def menu(self):
        print(self.get_theme(banner_tools)) 
    
    def fade_type(self,text):
        for c in text:
            print(c,end='',flush=True)
            sleep(0.009)
    
    def restart(self):
        dots = ['.','..','...','....']
        for i in dots:
            print(f'Restarting {i}',end='\r',flush=True)
            sleep(0.5)
    def exit_program(self):
        dots = ['.','..','...','....']
        for i in dots:
            print(f'exiting {i}',end='\r',flush=True)
            sleep(0.5)
        exit(-1)
    def change_theme_to(self,num):
        file = open('settings\\theme','w')
        if num == 1:
            file.write('Scarecrow_def')
        elif num == 2:
            file.write('Scarecrow_water')
        elif num == 3:
            file.write('Scarecrow_fire')
        elif num == 4:
            file.write('Scarecrow_neon')
        else:
            file.write('Scarecrow_def')
        done = f'done change theme to {num}'
        for i in done:print(i,end='',flush=True);sleep(0.009)
    def change_theme(self):
        print(self.get_theme(change_theme))
    def about(self):
        print(self.get_theme(about))
    def death_banner(self):
        print(self.get_theme(death))
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')
