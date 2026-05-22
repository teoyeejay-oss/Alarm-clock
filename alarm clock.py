import datetime
import time
import playsound

def set_alarm(alarm_time):
   print(f"Alarm set to {alarm_time}.")
   is_running = True
   sound_file= "music1.mp3"
   while is_running:
       current_time = datetime.datetime.now().strftime("%H:%M:%S")
       print(current_time)
       time.sleep(1)
       if current_time == alarm_time:
           print("Wake up!")
           playsound.playsound(sound_file)
           is_running = False

if __name__ =="__main__":
    alarm_time = input("Please set your alarm time(HH:MM:SS): ")
    set_alarm(alarm_time)

