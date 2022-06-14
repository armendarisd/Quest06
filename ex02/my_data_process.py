def my_data_process(param_1):
    index = 1
    dictionary = {"Gender":{"Male":0,"Female":0},"Email":{"yahoo.com":0,"hotmail.com":0},"Age":{"21->40":0,"66->99":0,"41->65":0},"City":{"Seattle":0,"Detroit":0,"Las Vegas":0,"Chicago":0},"Device":{"Safari iPhone":0,"Chrome Android":0,"Chrome":0},"Order At":{"afternoon":0,"morning":0}}

    while(index < len(param_1)):

        dictionary["Gender"]["Male"] = dictionary["Gender"]["Male"] + count_gender(param_1[index])[0] 
        dictionary["Gender"]["Female"] = dictionary["Gender"]["Female"] + count_gender(param_1[index])[1]

        dictionary["Email"]["yahoo.com"] = dictionary["Email"]["yahoo.com"] + count_email(param_1[index])[0] 
        dictionary["Email"]["hotmail.com"] = dictionary["Email"]["hotmail.com"] + count_email(param_1[index])[1]

        dictionary["Age"]["21->40"] = dictionary["Age"]["21->40"] + count_age(param_1[index])[0] 
        dictionary["Age"]["66->99"] = dictionary["Age"]["66->99"] + count_age(param_1[index])[1]
        dictionary["Age"]["41->65"] = dictionary["Age"]["41->65"] + count_age(param_1[index])[2] 

        dictionary["City"]["Seattle"] = dictionary["City"]["Seattle"] + count_city(param_1[index])[0] 
        dictionary["City"]["Detroit"] = dictionary["City"]["Detroit"] + count_city(param_1[index])[1]
        dictionary["City"]["Las Vegas"] = dictionary["City"]["Las Vegas"] + count_city(param_1[index])[2]
        dictionary["City"]["Chicago"] = dictionary["City"]["Chicago"] + count_city(param_1[index])[3]

        dictionary["Device"]["Safari iPhone"] = dictionary["Device"]["Safari iPhone"] + count_device(param_1[index])[0] 
        dictionary["Device"]["Chrome Android"] = dictionary["Device"]["Chrome Android"] + count_device(param_1[index])[1]
        dictionary["Device"]["Chrome"] = dictionary["Device"]["Chrome"] + count_device(param_1[index])[2] 

        dictionary["Order At"]["afternoon"] = dictionary["Order At"]["afternoon"] + count_orderAt(param_1[index])[0] 
        dictionary["Order At"]["morning"] = dictionary["Order At"]["morning"] + count_orderAt(param_1[index])[1]

        index += 1
    
    return str(dictionary).replace(", ", ",").replace(": ",":").replace("'", '"')
     



def count_gender(param_1):
  male_counter = 0
  female_counter = 0
  
  param_1 = param_1.split(',')

  if(param_1[0] == "Male"):
    male_counter += 1
  elif(param_1[0] == "Female"):
    female_counter += 1
    
  param_1 = ",".join(param_1)
 
  return male_counter, female_counter
def count_email(param_1):
  yahoo_counter = 0
  hotmail_counter = 0
  
  param_1 = param_1.split(',')

  if(param_1[4] == "yahoo.com"):
    yahoo_counter += 1
  elif(param_1[4] == "hotmail.com"):
    hotmail_counter += 1
    
  param_1 = ",".join(param_1)
 
  return  yahoo_counter, hotmail_counter
def count_age(param_1):

  group1 = 0
  group2 = 0
  group3 = 0
  
  param_1 = param_1.split(',')

  if(param_1[5] == "21->40"):
    group1 += 1
    
  elif(param_1[5] == "66->99"):
    group2 += 1
    
  elif(param_1[5] == "41->65"):
    group3 += 1
    
  param_1 = ",".join(param_1)
 
  return  group1, group2, group3
def count_city(param_1):
  seattle = 0
  detroit = 0
  las_vegas = 0
  chicago = 0
  
  param_1 = param_1.split(',')

  if(param_1[6] == "Seattle"):
    seattle += 1
    
  elif(param_1[6] == "Detroit"):
    detroit += 1
    
  elif(param_1[6] == "Las Vegas"):
    las_vegas += 1

  elif(param_1[6] == "Chicago"):
    chicago += 1
    
  param_1 = ",".join(param_1)
 
  return  seattle, detroit, las_vegas, chicago
def count_device(param_1):
  safari_iphone = 0
  chrome_android = 0
  chrome = 0
  
  param_1 = param_1.split(',')

  if(param_1[7] == "Safari iPhone"):
    safari_iphone += 1
    
  elif(param_1[7] == "Chrome Android"):
    chrome_android += 1

  elif(param_1[7] == "Chrome"):
    chrome += 1
    
  param_1 = ",".join(param_1)
 
  return  safari_iphone, chrome_android, chrome
def count_orderAt(param_1):
  afternoon = 0
  morning = 0
  
  param_1 = param_1.split(',')

  if(param_1[9] == "afternoon"):
    afternoon += 1
    
  elif(param_1[9] == "morning"):
    morning += 1
    
  param_1 = ",".join(param_1)
 
  return  afternoon, morning


