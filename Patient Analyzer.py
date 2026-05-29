patients = []

while True:
    name = input("Patient name (or done): ")
    
    if name.lower() == "done":
        break 
    # After they write their name successfully try these.
    try:
        heart_rate = int(input("Heart Rate: ")) 
        temperature = float(input("temperature: "))
        oxygen = int(input("oxygen Saturation: "))
        
    except:
        print("Invalid output, please enter the details correctly")
        continue # sends back to the try loop.
    

    patient = {
        "name": name,
        "heart_rate": heart_rate,
        "temperature": temperature,
        "oxygen": oxygen
    }
    
    patients.append(patient) #we created a list at the very beginning known as patients which will store all the health characterstics of the patient.
    
print()
print("PATIENT REPORT")
print()

total_hr = 0
total_temp = 0

highest_hr = None
lowest_oxygen = None
# we could have put highest oxygen, or temperature and all but that wouldve made the code even longer.
for patient in patients:
    
    total_hr = total_hr + patient["heart_rate"] 
    total_temp = total_temp + patient["temperature"]
    
    if highest_hr is None or patient["heart_rate"] > highest_hr["heart_rate"]:
        highest_hr = patient # This will keep on changing based on the highest heart rate that it encounters.
        
    if lowest_oxygen is None or patient["oxygen"] < lowest_oxygen["oxygen"]: #notice the less than sign here and greater than sign above.
        lowest_oxygen = patient
        
    print("Patient:",patient["name"])
    
    if patient["heart_rate"] > 100:
        print("Warning: High Heart Rate")
        
    if patient["temperature"] > 37.5:
        print("Warning: Fever")
    
    if patient["oxygen"] < 95:
        print("Warning: Low Oxygen")
        
        print()
        
avg_hr = total_hr/len(patients)
avg_temp = total_temp/ len(patients)

print("----------------")
print("SUMMARY")
print("----------------")

print("Total Patients:", len(patients))
print("Average Heart Rate:", round(avg_hr, 2)) #it means round the avg_hr to 2 decimals.
print("Average Temperature:", round(avg_temp, 2))

print()

print("Highest Heart Rate: ")
print(highest_hr["name"], highest_hr["heart_rate"])

print()
print("Lowest oxygen Saturation: ")
print(lowest_oxygen["name"], lowest_oxygen["oxygen"])



