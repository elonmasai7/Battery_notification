import psutil

batery = psutil.sensors_battery()
plugged = batery.power_unplugged
percent = batery.percent

if percent ≤ 30 and plugged≠true:
  from pynotifier import Notification
  Notification(
    title = "Battery low"
    description=str(percent) + "% Battery remainin!!",
    duration=5, 
  ).send()
 ## https://github.com/elonmasai7## 
