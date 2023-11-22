from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import sys, time
from cchrome import cchrome, shorter_EC, box

# user profile can be saved.
class log_on:
    def __init__(s, webdriver, wait, keys="keys.txt", codes="codes.txt"):
        s.wd = webdriver
        s.w = wait
        s.keys_file = keys
        s.code_file = codes
        try:
            with open(s.keys_file) as f:
                s.username, s.password = f.readlines()[1].strip().split()
        except FileNotFoundError:
            string0 = "There is no keys.txt..."
            string = "# Creating keys.txt... #"
            print("#" * len(string0), string0, "#" * len(string0))
            print("#" * len(string), string, "#" * len(string))
            with open(s.keys_file, 'w') as f:
                username = input("School Username, Type Here and Press Enter: ")
                password = input("School Password, Type Here and Press Enter")
                f.write(f'{username} {password}')
    def auth(s):
        print("Authentificaiton...")
        try:
            use = box(s.w, "username", By.NAME)
            pas = box(s.w, "password", By.NAME)
            print(use.get_attribute("value"))
            if not (use.get_attribute("value") == "" and pas.get_attribute("value") == ""):
                pas.send_keys(s.password)
                use.send_keys(s.username)
            # sometimes it clicks way too fast
            time.sleep(3)
            box(s.w, "submit", By.NAME).click()
            duo_iframe = box(s.w, '//*[@id="duo_iframe"]')
            s.wd.switch_to.frame(duo_iframe)
            duo_login = box(s.w, '//*[@id="passcode"]')
            duo_login.click()
            duo_checkbox = box(s.w, '//*[@id="login-form"]/div[2]/div/label/input')
            if not duo_checkbox.is_selected():
                duo_checkbox.click()
            while True:
                try:
                    print("Code Version...")
                    with open(s.code_file) as f:
                        raw_codes = f.read().strip().split()
                        codes = [code for code in raw_codes if code != ""]
                        code = codes.pop()
                    with open(s.code_file, "w") as f:
                        f.write(" ".join(codes))
                    if not (len(codes) == 0):
                        print(len(codes), " Are Left")
                        box(s.w, '//*[@id="auth_methods"]/fieldset/div[3]/div/input').send_keys(code)
                        duo_login.click()
                        break
                    else:
                        raise ValueError("NO MORE CODES....")
                except:
                    print("Calling Version...")
                    box(s.w, '//*[@id="message"]').click()
                    box(s.w, '//*[@id="auth_methods"]/fieldset/div[2]/button').click()
        except Exception as e:
            print("error", e)
    
    def gmail(s):
        print("Gmail...")
        s.wd.get("https://gmail.com")
        try:
            with open(s.keys_file) as f:
                username, _ = f.read().strip().split("\n")[0].split(" ")
                box(s.w, '//input[@type="email"]').send_keys(username)
                box(s.w, '//*[@id="identifierNext"]/div/button').click()
                s.auth()
                s.wd.switch_to.window(s.wd.window_handles[0])
                box(s.w, '//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button').click()
        except Exception as e:
            print(e)

    def laulima(s, amount_of_classes):
        print("Laulima...")
        s.wd.execute_script(f"window.open('https://authn.hawaii.edu/cas/login?service=https%3A%2F%2Flaulima.hawaii.edu%2Fsakai-login-tool%2Fcontainer&renew=true', '_blank')")
        s.wd.switch_to.window(s.wd.window_handles[-1])
        s.auth()
        while True:
            try:
                s.wd.switch_to.window(s.wd.window_handles[-1])
                try:
                    box(s.w, '//*[@id="more-sites-menu"]').click()
                except:
                    box(s.w, '//*[@id="viewAllSites"]').click()
                for i in range(1, amount_of_classes + 1):
                    link_xpath = f'//*[@id="otherSitesCategorWrap"]/div[4]/div/ul/li[{i}]/div/a'
                    link = box(s.w, link_xpath)
                    actions = ActionChains(s.wd)
                    actions.key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL).perform()
                break
            except Exception as e:
                input(f"{e} There are pop ups...")

    # ERROR WITH THE TABS AND CALLING THE FUNCTION.
    def opening_classes(s):
        print("oepning classes")
        # The title of the classes for KCC are a different, must be subsitited to get the function name of the class season.
        class_parts = {
                    "ENG-100-0": "ENG_100",
                    "ITS-227-0": "ITS_227",
                    "ITS-122": "ITS_122",
                    "MATH-103-0": "MATH_103",
                    "PHYL-141-0": "PHYL_141"
                }
        tabs = []
        for i in range(len(s.wd.window_handles)):
            s.wd.switch_to.window(s.wd.window_handles[i])
            title = str(s.wd.title)
            print(title)
            identify_tab = title.split(" ")
            for part in identify_tab:
                for key in class_parts:
                    if key in part:
                        tabs.append((i, title, class_parts[key]))
            # (tabs.append(tuple((i, title, class_parts[key]))) for key in class_parts for title in str(s.wd.title).split() if key in title)
            print(tabs)
        for tab in tabs:
            index, _, class_name = tab
            # index, title, class_name = tab
            s.wd.switch_to.window(s.wd.window_handles[index])
            getattr(Fall_2023, class_name)(s.wd, s.w)
        # print(tabs)
        print("\nall assignments premade are open...")
        s.wd.switch_to.window(s.wd.window_handles[0])
    
    def star(s):
        print("opening star")
        s.wd.execute_script(f"window.open('https://www.star.hawaii.edu/studentinterface/', '_blank');")
        s.wd.switch_to.window(s.wd.window_handles[-1])
        try:
            box(s.w, '//*[@id="casEnterLogin"]').click()
            with open(s.keys_file) as f:
                username, password = f.read().split("\n")[1].split(" ")
                box(s.w, '//*[@id="username"]').send_keys(username)
                box(s.w, '//*[@id="password"]').send_keys(password)
                box(s.w, '//*[@id="fm1"]/div/button').click()
            # auth(chrome_driver, wait)
        except Exception as e:
            print(e)
            input("it didn't work")
        s.wd.switch_to.window(s.wd.window_handles[0])



            

        
