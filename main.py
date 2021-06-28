import time
from plyer import notification

if __name__ == '__main__':
    while True:
        notification.notify(
            title = " Drink Water Now",
            message = "For men: 15.5 cups(3.7 litres), For women: 11.5 cups(2.7 lites) per days",
            app_icon = "E:\LAB\Python\Desktop_notification\Cup.ico",
            timeout =12
        )
        #time.sleep(6)
        time.sleep(60*60)