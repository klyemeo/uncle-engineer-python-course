height = float(input("ป้อนส่วนสูง:  "))
height =( height/100)**2
weight = float(input("ป้อนน้ำหนัก:  "))
bmi = weight/height
print(bmi)
if bmi < 18.50 :
    print('ผอม')
elif bmi >= 18.50 and bmi <= 22.90:
    print('ปกติ')
elif bmi >=23 and bmi <= 24.90:
    print('ท้วม')
elif bmi >=25 and bmi <=29.90:
    print('อ้วน')
elif bmi > 30:
    print('อ้วนมาก')
            
