import math as m #importing method/libary to use cosine and sine
#making 2 lists of forces and anles having equal number of elements 
#if length of forces != length of angles then exit the program 
#forces = [32.2, 85.6, -72.1, 12.3, -7.9]#force in Newton
#angles = [45.0, 62.4, 110.2, 180.0, 207.9]#angles in degrees respectively

numOfElements = int(input("Enter the number of forces: "))
forces = []
for i in range(numOfElements):
    force = float(input(f"Enter force {i+1}: "))
    forces.append(force)
print(forces)

numOfangles = int(input("Enter the number of angles: "))
angles = []
for i in range(numOfangles):
    angle = float(input(f"Enter angle {i+1}: ")) 
    angles.append(angle)
print(angles)

if len(forces) != len(angles):
    print("Your input is incorrect . Please check it and try again!")
    quit()

#for each (force , angle): 
FxSum = 0.0 #Fx sum += force * cos(angle). Also called as running sum
FySum = 0.0 #Fy sum += force * sin(angle)

#Resultant = ( (fx sum)^2 + (fy sum)^2 )^(0.5)
#Theta= tan^(-1) (fy sum / fx sum)
 
for index, force in enumerate(forces): #enumerate means we can track the index of each element ie.forces which we are looping over 
    angle = angles[index] #retrieves value of index of the force and then refers to same index in angles list

    if angle >= 90 and angle <= 180:
        angle = 180 - angle
        FxSum += -round(force * m.cos(m.radians(angle)),2)
        FySum += round(force * m.sin(m.radians(angle)),2)

    elif angle >= 180 and angle <= 270:
        angle = angle - 180
        FxSum += -round(force * m.cos(m.radians(angle)),2)
        FySum += -round(force * m.sin(m.radians(angle)),2)

    elif angle >= 270 and angle <= 360:
        angle = 360 - angle
        FxSum += round(force * m.cos(m.radians(angle)),2)
        FySum += -round(force * m.sin(m.radians(angle)),2)


print(f"Sum of all horizontal components is {FxSum}")#the F before the inerted commas denotes a f-string which means that we can print a value of a variable in a print function along with predecided sentence or string.
print(f"Sum of all vertical components is {FySum}")
RMag = m.sqrt((FxSum)**2 + (FySum)**2)
RMag = round(RMag, 2)
print(f"Resultant is {RMag}")
 
if FySum == 0.0 and FxSum == 0.0:
    Rtheta = 0.0
elif FxSum == 0.0 and FySum > 0.0:
    Rtheta = 90.0
elif FxSum == 0.0 and FySum < 0.0:
    Rtheta = -90.0
else:
    Rtheta = m.atan2(FySum, FxSum)#return angle in radians
    Rtheta = m.degrees(Rtheta)#degrees
print(f"RESULTANT: {RMag} \n Angle: {Rtheta}")