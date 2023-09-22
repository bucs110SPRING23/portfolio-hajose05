rate = float(input('what is the current exchange rate for euro to dollar? ')) 
amount = float(input('how much you trynna convert friend? '))
total = (rate)*(amount)  
print('-------------------------------') 
print('service charge = $3')
service_charge = float(3)  
result = total - service_charge 
print ('$',result)
