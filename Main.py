import time
import pyautogui as auto
import schedule, webbrowser
from twilio.rest import Client
import keys
def join():

    client = Client(keys.account_sid, keys.auth_token)

    message = client.messages.create(
    body="We have been successfully joined this class if u want kindly check it",
    from_=keys.twilio_number,
    to=keys.my_phone_number
    )
    
    print(message.body)
    time.sleep(10)

    webbrowser.open_new_tab('https://meet.google.com/pad-ztqi-aaz')
    time.sleep(10)

    auto.hotkey('ctrl', 'd')
    auto.hotkey('ctrl', 'e')

    auto.click(1365, 582)

    time.sleep(20)
    auto.hotkey('ctrl', 'w')

schedule.every().day.at("20:29").do(join)

while True:
    schedule.run_pending()
    time.sleep(1)


