
from funcs import calcularVo2Max,calcularAgeVo2,calcularVelocity

age = int(input("Digite sua idade: "))
distancy = float(input("digite a distância em metros: "))
timeInMin = float(input("Digite a os minutos: "))
second = float(input("Digite os segundos: "))



vo2Max = calcularVo2Max(distancy,timeInMin,second)
calcularAgeVo2(age,vo2Max)
velocity = calcularVelocity(vo2Max)
print("A velocidade máxima é:",velocity)