def auth(chrome_driver, wait):
    print("auth...")
    iframe_xpath = '//*[@id="duo_iframe"]'
    checkbox_xpath = '//*[@id="login-form"]/div[2]/div/label/input'
    login_box_xpath = '//*[@id="passcode"]'

    input_box_xpath = '//*[@id="auth_methods"]/fieldset/div[3]/div/input'
    text_me_xpath = '//*[@id="message"]'
    call_me_button_xpath = '//*[@id="auth_methods"]/fieldset/div[2]/button'
    # print("adding user information...")
    with open("keys.txt") as f:
        username, password = f.read().strip().split("\n")[1].split(" ")
        # print("inputing user information...")
        shorter_EC(wait, "username", By.NAME).send_keys(username)
        shorter_EC(wait, "password", By.NAME).send_keys(password)
        time.sleep(3)
        shorter_EC(wait, "submit", By.NAME).click()
        try:
            iframe_check_wait = shorter_EC(wait, iframe_xpath)
            chrome_driver.switch_to.frame(iframe_check_wait)
            checkbox_box = shorter_EC(wait, checkbox_xpath)
            login_box = shorter_EC(wait, login_box_xpath)
            login_box.click()
            if not checkbox_box.is_selected():
                checkbox_box.click()
            while True:
                try:
                    print("trying code auth...")
                    with open("codes.txt") as f:
                        codes = f.read().strip().split()
                        # print(codes)
                        codes = [x for x in codes if x != ""]
                        code = codes.pop()
                    with open("codes.txt", "w") as f:
                        if codes == []:
                            f.write("")
                        else:
                            less_codes = " ".join(codes)
                            f.write(less_codes)
                    if len(codes) == 0:
                        raise ValueError("NO MORE CODES")
                    print(len(codes), "many codes are left...")
                    # print(code)
                    input_box = shorter_EC(wait, input_box_xpath) 
                    input_box.send_keys(code)
                    login_box.click()
                    break
                except:
                    print("calling auth...")
                    # print("please input more codes...")
                    text_me_box = shorter_EC(wait, text_me_xpath)
                    text_me_box.click()
                    shorter_EC(wait, call_me_button_xpath).click()
                    break
        except:
            pass

