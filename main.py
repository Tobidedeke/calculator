 #prcaticing coding and deploying of a calculator
#new update!!
#test b3
class Calculator:
   # Firstnumber = 0
    #Secondnumber = 0
    #Answer = Firstnumber + Secondnumber

    def __init__(self, num1, num2):
       self.Firstnumber = num1
       self.Secondnumber = num2

    def Calculation(self, num1, num2):
       answer = num1 + num2
       return answer


print("{: ^100s}".format("***calculator app***"))

obj1 = Calculator(5, 5)

print(obj1.Calculation( 5, 5))


