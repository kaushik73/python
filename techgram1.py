# from gtts import gTTS
# from playsound import playsound
print("Text to audio converter")
# def play_audio(path):   
#     playsound(path)


# def convert_to_audio(text):
#     my_audio = gTTS(text)
#     my_audio.save('Alaram_Clock.mp3')
#     play_audio('Alaram_Clock.mp3')

# convert_to_audio(" Wake up Kaushik . It's time to do your work.")

# ---------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------

# import speech_recognition as sr
# r = sr.Recognizer()
# with sr.Microphone() as source:
#     """this is a program in which you can speak anything and it will convert it to test message"""
print("Audio to Text converter")
# print("I don't know why but this programwill take too much to execute :-")
#     print("Speak Anything :")
#     audio = r.listen(source)
#     try:
#         text = r.recognize_google(audio)
#         print("You said : {}".format(text))
#     except:
#         print("Sorry could not recognize what you said")
# ---------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------        
 


# import calendar
print("Calender Printer")
# yy = int(input("Enter Year : "))
# mm =  int(input("Enter Month :"))
# print("\n")
# print(calendar.month(yy, mm))



# ---------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------     


# import random
# # Initiating an while loop to keep the program executing
print("DICE ROLLER")
# while True:
#     print("Rolling Dice...")

#     # Using random.randint(1,6) to generate a random value between 1 & 6
#     print(f"The value is ", random.randint(1,6))

#     # Asking user to roll the dice again or quit 
#     repeat = input("Roll Dice again? 'y' for yes & 'n' for no: ")

#     # If the user answers negative the loop will break and program execution stops otherwise the program will continue executing 
#     if repeat == 'n':
#         break
# print("Thanks For Using our Dice Roller!")


# ---------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------     

print("Email Fetcher")
# email = input("Enter Your Email: ").strip() # .strip() is used to remove left and right spaces  

# username = email[:email.index('@')]
# domain = email[email.index('@') + 1:]

# print(f"Your username is {username} & domain is {domain}")





# # ---------------------------------------------------------------------------------------------
# # ---------------------------------------------------------------------------------------------
# #--------------------------------------------------------------------------------------------- 

# from datetime import datetime   #To set date and time
# from playsound import playsound     #To play sound
print(" ALARM CLOCK").strip()
# def validate_time(alarm_time):
#     if len(alarm_time) != 11:
#         return "Invalid time format! Please try again..."
#     else:
#         if int(alarm_time[0:2]) > 12:
#             return "Invalid HOUR format! Please try again..."
#         elif int(alarm_time[3:5]) > 59:
#             return "Invalid MINUTE format! Please try again..."
#         elif int(alarm_time[6:8]) > 59:
#             return "Invalid SECOND format! Please try again..."
#         else:
#             return "ok"

# while True:
#     alarm_time = input("Enter time in 'HH:MM:SS AM/PM' format: ")
    
#     validate = validate_time(alarm_time.lower())
#     if validate != "ok":
#         print(validate)
#     else:
#         print(f"Setting alarm for {alarm_time}...")
#         break

# alarm_hour = alarm_time[0:2]
# alarm_min = alarm_time[3:5]
# alarm_sec = alarm_time[6:8]
# alarm_period = alarm_time[9:].upper()

# while True:
#     now = datetime.now()

#     current_hour = now.strftime("%I")
#     current_min = now.strftime("%M")
#     current_sec = now.strftime("%S")
#     current_period = now.strftime("%p")

#     if alarm_period == current_period:
#         if alarm_hour == current_hour:
#             if alarm_min == current_min:
#                 if alarm_sec == current_sec:
#                     print("Wake Up!")
#                     playsound('F:\Python\Alaram_Clock.mp3')
#                     break


# ---------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------- 









# ---------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------- 









# ---------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------- 










# ---------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------- 








# ---------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------- 
