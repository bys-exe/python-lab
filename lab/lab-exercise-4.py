# lab exercise 4 - electricity bill generator

print("--------------------------------------------------")
print("Welcome to the Electricity bill generator!")
print("--------------------------------------------------")

name = str(input("Enter your name: "))
id = int(input("Enter your ID: "))
prev_read = float(input("Enter the previous meter reading (kWh): "))
curr_read = float(input("Enter the current meter reading (kWh): "))
cost = float(input("Enter the cost per unit in rupees: "))

units_consumed = curr_read - prev_read
energy_charge = units_consumed * cost
electricity_duty = (5/100) * energy_charge
fixed_meter_charge = 100
net_bill_amount = energy_charge + electricity_duty + fixed_meter_charge

print("------------------ELECTRICITY BILL-----------------")
print(f"Name:                               {name}")
print(f"Id:                                 {id}")
print(f"Previous reading:                   {prev_read}")
print(f"Current reading:                    {curr_read}")
print(f"Total units consumed:               {units_consumed:.2f} kWh")
print(f"Energy charged:                     {energy_charge}")
print(f"Electricity Duty:                   {electricity_duty}")
print(f"Fixed Meter Charge:                 {fixed_meter_charge}")
print("----------------------------------------------------")
print(f"Net bill amount:                    {net_bill_amount} Rupees")
print("----------------------------------------------------")