def uh_gmail(chrome_driver, wait):
    """ function to solve the html movements for gmail. """
    print("entering gmail.com")
    email_box_xpath = '//input[@type="email"]'
    next_button_xpath = '//*[@id="identifierNext"]/div/button'
    chrome_driver.get("https://gmail.com/")
    continue_box_xpath = '//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button'
    # print("adding user information...")
    with open("keys.txt") as f:
        username, _ = f.read().strip().split("\n")[0].split(" ")
        shorter_EC(wait, email_box_xpath).send_keys(username)
        shorter_EC(wait, next_button_xpath).click()
    auth(chrome_driver, wait)
    chrome_driver.switch_to.window(chrome_driver.window_handles[0])
    shorter_EC(wait, continue_box_xpath).click()

def laulima(chrome_driver, wait, links_range):
    """ function to open class links in laulima """
    print("entering Laulima")
    lualima_url = "https://authn.hawaii.edu/cas/login?service=https%3A%2F%2Flaulima.hawaii.edu%2Fsakai-login-tool%2Fcontainer&renew=true"
    chrome_driver.execute_script(f"window.open('{lualima_url}', '_blank');")
    chrome_driver.switch_to.window(chrome_driver.window_handles[-1])
    auth(chrome_driver, wait)
    print("working in laulima...")
    while True:
        try:
            chrome_driver.switch_to.window(chrome_driver.window_handles[-1])
            try:
                site_links_xpath = '//*[@id="more-sites-menu"]'
                site_links_box = shorter_EC(wait, site_links_xpath)
            except:
                print("exception is running, find a way to withhold deapreciated code.")
                site_links_xpath = '//*[@id="viewAllSites"]'
                site_links_box = shorter_EC(wait, site_links_xpath)
            site_links_box.click()
            for i in range(1, links_range + 1):
                link_xpath = f'//*[@id="otherSitesCategorWrap"]/div[4]/div/ul/li[{i}]/div/a'
                link_box = shorter_EC(wait, link_xpath)
                actions = ActionChains(chrome_driver)
                actions.key_down(Keys.CONTROL).click(link_box).key_up(Keys.CONTROL).perform()
            break
        except:
            input("There are pop ups...")


