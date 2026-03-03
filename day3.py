def blood_moon(time):
  # get the hours and minutes
  hours = int(time[:2])
  mins = int(time[3:])

  # create a times list:
  times = []

  # calculate the three next times:
  for i in range(3):
    #add 48 min and check if it went over--> use % to get its new minute and add one to hours:
    updated_min = mins +48
    if updated_min >=60:
      updated_min = updated_min%60
      hours +=1
    # add 2 hours and check if it went over --> use % to get its new hour
    hours +=2
    if hours >=24:
      hours = hours%24
    
    # for string formatting of hours and mins if under 10:
    if (hours <10):
      str_hours = '0'+ str(hours)
    else:
      str_hours = str(hours)

    if (updated_min <10):
      str_min = '0'+ str(updated_min)
    else:
      str_min = str(updated_min)

    # now that its formatted for both hours and min, add to list
    new_time = f"{str_hours}:{str_min}"
    times.append(new_time)

    mins= updated_min
  #return the three moon times
  return times

#test inputs:
# print(blood_moon("01:00"))
# print(blood_moon("22:30"))
    


