import pyautogui
import datetime
import time


def click_at_scheduled_time(
    target_x, target_y, target_hour, target_minute, target_second
):
    while True:
        now = datetime.datetime.now()
        mouse_x, mouse_y = pyautogui.position()

        print(f"현재 시간: {now.hour}시 {now.minute}분 {now.second}초")
        print(f"타겟 시간: {target_hour}시 {target_minute}분 {target_second}초")
        print(f"현재 마우스 위치: X={mouse_x}, Y={mouse_y}")
        print("*" * 100)

        if (
            now.hour == target_hour
            and now.minute == target_minute
            and now.second == target_second
        ):
            # pyautogui.click(x=target_x, y=target_y, button='left')

            pyautogui.click(x=mouse_x, y=mouse_y, button="left")
            time.sleep(1)  #
            pyautogui.click(x=mouse_x, y=mouse_y, button="left")

            break
        time.sleep(1)  # 매 초마다 체크


# 클릭할 위치의 좌표 (100px, 100px)
target_x = 1000
target_y = 1000

# 클릭할 시간 설정
# target_hour = int(input("원하는 클릭 시간(시): "))
# target_minute = int(input("원하는 클릭 시간(분): "))
# target_second = int(input("원하는 클릭 시간(초): "))

target___hour = int(20)
target_minute = int(00)
target_second = int(00)

click_at_scheduled_time(target_x, target_y, target___hour, target_minute, target_second)
