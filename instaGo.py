from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time, sys, os, keyboard, threading
from colorama import init, Fore, Back, Style
from termcolor import colored
import ctypes
import getpass
from selenium.webdriver.common.keys import Keys
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning) 
ctypes.windll.kernel32.SetConsoleTitleW("InstaGo by Gorio")


os.system('color')

def colorpr(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

def start():
    global login, likes_by_tag, follow_by_tag, comment_by_tag, increase_followers, logincondition
    global open_instagram, unfollower, log_out, exitout
    logincondition=False
    try:
        options=Options()
        options.add_argument('--headless')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver=webdriver.Chrome(executable_path='drivers/chromedriver.exe', options=options)
        driver.get('https:\\instagram.com')
        try:
            driver.find_element_by_xpath('/html/body/div[4]/div/div/button[2]').click()
            time.sleep(0.5)
        except:
            pass
        
        def login(username, password):
            global logincondition
            while True:
                try:
                    print(colored('Try to login...', 'cyan'))
                    time.sleep(0.3)
                    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(Keys.CONTROL + "a")
                    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(Keys.DELETE)
                    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(username)
                    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(Keys.CONTROL+"a")
                    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(Keys.DELETE)
                    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(password)
                    try:
                        driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()
                    except:
                        print(colored('Error! Login failed!', 'red'))
                        return False
                    time.sleep(3.5)
                    
                    try:
                        time.sleep(3)
                        driver.find_element_by_xpath('//*[@id="slfErrorAlert"]')
                        print(colored('Error! Login failed!', 'red'))
                    except:
                        print(colored('Login succesfully!', 'cyan'))
                        logincondition=True
                        return False
                    try:
                        time.sleep(0.5)
                        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
                        time.sleep(1.5)
                        
                    except:
                        pass
                    try:
                        time.sleep(1)
                        driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()
                        time.sleep(0.5)
                    except:
                        pass
                    
                    return False
                    
                except:
                    pass
            
        
        def likes_by_tag(tag_name, amount):
            while True:
                likecounter=0
                driver.get(r"https:\\instagram.com\explore\tags"'/'+tag_name)
                time.sleep(0.5)
                try:
                    driver.execute_script("window.scrollTo(0, 900)") 
                    time.sleep(0.3)
                    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div/div[1]/div[1]/a/div/div[2]').click()
                    time.sleep(0.8)
                except:
                    print(colored('Error! Probabily "'+tag_name+'"'+" tag don't exist", 'red'))
                    return False
                for i in range(amount):
                    try:
                        driver.find_element_by_class_name('fr66n').click() #like
                        likecounter+=1
                        if visible_like==True:
                            user=driver.find_element_by_xpath('/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[1]/div/span').text
                            print(colored('Like putting to: '+user, 'cyan'))
                        if visible_like==False:
                            pass
                        driver.find_element_by_css_selector('body > div.RnEpo._Yhr4 > div.Z2Inc._7c9RR > div > div.l8mY4.feth3 > button').click()
                        time.sleep(2)
                        
                    except:
                        pass
                print(colored('Like put: '+str(likecounter), 'cyan'))
                return False
                
        def follow_by_tag(tag_name, amount):
            global visible_follower
            while True:
                followcounter=0
                driver.get(r"https:\\instagram.com\explore\tags"'/'+tag_name)
                time.sleep(0.5)
                try:
                    driver.execute_script("window.scrollTo(0, 900)") 
                    time.sleep(0.3)
                    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div/div[1]/div[1]/a/div/div[2]').click()
                    time.sleep(1)
                except:
                    print(colored('Error! Probabily "'+tag_name+'"'+" tag don't exist", "red"))
                    return False
                try:
                    for i in range(amount):
                        driver.find_element_by_class_name('bY2yH').click() #follow
                        followcounter+=1
                        if visible_follower==True:
                            user=driver.find_element_by_xpath('/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[1]/div/span').text
                            print(colored('Now following: '+user, 'cyan'))
                            
                        time.sleep(0.8)
                        driver.find_element_by_css_selector('body > div.RnEpo._Yhr4 > div.Z2Inc._7c9RR > div > div.l8mY4.feth3 > button').click()
                        time.sleep(1.4)
                    print(colored('Follow +: '+str(followcounter), 'cyan'))
                except:
                    print(colored('Error! Probabily you were ban! Try later...', 'red'))
                return False
                
        def comment_by_tag(tag_name, amount, comment):
            while True:
                comment_counter=0
                driver.get(r"https:\\instagram.com\explore\tags"'/'+tag_name)
                time.sleep(0.4)
                try:
                    driver.execute_script("window.scrollTo(0, 900)") 
                    time.sleep(0.3)
                    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div/div[1]/div[1]/a/div/div[2]').click()
                    time.sleep(1.8)
                except:
                    print(colored('Error! Probabily "'+tag_name+'"'+" tag don't exist", 'red'))
                    return False
                try:
                    for i in range(amount):
                        time.sleep(3.5)
                        driver.find_element_by_xpath('/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea').click()
                        user=driver.find_element_by_xpath('/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[1]/div/span').text
                        driver.find_element_by_xpath('/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea').send_keys(comment) #write comment
                        time.sleep(1.4)
                        driver.find_element_by_xpath('/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/button/div').click() #send comment
                        driver.find_element_by_css_selector('body > div.RnEpo._Yhr4 > div.Z2Inc._7c9RR > div > div.l8mY4.feth3 > button').click()
                        print(colored('comment sent to: '+user, 'cyan'))
                        comment_counter+=1
                except:
                    print(colorpr(255, 165, 0, 'General error!'))
                    return False
                print(colored('comment sending: '+str(comment_counter), 'cyan'))
                return False
        def increase_followers(tag_name):
            global condition
            
            def stop():
                global condition
                while True:
                    if keyboard.is_pressed('CTRL') and keyboard.is_pressed('C'):
                        condition=False
            
            condition=True
            threading.Thread(target=stop).start()
            driver.get(r"https:\\instagram.com\explore\tags"'/'+tag_name)
            try:
                driver.execute_script("window.scrollTo(0, 900)") 
                time.sleep(0.3)
                driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div/div[1]/div[1]/a/div/div[2]').click()
                time.sleep(1)
            except:
                print(colored('Error! Probabily "'+tag_name+'"'+" tag don't exist", "red"))
                condition=False
            print(colored('Increase followers... [ Press CTRL+C to stop ]', 'cyan'))
            while condition:
                try:
                    driver.find_element_by_class_name('bY2yH').click() #follow
                    user=driver.find_element_by_xpath('/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[1]/div/span').text
                    print(colored('Follow: '+user, 'cyan'))
                    time.sleep(3)
                    driver.find_element_by_class_name('bY2yH').click() #unfollow
                    time.sleep(0.5)
                    driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[3]/button[1]').click()
                    time.sleep(1)
                    print(colored('Unollow: '+user, 'cyan'))
                    time.sleep(0.8)
                    driver.find_element_by_css_selector('body > div.RnEpo._Yhr4 > div.Z2Inc._7c9RR > div > div.l8mY4.feth3 > button').click() #skip
                    time.sleep(6)
                except:
                    print(colored('Error! Probabily you were ban! Try later...', 'red'))
                    condition=False
                    
        def open_instagram(username, password):
            options=Options()
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            driver=webdriver.Chrome(executable_path='drivers/chromedriver.exe', options=options)
            try:
                driver.get('https:\\instagram.com')
            except:
                print('Error! Probabily you are offline!')
            try:
                driver.find_element_by_xpath('/html/body/div[4]/div/div/button[2]').click()
                time.sleep(0.5)
            except:
                pass
            try:
                print(colored('Try to login...', 'cyan'))
                time.sleep(0.3)
                driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(username)
                driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(password)
                try:
                    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()
                except:
                    pass
                try:
                    time.sleep(2.5)
                    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
                    time.sleep(1.5)
                    
                except:
                    pass
                try:
                    time.sleep(0.5)
                    driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()
                    time.sleep(0.5)
                except:
                    pass
                
            except:        
                pass
            
        def unfollower():
            while True:
                driver.get('https:\\instagram.com/'+username)
                time.sleep(0.3)
                driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a/div').click()
                time.sleep(1.5)
                counter=0
                try:
                    ita_en=driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/ul/div/li[1]/div').text
                    ita_en=ita_en.split('\n')
                    ita_en=ita_en[-1]
                    if ita_en=='Segui già':
                        buttons=driver.find_elements_by_xpath("//*[contains(text(), 'Segui già')]")
                    if ita_en=='Following':
                        buttons=driver.find_elements_by_xpath("//*[contains(text(), 'Following')]")
                    for btn in buttons:
                        btn.click()
                        time.sleep(1.5)
                        try:
                            driver.find_element_by_xpath("//*[contains(text(), 'Non seguire più')]").click()
                        except:
                            driver.find_element_by_xpath("//*[contains(text(), 'Non seguire più')]").click()
                        time.sleep(1.5)
                        print('An user unfollowed!')
                        counter+=1
                except:
                    return False
                    print('Finish to unfollowing!')
        
        def log_out():
            global logincondition
            try:
                driver.get('https:\\instagram.com')
                try:
                    time.sleep(1)
                    driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()
                    time.sleep(0.8)
                except:
                    pass
                try:
                    driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[6]/span/img').click()
                    time.sleep(0.8)
                    driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[6]/div[2]/div[2]/div[2]/div[2]/div').click()
                except:
                    pass
                
                logincondition=False
                print('Log out succesfully!')
                
            except:
                print(colored('Error! Log out failed!', 'red'))
        
        def exitout():
            print('Exiting...')
            driver.quit()
            time.sleep(0.5)
            os.system('cls')
            os.system('color')
        
    except:
        print(colored('General error!', 'red'))
    
threading.Thread(target=start).start()

while True:
    print(colored('''
         
 ___   __    _  _______  _______  _______  _______  _______ 
|   | |  |  | ||       ||       ||   _   ||       ||       |
|   | |   |_| ||  _____||_     _||  |_|  ||    ___||   _   |
|   | |       || |_____   |   |  |       ||   | __ |  | |  |
|   | |  _    ||_____  |  |   |  |       ||   ||  ||  |_|  |
|   | | | |   | _____| |  |   |  |   _   ||   |_| ||       |
|___| |_|  |__||_______|  |___|  |__| |__||_______||_______|
                                                    
                                                        
                                                       By Gorio
          
          ''', 'red'))
    
    try:
        input_=int(input(Fore.CYAN+'''
Login = '''+str(logincondition)+'''
                         
[1] - login
[2] - likes_by_hashtag
[3] - follow_by_hashtag
[4] - comment_by_hashtag
[5] - increase_followers             
[6] - open_instagram
[7] - unfollower++
[8] - log_out
[9] - exit

>>> '''))
                
        if input_>9 or input_<1:
            raise ValueError
    
        if input_==1:
            if logincondition==True:
                print(colorpr(255,165,0, 'Login alwready done!'))
                time.sleep(1.5)
                os.system('cls')
            else:
                username=input('\nEnter username here: ')
                password=getpass.getpass('Enter password here: ')
                print('___________________________________\n')
                try:
                    login(username=username, password=password)
                except:
                    print('Error! Probabily you are offline!')
                time.sleep(1.5)
                os.system('cls')
        
        if input_==2:
            if logincondition==True:
                tag_name=input("\nHashtag name: ")
                amount=int(input("Amount: "))
                while True:
                    try:
                        visible=input("Visible who you like (y/n): ")
                        if visible=='y' or visible=='Y':
                            visible_like=True
                            break
                        if visible=='n' or visible=='N':
                            visible_like=False
                            break
                    except NameError:
                        pass
                        
                print('___________________________________\n')
                print(colored('Try to putting like...', 'cyan'))
                likes_by_tag(tag_name=tag_name, amount=amount)
                time.sleep(2.5)
                os.system('cls')
            else:
                print(colored('Error! First you must be login (press 1)', 'red'))
                time.sleep(1.5)
                os.system('cls')
        
        if input_==3:
            if logincondition==True:
                tag_name=input("\nHashtag name: ")
                amount=int(input("Amount: "))
                while True:
                    try:
                        visible=input("Visible who you comment (y/n): ")
                        if visible=='y' or visible=='Y':
                            visible_follower=True
                            break
                        if visible=='n' or visible=='N':
                            visible_follower=False
                            break
                    except NameError:
                        pass
                print('___________________________________\n')
                print(colored('Try to following...', 'cyan'))
                follow_by_tag(tag_name=tag_name, amount=amount)
                time.sleep(2.5)
                os.system('cls')
            else:
                print(colored('Error! First you must be login (press 1)', 'red'))
                time.sleep(1.5)
                os.system('cls')
        
        if input_==4:
            if logincondition==True:
                tag_name=input("\nHashtag name: ")
                amount=int(input("Amount: "))
                comment=input('With what do you wont comment? ')
                while True:
                    try:
                        visible=input("Visible who you following (y/n): ")
                        if visible=='y' or visible=='Y':
                            visible_follower=True
                            break
                        if visible=='n' or visible=='N':
                            visible_follower=False
                            break
                    except NameError:
                        pass
                print('___________________________________\n')
                print(colored('Try to comment...', 'cyan'))
                comment_by_tag(tag_name=tag_name, amount=amount, comment=comment)
                time.sleep(2.5)
                os.system('cls')
            else:
                print(colored('Error! First you must be login (press 1)', 'red'))
                time.sleep(1.5)
                os.system('cls')
            
        if input_==5:
            if logincondition==True:
                tag_name=input("\nHashtag name: ")
                print('___________________________________\n')
                print('Starting function...')
                increase_followers(tag_name=tag_name)
                time.sleep(1.5)
                os.system('cls')
            else:
                print(colored('Error! First you must be login (press 1)', 'red'))
                time.sleep(1.5)
                os.system('cls')
        
        if input_==6:
            if logincondition==True:
                print('___________________________________\n')
                print('Starting function...')
                open_instagram(username=username, password=password)
                time.sleep(1.5)
                os.system('cls')
            else:
                print(colored('Error! First you must be login (press 1)', 'red'))
                time.sleep(1.5)
                os.system('cls')
        
        if input_==7:
            if logincondition==True:
                print('___________________________________\n')
                print('Unfollowing...')
                unfollower()
                time.sleep(1.5)
                os.system('cls')
            else:
                print(colored('Error! First you must be login (press 1)', 'red'))
                time.sleep(1.5)
                os.system('cls')
        
        if input_==8:
            if logincondition==True:
                print('___________________________________\n')
                print('Try to log out...')
                log_out()
                time.sleep(1.5)
                os.system('cls')
            else:
                print(colored('Error! First you must be login (press 1)', 'red'))
                time.sleep(1.5)
                os.system('cls')
        
        if input_==9:
            print('___________________________________\n')
            try:
                exitout()
                break
            except:
                print('Wait a moment...')
                time.sleep(1.5)
                os.system('cls')
            
    except ValueError:
        print(colored('Command not found', 'red'))
        time.sleep(0.3)
        os.system('cls')
