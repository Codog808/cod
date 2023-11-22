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


def shorter_EC(driver_wait, locator, indentier):
    return driver_wait.until(EC.visibility_of_element_located((locator, indentier)))


def auth(chrome_driver, wait):
    print("completing auth...")
    print("adding user information...")
    with open("keys.txt") as f:
        username, password = f.read().strip().split("\n")[1].split(" ")
        print("inputing user information...")
        wait.until(EC.visibility_of_element_located((By.NAME, "username"))).send_keys(username)
        wait.until(EC.visibility_of_element_located((By.NAME, "password"))).send_keys(password)
        wait.until(EC.visibility_of_element_located((By.NAME, "submit"))).click()
        try:
            iframe_xpath = '//*[@id="duo_iframe"]'
            iframe_check_wait = shorter_EC(wait, By.XPATH, iframe_xpath)
            chrome_driver.switch_to.frame(iframe_check_wait)
            checkbox_xpath = '//*[@id="login-form"]/div[2]/div/label/input'
            checkbox_box = shorter_EC(wait, By.XPATH, checkbox_xpath)
            login_box_xpath = '//*[@id="passcode"]'
            login_box = shorter_EC(wait, By.XPATH, login_box_xpath)
            login_box.click()
            input_box = shorter_EC(wait, By.XPATH, "//input[@name='passcode']")
            if not checkbox_box.is_selected():
                checkbox_box.click()
            while True:
                try:
                    print("trying code auth...")
                    # input("\n\nadd some codes maybe?\n\n")
                    with open("codes.txt") as f:
                        codes = f.read().strip().split()
                        print(codes)
                        code = codes.pop()
                        if len(codes) <= 0:
                            with open("codes.txt", "w") as f:
                                less_codes = " ".join(codes)
                                f.write(less_codes)
                            raise ValueError("NO MORE CODES")
                        print(len(codes), "many codes are left...")                       
                        print(code)
                    input_box.send_keys(code)
                    login_box.click()
                    with open("codes.txt", "w") as f:
                        less_codes = " ".join(codes)
                        f.write(less_codes)
                    break
                except:
                    print("calling auth...")
                    print("please input more codes...")
                    text_me_xpath = '//*[@id="message"]'
                    text_me_box = shorter_EC(wait, By.XPATH, text_me_xpath)
                    text_me_box.click()
                    # input("press enter after you get more codes...")
                    # There was a goddamn iframe
                    # iframe = chrome_driver.find_element(By.XPATH, "//iframe[@id='duo-iframe']")
                    # input("what the......")
                    time.sleep(6)
                    call_me_button_xpath = '//*[@id="auth_methods"]/fieldset/div[2]/button'
                    call_me_button = wait.until(EC.visibility_of_element_located((By.XPATH, call_me_button_xpath)))
                    call_me_button.click()
                    break
        except:
            pass

def uh_gmail(chrome_driver, wait):
    """ function to solve the html movements for gmail. """
    # Instructions
    print("opening gmail.com...")
    chrome_driver.get("https://gmail.com/")
    print("adding user information...")
    with open("keys.txt") as f:
        username, _ = f.read().strip().split("\n")[0].split(" ")
        email_box = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@type='email']"))) 
        email_box.send_keys(username)
        # input("finding jsname")
        next_button_xpath = '//*[@id="identifierNext"]/div/button'
        next_button = wait.until(EC.visibility_of_element_located((By.XPATH, next_button_xpath)))
        next_button.click()
    auth(chrome_driver, wait)
    chrome_driver.switch_to.window(chrome_driver.window_handles[0])
    continue_box_xpath = '//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button'
    continue_box = shorter_EC(wait, By.XPATH, continue_box_xpath)
    continue_box.click()

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
                site_links_box = shorter_EC(wait, By.XPATH, site_links_xpath)
            except:
                print("exception is running, find a way to withhold deapreciated code.")
                site_links_xpath = '//*[@id="viewAllSites"]'
                site_links_box = shorter_EC(wait, By.XPATH, site_links_xpath)
            site_links_box.click()
            for i in range(1, links_range + 1):
                link_xpath = f'//*[@id="otherSitesCategorWrap"]/div[4]/div/ul/li[{i}]/div/a'
                link_box = shorter_EC(wait, By.XPATH, link_xpath)
                actions = ActionChains(chrome_driver)
                actions.key_down(Keys.CONTROL).click(link_box).key_up(Keys.CONTROL).perform()
            break
        except:
            input("There are pop ups...")


