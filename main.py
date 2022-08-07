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
from src.info import Scarecrow_DIG
from src.tui import Scarecrow_Theme
from time import sleep
themes = Scarecrow_Theme()
DIG = Scarecrow_DIG
themes.clear()
themes.death_banner()
input()
themes.clear()
themes.banner()
themes.fade_type('Enter token to connect : ')
token = input()
try:
    token = token.replace(' ','')
except:
    pass
nice = Scarecrow_DIG(token).check()
if nice:
    pass
else:
    themes.fade_type('Invaild token\n')
    sleep(1)
    themes.exit_program()
themes.clear()
def main():
    themes.menu()
    themes.fade_type('Enter your choice : ')
    try:
        cohice = int(input())
    except:
        themes.fade_type('Invaild choice\n')
        sleep(1)
        themes.restart()
        themes.clear()
        main()
    if cohice == 1:
          themes.clear()
          print(themes.get_theme(DIG(token).token_info()))
          input()
          themes.clear()
          main()
    elif cohice == 2:
        themes.clear()
        themes.change_theme()
        themes.fade_type('Enter your choice : ')
        try:
            choicet = int(input())
        except:
            themes.fade_type('Invaild choice\n')
            sleep(1)
            themes.restart()
            themes.clear()
            main()
        if choicet == 1:
            themes.change_theme_to(1)
        elif choicet == 2:
            themes.change_theme_to(2)
        elif choicet == 3:
            themes.change_theme_to(3)
        elif choicet == 4:
            themes.change_theme_to(4)
        else:
            themes.fade_type('Invaild choice\n')
            sleep(1)
            themes.restart()
            themes.clear()
            main()
        themes.clear()
        main()
    elif cohice == 3:
        themes.clear()
        themes.about()
        themes.fade_type('press enter to back ...')
        input()
        themes.clear()
        main()
    elif cohice == 4:
        themes.exit_program()
    else:
        themes.fade_type('Invaild choice\n')
        sleep(1)
        themes.restart()
        themes.clear()
        main()
while True:
    main()