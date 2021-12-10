#Max VO²
def calcularVo2Max(distancy,timeInMin,second):

 convertToSecond = timeInMin*60+second
 calculoVo2Max = distancy/convertToSecond*(60*0.2)+3.5

 return calculoVo2Max

#CalcularAge
def calcularAgeVo2(age,vo2MaxPorIdade):
    
 #Vo2 homem muito fraco
  if(age<=20 and age>=29):
    if(vo2MaxPorIdade<25):
     print("Vo² muito Fraco")
  if(age>=30 and age<=39):
    if(vo2MaxPorIdade<23):
     print("Vo² muito Fraco")
  if(age>=40 and age<=49):
    if(vo2MaxPorIdade<20):
     print("Vo² muito Fraco")
  if(age>=50 and age <=59):
    if(vo2MaxPorIdade<18):
     print("Vo² muito Fraco")
  if(age>=60 and age<=69):
    if(vo2MaxPorIdade<16):
     print("Vo² muito Fraco")

 #Vo2 homem fraco
  if(age>=20 and age<=29):
    if(vo2MaxPorIdade>=25 and vo2MaxPorIdade <=33):
     print("Vo² Fraco")
  if(age>=30 and age<=39):
    if(vo2MaxPorIdade<=23 and vo2MaxPorIdade <=30):
     print("Vo² Fraco")
  if(age>=40 and age<=49):
    if(vo2MaxPorIdade<=20 and vo2MaxPorIdade <=26):
     print("Vo² Fraco")
  if(age>=50 and age<=59):
    if(vo2MaxPorIdade<=18 and vo2MaxPorIdade <=24):
     print("Vo²  Fraco")
  if(age>=60 and age<=69):
    if(vo2MaxPorIdade<=16 and vo2MaxPorIdade <=12):
     print("Vo²  Fraco")

 #Vo2 homem regular
  if(age>=20 and age<=29):
    if(vo2MaxPorIdade>=34 and vo2MaxPorIdade <=42):
     print("Vo² regular")
  if(age>=30 and age<=39):
    if(vo2MaxPorIdade<=31 and vo2MaxPorIdade <=38):
     print("Vo² regular")
  if(age>=40 and age<=49):
    if(vo2MaxPorIdade<=27 and vo2MaxPorIdade <=35):
     print("Vo² regular")
  if(age>=50 and age<=59):
    if(vo2MaxPorIdade<=25 and vo2MaxPorIdade <=33):
     print("Vo²  regular")
  if(age>=60 and age<=69):
    if(vo2MaxPorIdade>=23 and vo2MaxPorIdade <=30):
     print("Vo² regular")

 #Vo2 homem Bom
  if(age>=20 and age<=29):
    if(vo2MaxPorIdade>=43 and vo2MaxPorIdade <=52):
     print("Vo² Boa")
  if(age>=30 and age<=39):
    if(vo2MaxPorIdade<=39 and vo2MaxPorIdade <=48):
     print("Vo² Boa")
  if(age>=40 and age<=49):
    if(vo2MaxPorIdade<=36 and vo2MaxPorIdade <=44):
     print("Vo² Boa")
  if(age>=50 and age<=59):
    if(vo2MaxPorIdade<=34 and vo2MaxPorIdade <=34):
     print("Vo² Boa")
  if(age>=60 and age<=69):
    if(vo2MaxPorIdade>=31 and vo2MaxPorIdade <=40):
     print("Vo² Boa")

 #Vo2 homem Excelente
  if(age>=20 and age<=29):
    if(vo2MaxPorIdade>53):
     print("Vo² excelente")
  if(age>=30 and age<=39):
    if(vo2MaxPorIdade>49):
     print("Vo² excelente")
  if(age>=40 and age<=49):
    if(vo2MaxPorIdade>45):
     print("Vo² excelente")
  if(age>=50 and age<=59):
    if(vo2MaxPorIdade>43):
     print("Vo²  excelente")
  if(age>=60 and age<=69):
    if(vo2MaxPorIdade>41):
     print("Vo² excelente")


    return vo2MaxPorIdade
  
#Maximum Aerobic Speed
def calcularVelocity(vo2Max):
 

 return vo2Max/ 3.5



