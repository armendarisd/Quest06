import datetime

''' This is the main funtion '''
def my_data_transform(param_1):
  array = param_1.split('\n')
  index = 1

  while(index < len(array)-1):
    array[index] = change_my_age(array[index])
    array[index] = change_my_timezone(array[index])
    array[index] = change_my_email(array[index])
    index += 1
  
  array.pop(len(array)-1)
  
  return array
  
''' This transform the age '''
def change_my_age(param_1):
    array = param_1.split(',') 
  
    if(int(array[5]) >= 1 and int(array[5]) <= 20 ):
      array[5] = "1->20"
    elif(int(array[5]) >= 21 and int(array[5]) <= 40 ):
      array[5] = "21->40"
    elif(int(array[5]) >= 41 and int(array[5]) <= 65 ):
      array[5] = "41->65"
    elif(int(array[5]) >= 66 and int(array[5]) <= 99 ):
      array[5] = "66->99"
    
    array1 = ','.join(array)
  
    return array1

''' This transform the timezone'''
def change_my_timezone(param_1):
    array = param_1.split(',')
  
    date_time_obj = datetime.datetime.strptime(array[9], '%Y-%m-%d %H:%M:%S')
  
    if(date_time_obj.hour >= 6 and date_time_obj.hour < 12):
      array[9] = "morning"
      
    elif(date_time_obj.hour >= 12 and date_time_obj.hour < 18):
      array[9] = "afternoon"
      
    elif(date_time_obj.hour >= 18 and date_time_obj.hour < 24):
      array[9] = "evening"
  
    array1 = ','.join(array)
    return array1
    
''' This transform the email'''
def change_my_email(param_1):
  array = param_1.split(',')
  
  temp_array = array[4].split('@')
  array[4] = temp_array[1]
  
  array1 = ','.join(array)
  return array1




  