class Fall_2023:
    @classmethod
    def ENG_100(cls, chrome_driver, wait):
        print("ENG_100")
        doc_link = "https://www.docs.google.com"
        chrome_driver.execute_script(f"window.open('{doc_link}', '_blank');")
        return 0
    @classmethod
    def PHYL_141(cls, chrome_driver, wait):
        try:
            ul_li_a_menu_xpath = '//*[@id="skipNav"]/ul/li[3]/a[1]'
            ul_li_a_menu_box = shorter_EC(wait, ul_li_a_menu_xpath)
            ul_li_a_menu_box.click()
            ul_li_a_xpath = '//*[@id="toolMenu"]/ul'
            ul_li_a_box = shorter_EC(wait, ul_li_a_xpath)
            print("opening ITS_122 set up...")
            li_a_boxes = ul_li_a_box.find_elements(By.TAG_NAME, "li")
            li_and_a = []
            for li in li_a_boxes:
                # if li has Week in its title
                a_box = li.find_elements(By.TAG_NAME, "a")
                for a_tag in a_box:
                    if 'Week' in a_tag.get_attribute('title'):
                        create_tuple = (li, a_tag)
                        li_and_a.append(create_tuple)
                        # print(li_and_a[-1][-1])
                        # a_tag.click()
                        break
            # always the last, or latest, week is at the end.
            time.sleep(3)
            li_and_a[-1][-1].click()
        except Exception as e:
            print("error in phul_141", e)
    @classmethod
    def ITS_227(cls, chrome_driver, wait):
        """Will be on the link itself."""
        try:
            ul_li_a_menu_xpath = '//*[@id="skipNav"]/ul/li[3]/a[1]'
            ul_li_a_menu_box = shorter_EC(wait, ul_li_a_menu_xpath)
            ul_li_a_menu_box.click()
            zybooks_xpath = '//*[@id="toolMenu"]/ul/li[2]/a'
            zybooks_box = shorter_EC(wait, zybooks_xpath)
            print("Opening ITS_227 assignments...")
            zybooks_box.click()
            with open("keys.txt") as f:
                email, password = f.read().strip().split("\n")[0].split(" ")
            # weird selenium error where I need to move to the newly opened window.
            # input("double check the iframe")
            chrome_driver.switch_to.window(chrome_driver.window_handles[-1])
            # iframe_box_xpath = '/html/body/iframe'
            # iframe_box = box(wait, iframe_box_xpath)
            # chrome_driver.switch_to.frame(iframe_box)
            email_box_xpath = '//input[@type="email"]'
            email_box = box(wait, email_box_xpath)
            email_box.send_keys(email)
            email_box.click()
            password_box_xpath = '//input[@type="password"]'
            password_box = box(wait, password_box_xpath)
            password_box.send_keys(password)
            password_box.click()
            try:
                sign_in_box_xpath = '//*[@id="ember7"]/div/div[3]/button'
                sign_in_box = box(wait, sign_in_box_xpath)
                sign_in_box.click()
            except:
                sign_in_box_xpath = '//*[@id="ember6"]/div/div[3]/button'
                sign_in_box = box(wait, sign_in_box_xpath)
                sign_in_box.click()
            # input("did it work?")
            # to open a window without being in it...
            # action = ActionChains(chrome_driver)
            # action.key_down(Keys.CONTROL).click(zybooks_box).key_up(Keys.CONTROL).perform()
            return 1
        except:
            print("error in ITS 227")
    @classmethod
    def ITS_122(cls, chrome_driver, wait):
        try:
            ul_li_a_menu_xpath = '//*[@id="skipNav"]/ul/li[3]/a[1]'
            ul_li_a_menu_box = shorter_EC(wait, ul_li_a_menu_xpath)
            ul_li_a_menu_box.click()
            ul_li_a_xpath = '//*[@id="toolMenu"]/ul'
            ul_li_a_box = shorter_EC(wait, ul_li_a_xpath)
            print("opening ITS_122 set up...")
            li_a_boxes = ul_li_a_box.find_elements(By.TAG_NAME, "li")
            li_and_a = []
            for li in li_a_boxes:
                # if li has Week in its title
                a_box = li.find_elements(By.TAG_NAME, "a")
                for a_tag in a_box:
                    if 'infosecLearning' in a_tag.get_attribute('title'):
                        input(" found the inforsecLearning tag")
                        action = ActionChains(chrome_driver)
                        action.key_down(Keys.CONTROL).click(a_tag).key_up(Keys.CONTROL).perform()

                    if 'Week' in a_tag.get_attribute('title'):
                        create_tuple = (li, a_tag)
                        li_and_a.append(create_tuple)
                        # print(li_and_a[-1][-1])
                        # a_tag.click()
                        break
            # always the last, or latest, week is at the end.
            time.sleep(3)
            li_and_a[-1][-1].click()
            return 1
        except:
            print("error in ITS 122")
    @classmethod
    def MATH_103(cls, chrome_driver, wait):
        """ similar to ITS_227 """
        try:
            ul_li_a_menu_xpath = '//*[@id="skipNav"]/ul/li[3]/a[1]'
            ul_li_a_menu_box = shorter_EC(wait, ul_li_a_menu_xpath)
            ul_li_a_menu_box.click()
            vitalsource_UH = '//*[@id="toolMenu"]/ul'
            ul_li_a_box = shorter_EC(wait, vitalsource_UH)
            print("opening MATH_103 set up...")
            li_a_boxes = ul_li_a_box.find_elements(By.TAG_NAME, "li")
            li_and_a = []
            for li in li_a_boxes:
                # if li has Week in its title
                a_box = li.find_elements(By.TAG_NAME, "a")
                for a_tag in a_box:
                    if 'VitalSource' in a_tag.get_attribute('title'):
                        create_tuple = (li, a_tag)
                        li_and_a.append(create_tuple)
            # always the last, or latest, week is at the end.
            li_and_a[-1][-1].click()
            chrome_driver.switch_to.window(chrome_driver.window_handles[-1])
            # input("check courseware box")
            time.sleep(5)
            courseware_box_xpath = '//*[@id="react-tabs-25"]/div/div[4]/div[2]/div/div/a'
            courseware_box = box(wait, courseware_box_xpath)

            courseware_box.click()
            time.sleep(3)
            chrome_driver.switch_to.window(chrome_driver.window_handles[-2])
            chrome_driver.close()
            # slow connection to Pearson's server...
            # input("PEARSONS ISSUE")
            chrome_driver.switch_to.window(chrome_driver.window_handles[-1])
            time.sleep(9)
            # body_x = '/html/body'
            # body = box(wait, body_x)
            # body.click()
            # whether it is mobile or web depends on the size of the window.
            try:
                pearsons_box_xpath = '//*[@id="mobileBtnOpenMLM"]'
                pearsons_box = box(wait, pearsons_box_xpath)
                # print("found the mobile version")
            except:
                pearsons_box_xpath = '//button[@href="javascript:void(0)"]'
                pearsons_box = box(wait, pearsons_box_xpath)
                # print("found the web version")
            pearsons_box.click()
            time.sleep(3)
            chrome_driver.switch_to.window(chrome_driver.window_handles[-2])
            chrome_driver.close()
            # time.sleep(3)
            # input("assignment box")
            time.sleep(9)
            chrome_driver.switch_to.window(chrome_driver.window_handles[-1])
            assignments_box_xpath = '//*[@id="ov_leftnav"]/div[2]/div[2]/div/div/div/a'
            assignments_box = box(wait, assignments_box_xpath)
            assignments_box.click()
            return 1
        except Exception as e:
            print("error in math", e)