def chrome_driver_init(exe_path=""):
    print("setting up settings...")
    if exe_path=="":
        service = ChromeService(ChromeDriverManager().install())
    else:
        service = ChromeService(executable_path=exe_path)
    options = ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging", "enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    # doesn't save cookies to log into other sites
    # options.add_argument("--incognito")
    options.add_argument("window-size=720,900")
    chrome_driver = webdriver.Chrome(service=service, options=options)
    wait = WebDriverWait(chrome_driver, 60)
    return chrome_driver, wait

def box(wait, xpath):
    return shorter_EC(wait, By.XPATH, xpath)

class Fall_2023:
    @classmethod
    def ENG_100(cls, chrome_driver, wait):
        return 0
    @classmethod
    def PHYL_141(cls, chrome_driver, wait):
        ul_li_a_menu_xpath = '//*[@id="skipNav"]/ul/li[3]/a[1]'
        ul_li_a_menu_box = shorter_EC(wait, By.XPATH, ul_li_a_menu_xpath)
        ul_li_a_menu_box.click()
        ul_li_a_xpath = '//*[@id="toolMenu"]/ul'
        ul_li_a_box = shorter_EC(wait, By.XPATH, ul_li_a_xpath)
        print("opening PHYL_141 set up...")
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
        return 1
    @classmethod
    def ITS_227(cls, chrome_driver, wait):
        """Will be on the link itself."""
        ul_li_a_menu_xpath = '//*[@id="skipNav"]/ul/li[3]/a[1]'
        ul_li_a_menu_box = shorter_EC(wait, By.XPATH, ul_li_a_menu_xpath)
        ul_li_a_menu_box.click()
        zybooks_xpath = '//*[@id="toolMenu"]/ul/li[2]/a'
        zybooks_box = shorter_EC(wait, By.XPATH, zybooks_xpath)
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
        sign_in_box_xpath = '//*[@id="ember7"]/div/div[3]/button'
        sign_in_box = box(wait, sign_in_box_xpath)
        sign_in_box.click()
        # to open a window without being in it...
        # action = ActionChains(chrome_driver)
        # action.key_down(Keys.CONTROL).click(zybooks_box).key_up(Keys.CONTROL).perform()
        return 1
    @classmethod
    def ITS_122(cls, chrome_driver, wait):
        ul_li_a_menu_xpath = '//*[@id="skipNav"]/ul/li[3]/a[1]'
        ul_li_a_menu_box = shorter_EC(wait, By.XPATH, ul_li_a_menu_xpath)
        ul_li_a_menu_box.click()
        ul_li_a_xpath = '//*[@id="toolMenu"]/ul'
        ul_li_a_box = shorter_EC(wait, By.XPATH, ul_li_a_xpath)
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
    @classmethod
    def MATH_103(cls, chrome_driver, wait):
        """ similar to ITS_227 """
        ul_li_a_menu_xpath = '//*[@id="skipNav"]/ul/li[3]/a[1]'
        ul_li_a_menu_box = shorter_EC(wait, By.XPATH, ul_li_a_menu_xpath)
        ul_li_a_menu_box.click()
        vitalsource_UH = '//*[@id="toolMenu"]/ul'
        ul_li_a_box = shorter_EC(wait, By.XPATH, vitalsource_UH)
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
        courseware_box_xpath = '//*[@id="react-tabs-25"]/div/div[4]/div[2]/div/div/a'
        courseware_box = box(wait, courseware_box_xpath)
        courseware_box.click()
        # slow connection to Pearson's server...
        # input("PEARSONS ISSUE")
        chrome_driver.switch_to.window(chrome_driver.window_handles[-1])
        body_x = '/html/body'
        body = box(wait, body_x)
        body.click()
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
        # time.sleep(3)
        # input("assignment box")
        time.sleep(9)
        chrome_driver.switch_to.window(chrome_driver.window_handles[-1])
        body = box(wait, body_x)
        body.click()
        input("check the there is something weird here.")
        assignments_box_xpath = '//*[@id="ov_leftnav"]/div[2]/div[2]/div/div/div/a'
        assignments_box = box(wait, assignments_box_xpath)
        assignments_box.click()
        return 1

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



def main():
    # Initalization
    chrome_driver, wait = chrome_driver_init()
    uh_gmail(chrome_driver, wait)
    # iterate through the tabs [and identify which tab is what, maybe.
    laulima(chrome_driver, wait, 5)
    opening_class_resources(chrome_driver, wait)
    input("Press Enter to Quit...")
    chrome_driver.quit()
    print("success")

if __name__ == "__main__":
    main()
