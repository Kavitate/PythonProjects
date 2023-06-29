while True:
  print("_________         __                __          __")
  print("\_   ___ \_____  |  |   ____  __ __|  | _____ _/  |_  ___________  ______")
  print("/    \  \/\__  \ |  | _/ ___\|  |  \  | \__  \\   __\/   _ \_  __ \/  ___/")
  print("\     \____/ __ \|  |_\  \___|  |  /  |__/ __ \|  | (  (_) )   | \/\___ \ ")
  print(" \________(_____/ ____/\_____>____/|____(_____/ __|  \____/ |__|  /______\   By: Kavitate")
  print("__________________________________________________________________________________________\n")
  print("Select the calculator you would like to use.\n")
  print("1.  PSI Calculation                    11.  CU-IN/REV")
  print("2.  Torque Force                       12.  CC/REV")
  print("3.  Horsepower Applied                 13.  Torque Applied")
  print("4.  Flow Rate                          14.  Stroke Time")
  print("5.  Gallons Per Minute                 15.  Blind End Cylinder Area")
  print("6.  Tine Shaft Bend                    16.  Rod End Cylinder Area")
  print("7.  Electric Horsepower")
  print("8.  Fluid Horsepower ")
  print("9.  Motor Speed (Flow) ")
  print("10. Cylinder Force\n")
  greeting = input("Enter your selection here: ")
  selection = float(greeting)

  if selection == 1:
    import os
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("\nEnter the values below for PSI calculation.\n" )

    Flow = input("Enter Flow: ")
    Restriction = input("Enter Restriction: ")

    psi_calculation = float(Flow) * float(Restriction)
    print("\nPSI Calculation =" , psi_calculation)

  elif selection == 2:
    import os
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("Enter the values below to calculate Torque Force.\n" )

    Pressure = input("Enter PSI: ")
    Displacement = input("Enter Displacement(CU-IN/REV): ")

    torque_force = float(Pressure) * float(Displacement) / 6.28
    print("\nTorque Force (IN. LBS.):" , torque_force)

  elif selection == 3:
    import os
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("Enter the values below to calculate Horsepower Applied.\n" )

    IN_LBS = input("Enter IN. LBS.: ")
    RPM = input("Enter RPM: ")

    horsepower_applied = float(IN_LBS) * float(RPM) / 63025
    print("\nHorsepower Applied:" , horsepower_applied)

  elif selection == 4:
    import os
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("Enter the values below to calculate Flow Rate.\n" )

    Velocity = input("Enter Velocity(FT/S):")
    Area = input("Enter Area(IN²): ")

    flow_rate = float(Velocity) * float(Area) / 0.3208
    print("\nFlow Rate:" , flow_rate)

  elif selection == 5:
    import os
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("Enter the values below to calculate Gallons Per Minute.\n" )

    Pump_RPM = input("Enter Pump RPM: ")
    Displacement = input("Enter Displacement(CU-IN/REV): ")

    GPM = float(Pump_RPM) * float(Displacement) / 231 * 0.8
    print("\nGallons Per Minute:" , GPM)

  elif selection == 6:
    import os
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("Enter the values below to calculate Tine Shaft Bend.\n" )

    Tine_Max_Load = input("Enter Tine Max Load: ")
    Length_To_Load_Point = input("Enter Length To Load Point: ")
    Riser_Height = input("Riser Height: ")

    Tine_Shaft_Bend = float(Tine_Max_Load) * float(Length_To_Load_Point) / float(Riser_Height)
    print("\nTine Shaft Bend:" , Tine_Shaft_Bend)

  elif selection == 7:
    import os
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("Enter the values below to calculate Electric Horsepower.\n" )

    Volts = input("Enter Volts: ")
    Amps = input("Enter Amps: ")
    Efficiency = input("Efficiency: ")

    Electric_Horsepower = float(Volts) * float(Amps) * float(Efficiency) / 746
    print("\nElectric Horsepower:" , Electric_Horsepower)

  elif selection == 8:
    import os
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("Enter the values below to calculate Fluid Horsepower.\n" )

    Pressure = input("Enter PSI: ")
    GPM = input("Enter GPM: ")
    Efficiency = input("Efficiency: ")

    Fluid_Horsepower = float(Pressure) * float(GPM) * float(Efficiency) / 1714
    print("\nFluid Horsepower:" , Fluid_Horsepower)

  elif selection == 9:
    import os
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("Enter the values below to calculate Motor Speed (Flow).\n" )

    GPM = input("Enter GPM: ")
    Displacement = input("Enter Displacement: ")
    Efficiency = input("Efficiency: ")

    Motor_Speed = float(231 * float(GPM)) / float(Displacement) * float(Efficiency)
    print("\nMotor Speed (Flow):" , Motor_Speed)

  elif selection == 10:
    import os
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("Enter the values below to calculate Cylinder Force(Lbs.).\n" )

    Pressure = input("Enter PSI: ")
    Cylinder_Area = input("Enter Cylinder Area: ")

    Cylinder_Force = float(Pressure) * float(Cylinder_Area)
    print("\nCylinder Force(Lbs.):" , Cylinder_Force)

  elif selection == 11:
    import os
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("Enter the values below to calculate CU-IN/REV.\n" )

    CC_REV = input("Enter CC/REV: ")

    CU_IN = float(CC_REV) * 0.0610237
    print("\nCU-IN/REV:" , CU_IN)

  elif selection == 12:
    import os
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("Enter the values below to calculate CC/REV.\n" )

    CU_IN = input("Enter CU-IN/REV: ")

    CC_REV = float(CU_IN) * 16.3871
    print("\nCC/REV:" , CC_REV)

  elif selection == 13:
    import os
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("Enter the values below to calculate Torque Applied.\n" )

    Horsepower = input("Enter Horsepower: ")
    RPM = input("Enter RPM: ")

    Torque_Applied = float(Horsepower) * 63025 / float(RPM)
    print("\nTorque Applied(IN. LBS.):" , Torque_Applied)

  elif selection == 14:
    import os
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("Enter the values below to calculate Stroke Time.\n" )

    Area = input("Enter Area: ")
    Stroke = input("Enter Stroke: ")
    GPM = input("Enter GPM: ")

    Stroke_Time = float(Area) * float(Stroke) * 0.26 / float(GPM)
    print("\nStroke Time:" , Stroke_Time)

  elif selection == 15:
    import os
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("Enter the values below to calculate Blind End Cylinder Area.\n" )

    Piston_Diameter = input("Enter Piston Diameter: ")
    Radius = float(Piston_Diameter) / 2
    R_Squared = float(Radius * Radius)

    print("Radius:" , Radius)
    print("Radius Squared:" , R_Squared)

    BECA = float(R_Squared) * 3.1415
    print("\nBlind End Cylinder Area:" , BECA)

  elif selection == 16:
    import os
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("To calculate the Rod End Cylinder Area we must first calculate the Blind End Cylinder Area.\n" )

    Piston_Diameter = input("Enter Piston Diameter: ")
    Radius = float(Piston_Diameter) / 2
    R_Squared = float(Radius * Radius)

    BECA = float(R_Squared) * 3.1415
    print("Blind End Cylinder Area:" , BECA)
    Rod_Diameter = input("Enter Rod Diameter: ")
    Radius = float(Rod_Diameter) / 2
    R_Squared = float(Radius * Radius)
    Rod_Area = float(R_Squared) * 3.1415
    print("Radius:" , Radius)
    print("Radius Squared:" , R_Squared)
    print("Rod Area:" , Rod_Area)

    RECA = float(BECA - Rod_Area)
    print("\nRod End Cylinder Area:" , RECA)

  else:
    import os
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("\nERROR, SELECTION OUT OF RANGE")

  var = input("\nPress ENTER to return to the main menu.")
  import os
  os.system('cls' if os.name == 'nt' else "printf '\033c'")
  continue
