from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from reading import Phone_Numbers
from entries import driver_path,group_name

#path to webdriver
service = EdgeService(executable_path=driver_path)
options = Options()
driver = webdriver.Edge(service=service, options=options)

# opening whatsapp web browser
driver.get("https://web.whatsapp.com")

# waiting for 30seconds for scaning QR and opening whatsapp
print("Please scan the QR code and log in to WhatsApp Web.")
time.sleep(30)  # can change the login time based on preference

def add_to_group():
    # search tab clicking and entering groupname
    search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
    search_box.click()
    search_box.send_keys(group_name)
    time.sleep(3)
    
    # clicking on the group make  NB : sure group is created and groupname is correct
    try:
        group = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, f'//span[@title="{group_name}"]'))
    )
        group.click()
        print(f"Clicked on the group: {group_name}")

    except Exception as e:
        print(f"Failed to find or click on the group: {group_name}. Error: {e}")
        time.sleep(3)

    # Clicking on the group for going to menu
    menu_button = driver.find_element(By.XPATH, '//*[@id="main"]/header/div[2]/div[2]/span')
    menu_button.click()
    time.sleep(1)

    # Clicking on - add participant
    add_participant = driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[5]/span/div/span/div/div/div/section/div[6]/div[2]/div[1]/div[2]/div/div')
    add_participant.click()
    time.sleep(3)

    # searching for each contact and selecting them
    for contact in Phone_Numbers:
        search_contact_box = driver.find_element(By.XPATH,'//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/div/div/p')
        search_contact_box.send_keys(contact)
        time.sleep(2)

        contact_to_add = driver.find_element(By.XPATH,'//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[2]')
        contact_to_add.click()
        time.sleep(1)

    # Clicking on the tick mark
    confirm_button = driver.find_element(By.XPATH,'//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div/span[2]/div/div/div/span')
    confirm_button.click()
    time.sleep(3)

    # clicking on the reconform add members
    re_confirm_button=driver.find_element(By.XPATH,'//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[2]/div/button[2]/div/div')
    re_confirm_button.click()
    time.sleep(3)


# calling the function
add_to_group()
print("All were added to groups")

# closing the browser
driver.quit()
