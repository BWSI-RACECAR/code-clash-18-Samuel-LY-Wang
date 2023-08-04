"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2023

Code Clash #18 - Talking Clock (talkingclock.py)


Author: Andrew Scott White

Difficulty Level: 8/10

Prompt: I don’t want to be late for the BWSI Grand Prix, so I want
to program my phone to update me on the time. Can you help me make 
a Talking Clock? I need a script that takes an input 24-hour time 
(00:00 - 23:59) and translates it into words. Please format the input 
as ‘##:##’ and include am/pm in the output string. Thanks!

Test Cases:
Input: 12:00  Output: It's twelve pm

Input: 23:59  Output: It's eleven fifty nine pm

Input: 12:05  Output: It's twelve oh five pm
"""

teens = {11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"}

nonteens = {0: "", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 20: "twenty", 30: "thirty", 40: "fourty", 50: "fifty"}

def toString(num, isminute):
  if num == 0:
    return ""
  if num<20 and num>10:
    return teens[num]
  elif (num<10 and num != 0) and isminute:
    return "oh "+nonteens[num]
  else:
    return nonteens[num-num%10]+" "+nonteens[num%10]
    # This will convert military hours to regular hours, and determine AM vs PM
class Solution:    
    def ClockTalker(self, input_time):
      hour=10*int(input_time[0])+int(input_time[1])
      minute=10*int(input_time[3])+int(input_time[4])
      ispm=hour>=12
      if hour>12:
        hour -= 12
      elif hour == 0:
        hour += 12
      string="am"
      if ispm:
        string="pm"
      # print(hour)
      # print(minute)
      # print(ispm)
      if minute == 0:
        return ("It's "+toString(hour, False)+" "+string)
      if hour < 10:
        return ("It's"+toString(hour, False)+" "+toString(minute, True)+" "+string)
      return ("It's "+toString(hour, False)+" "+toString(minute, True)+" "+string)

def main():
     str1=input()
     tc1= Solution()
     ans=tc1.ClockTalker(str1)
     print(ans)
    
if __name__ == '__main__': 
    main()