income = 15000
if income<10000:
    tax_coefficience=0.0
elif income<30000:
    tax_coefficience=0.5
else:
    tax_coefficience=1

print(' I will pay : ',income * tax_coefficience, ' in taxes')
