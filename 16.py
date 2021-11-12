def BMI_test(name,height,weight):
    BMI=round(weight/(height/100)/(height/100),6)
    if BMI>24:
        print("Hi {name}, Your BMI: {xxx} too HIGH.".format(name=name,xxx=BMI))
    elif BMI<18.5:
        print("Hi {name}, Your BMI: {xxx} too LOW.".format(name=name,xxx=BMI))
    else:
        print("Hi {name}, Your BMI: {xxx}.".format(name=name,xxx=BMI))

def main():
    name=str(input())
    height=float(input())
    weight=float(input())
    BMI_test(name,height,weight)

main()