def opening_class_resources(chrome_driver, wait):
    print("working in the classes")
    class_parts = {
                "ENG-100-0": "ENG_100",
                "ITS-227-0": "ITS_227",
                "ITS-122": "ITS_122",
                "MATH-103-0": "MATH_103",
                "PHYL-141-0": "PHYL_141"
            }
    tabs = []
    for i in range(len(chrome_driver.window_handles)):
        chrome_driver.switch_to.window(chrome_driver.window_handles[i])
        title = str(chrome_driver.title)
        # print(title)
        identify_tab = title.split(" ")
        for part in identify_tab:
            for key in class_parts:
                if key in part:
                    tabs.append((i, title, class_parts[key]))
    for tab in tabs:
        index, title, class_name = tab
        chrome_driver.switch_to.window(chrome_driver.window_handles[index])
        getattr(Fall_2023, class_name)(chrome_driver, wait)
    # print(tabs)
    print("\nall assignments premade are open...")
    chrome_driver.switch_to.window(chrome_driver.window_handles[0])

def stargps(chrome_driver, wait):
    print("opening stargps")
    star_link = "https://www.star.hawaii.edu/studentinterface/"
    chrome_driver.execute_script(f"window.open('{star_link}', '_blank');")
    chrome_driver.switch_to.window(chrome_driver.window_handles[-1])
    try:
        shorter_EC(wait, '//*[@id="casEnterLogin"]').click()
        with open("keys.txt") as f:
            username, password = f.read().split("\n")[1].split(" ")
            shorter_EC(wait, '//*[@id="username"]').send_keys(username)
            shorter_EC(wait, '//*[@id="password"]').send_keys(password)
            shorter_EC(wait, '//*[@id="fm1"]/div/button').click()
        # auth(chrome_driver, wait)
    except Exception as e:
        print(e)
        input("it didn't work")
    chrome_driver.switch_to.window(chrome_driver.window_handles[0])
    
def kapiolani_community_college_homepage(chrome_driver, wait):
    kcc_link = "https://www.kapiolani.hawaii.edu/"
    chrome_driver.execute_script(f"window.open('{kcc_link}', '_blank');")
    chrome_driver.switch_to.window(chrome_driver.window_handles[-1])


def kcc_library(chrome_driver, wait):
    kcc_library_link = "https://guides.library.kapiolani.hawaii.edu/home"
    chrome_driver.execute_script(f"window.open('{kcc_library_link}', '_blank');")
    chrome_driver.switch_to.window(chrome_driver.window_handles[0])

def main():
    # Initalization
    # chrome_driver, wait = chrome_driver_init()
    chrome_driver, wait = cchrome(r"C:\Users\shita\Projects\gitted\Selen\chromedriver118.exe", r"C:\Users\shita\appdata\local\chromium-118\application\chrome.exe", cody_user=False)
    # uh_gmail(chrome_driver, wait)
    # # iterate through the tabs [and identify which tab is what, maybe.
    # laulima(chrome_driver, wait, 5)
    # opening_class_resources(chrome_driver, wait)
    # stargps(chrome_driver, wait)
    # kcc_library(chrome_driver, wait)    
    # input("Press Enter to Quit...")
    steps = log_on(chrome_driver, wait, keys="jkeys.txt", codes="jcodes.txt")
    steps.gmail()
    # ERROR WITHIN LAULIMA
    steps.laulima(5)
    steps.star()
    kcc_library(chrome_driver, wait)
    input("PRESS ENTER TO END.")
    chrome_driver.quit()
    print("success")

if __name__ == "__main__":
    main()
