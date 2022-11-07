import os

from getpass import getpass

buckets = []
count = 0

def clear():
    os.system('cls' if os.name == 'nt' else "printf '\033c'")

def search_Edit(groupnumber):
  findIndex = 0
  for i in buckets:
    if(i[0]==groupnumber):
      return findIndex
    findIndex+=1
  return-1

def export_bkt(buckets):
    fopen = open("PushoutBuckets.txt", "a")
    for bucket in buckets:
        for i in bucket:
            fopen.write(i + ",")
        fopen.write("\n")
    fopen.close()

def import_bkt(fname):
    temp = []
    fopen = open(fname, "r")
    for line in fopen:
        line = line.strip(' ')
        if len(line) != 0:
            line = line.split(',')
            temp.append(line)
    fopen.close()
    return temp

def Add_Bucket():
    global count
    Bucket = []
    count += 1
    print('Enter group number: ', end='')
    Bucket.append(input())
    print('Enter machine: ', end='')
    Bucket.append(input())
    print('Enter hookup type: ', end='')
    Bucket.append(input())
    print('Enter capacity: ', end='')
    Bucket.append(input())
    print('Enter width: ', end='')
    Bucket.append(input())
    print('Enter profile: ', end='')
    Bucket.append(input())
    print('Enter weight: ', end='')
    Bucket.append(input())
    print('Enter notes: ', end='')
    Bucket.append(input())
    print('Enter coupler type: ', end='')
    Bucket.append(input())
    print('Enter large notes: ', end='')
    Bucket.append(input())
    buckets.append(Bucket)

    clear()

def view_all_Buckets(buckets):
    for i in buckets:
        print('--------------------------------------------------------------------------------')
        print('Group Number: ', i[0])
        print('Machine: ', i[1])
        print('Pin On / Coupler: ', i[2])
        print('Capacity: ', i[3])
        print('Width: ', i[4])
        print('Profile: ', i[5])
        print('Weight: ', i[6])
        print('Notes & Updates: ', i[7])
        print('Coupler Type: ', i[8])
        print('Large Notes: ', i[9])
        print('--------------------------------------------------------------------------------')

def search_GroupNumber(lst, groupnumber):
    result = []
    for index, item in enumerate(lst):
        if item[0] == groupnumber:
            result.append(index)
    return result

def search_Machine(lst, machine):
    result = []
    for index, item in enumerate(lst):
        if item[1] == machine:
            result.append(index)
    return result

def search_Hookup(lst, hookup):
    result = []
    for index, item in enumerate(lst):
        if item[2] == hookup:
            result.append(index)
    return result

def search_Capacity(lst, capacity):
    result = []
    for index, item in enumerate(lst):
        if item[3] == capacity:
            result.append(index)
    return result

def search_Width(lst, width):
    result = []
    for index, item in enumerate(lst):
        if item[4] == width:
            result.append(index)
    return result

def search_Profile(lst, profile):
    result = []
    for index, item in enumerate(lst):
        if item[5] == profile:
            result.append(index)
    return result

def search_Weight(lst, weight):
    result = []
    for index, item in enumerate(lst):
        if item[6] == weight:
            result.append(index)
    return result

def search_Coupler(lst, coupler):
    result = []
    for index, item in enumerate(lst):
        if item[8] == coupler:
            result.append(index)
    return result

def search_Notes(lst, notes):
    result = []
    for index, item in enumerate(lst):
        if item[9] == notes:
            result.append(index)
    return result

def main():
    global count
    global buckets

while True:
    print("----------------------------- Pushout Buckets ----------------------------------\n")
    print('Enter -1 to exit')
    print('\nThere are (', count, ') buckets in the database.')
    print('--------------------------------------------------------------------------------')
    print('1. View all buckets.\n')
    print('2. Search database for buckets.\n')
    print('3. Admin access')
    print('--------------------------------------------------------------------------------\n')
    print('Please enter your option number: ', end="")
    a = int(input())

    clear()
    if a == -1:

        clear()
        quit()

    elif a == 1:
        view_all_Buckets(buckets)
        print()
        input("Press ENTER to return to the main menu.")

        clear()

    elif a == 2:
        print("----------------------------- Pushout Buckets ----------------------------------\n")
        print('Enter -1 to exit')
        print('\nThere are (', count, ') buckets in the database.')
        print('--------------------------------------------------------------------------------')
        print('Search the entire bucket database utilizing one of the options below.\n')
        print('1. Group Number\n')
        print('2. Machine\n')
        print('3. Hookup Type\n')
        print('4. Capacity\n')
        print('5. Width\n')
        print('6. Profile\n')
        print('7. Weight\n')
        print('8. Coupler\n')
        print('9. Notes')
        print('--------------------------------------------------------------------------------\n')
        print('Please enter your option number: ', end="")
        a = int(input())

        clear()
        if a == 1:
            test = input("Enter group number: ")
            searchable = search_GroupNumber(buckets, test)

            clear()
            for i in searchable:
                print("------------------------------------------------------------------------------")
                print("Group number:", buckets[i][0])
                print("Machine:", buckets[i][1])
                print('Pin On / Coupler:', buckets[i][2])
                print('Capacity:', buckets[i][3])
                print('Width:', buckets[i][4])
                print('Profile:', buckets[i][5])
                print('Weight:', buckets[i][6])
                print('Notes & Updates:', buckets[i][7])
                print('Coupler Type:', buckets[i][8])
                print('Large Notes:', buckets[i][9])
                print("------------------------------------------------------------------------------\n")

            input("Press ENTER to return to the main menu.")

            clear()
        elif a == 2:
            test = input("Enter machine: ")
            searchable = search_Machine(buckets, test)

            clear()
            for i in searchable:
                print("------------------------------------------------------------------------------")
                print("Group number:", buckets[i][0])
                print("Machine:", buckets[i][1])
                print('Pin On / Coupler:', buckets[i][2])
                print('Capacity:', buckets[i][3])
                print('Width:', buckets[i][4])
                print('Profile:', buckets[i][5])
                print('Weight:', buckets[i][6])
                print('Notes & Updates:', buckets[i][7])
                print('Coupler Type:', buckets[i][8])
                print('Large Notes:', buckets[i][9])
                print("------------------------------------------------------------------------------\n")

            input("Press ENTER to return to the main menu.")

            clear()

        elif a == 3:
            test = input("Enter hookup type: ")
            searchable = search_Hookup(buckets, test)

            clear()
            for i in searchable:
                print("------------------------------------------------------------------------------")
                print("Group number:", buckets[i][0])
                print("Machine:", buckets[i][1])
                print('Pin On / Coupler:', buckets[i][2])
                print('Capacity:', buckets[i][3])
                print('Width:', buckets[i][4])
                print('Profile:', buckets[i][5])
                print('Weight:', buckets[i][6])
                print('Notes & Updates:', buckets[i][7])
                print('Coupler Type:', buckets[i][8])
                print('Large Notes:', buckets[i][9])
                print("------------------------------------------------------------------------------\n")

            input("Press ENTER to return to the main menu.")

            clear()

        elif a == 4:
            test = input("Enter capacity: ")
            searchable = search_Capacity(buckets, test)

            clear()
            for i in searchable:
                print("------------------------------------------------------------------------------")
                print("Group number:", buckets[i][0])
                print("Machine:", buckets[i][1])
                print('Pin On / Coupler:', buckets[i][2])
                print('Capacity:', buckets[i][3])
                print('Width:', buckets[i][4])
                print('Profile:', buckets[i][5])
                print('Weight:', buckets[i][6])
                print('Notes & Updates:', buckets[i][7])
                print('Coupler Type:', buckets[i][8])
                print('Large Notes:', buckets[i][9])
                print("------------------------------------------------------------------------------\n")

            input("Press ENTER to return to the main menu.")

            clear()

        elif a == 5:
            test = input("Enter width: ")
            searchable = search_Width(buckets, test)

            clear()
            for i in searchable:
                print("------------------------------------------------------------------------------")
                print("Group number:", buckets[i][0])
                print("Machine:", buckets[i][1])
                print('Pin On / Coupler:', buckets[i][2])
                print('Capacity:', buckets[i][3])
                print('Width:', buckets[i][4])
                print('Profile:', buckets[i][5])
                print('Weight:', buckets[i][6])
                print('Notes & Updates:', buckets[i][7])
                print('Coupler Type:', buckets[i][8])
                print('Large Notes:', buckets[i][9])
                print("------------------------------------------------------------------------------\n")

            input("Press ENTER to return to the main menu.")

            clear()

        elif a == 6:
            test = input("Enter profile: ")
            searchable = search_Profile(buckets, test)

            clear()
            for i in searchable:
                print("------------------------------------------------------------------------------")
                print("Group number:", buckets[i][0])
                print("Machine:", buckets[i][1])
                print('Pin On / Coupler:', buckets[i][2])
                print('Capacity:', buckets[i][3])
                print('Width:', buckets[i][4])
                print('Profile:', buckets[i][5])
                print('Weight:', buckets[i][6])
                print('Notes & Updates:', buckets[i][7])
                print('Coupler Type:', buckets[i][8])
                print('Large Notes:', buckets[i][9])
                print("------------------------------------------------------------------------------\n")

            input("Press ENTER to return to the main menu.")

            clear()

        elif a == 7:
            test = input("Enter weight: ")
            searchable = search_Weight(buckets, test)

            clear()
            for i in searchable:
                print("------------------------------------------------------------------------------")
                print("Group number:", buckets[i][0])
                print("Machine:", buckets[i][1])
                print('Pin On / Coupler:', buckets[i][2])
                print('Capacity:', buckets[i][3])
                print('Width:', buckets[i][4])
                print('Profile:', buckets[i][5])
                print('Weight:', buckets[i][6])
                print('Notes & Updates:', buckets[i][7])
                print('Coupler Type:', buckets[i][8])
                print('Large Notes:', buckets[i][9])
                print("------------------------------------------------------------------------------\n")

            input("Press ENTER to return to the main menu.")

            clear()

        elif a == 8:
            test = input("Enter coupler: ")
            searchable = search_Coupler(buckets, test)

            clear()
            for i in searchable:
                print("------------------------------------------------------------------------------")
                print("Group number:", buckets[i][0])
                print("Machine:", buckets[i][1])
                print('Pin On / Coupler:', buckets[i][2])
                print('Capacity:', buckets[i][3])
                print('Width:', buckets[i][4])
                print('Profile:', buckets[i][5])
                print('Weight:', buckets[i][6])
                print('Notes & Updates:', buckets[i][7])
                print('Coupler Type:', buckets[i][8])
                print('Large Notes:', buckets[i][9])
                print("------------------------------------------------------------------------------\n")

            input("Press ENTER to return to the main menu.")

            clear()

        elif a == 9:
            test = input("Enter notes: ")
            searchable = search_Notes(buckets, test)

            clear()
            for i in searchable:
                print("------------------------------------------------------------------------------")
                print("Group number:", buckets[i][0])
                print("Machine:", buckets[i][1])
                print('Pin On / Coupler:', buckets[i][2])
                print('Capacity:', buckets[i][3])
                print('Width:', buckets[i][4])
                print('Profile:', buckets[i][5])
                print('Weight:', buckets[i][6])
                print('Notes & Updates:', buckets[i][7])
                print('Coupler Type:', buckets[i][8])
                print('Large Notes:', buckets[i][9])
                print("------------------------------------------------------------------------------\n")

            input("Press ENTER to return to the main menu.")

            clear()

        else:
          print('That is not a valid option.\n')
          input('Press ENTER to continue.')

          clear()

    elif a == 3:
      password = getpass()

      clear()

      if password == 'testing':
        print("----------------------------- Pushout Buckets ----------------------------------\n")
        print('Enter -1 to exit')
        print('\nThere are (', count, ') buckets in the database.')
        print('--------------------------------------------------------------------------------')
        print('1. Add new bucket.\n')
        print('2. Edit bucket information.\n')
        print('3. Export bucket information into a text file.\n')
        print('4. Import bucket information from a text file.\n')
        print('--------------------------------------------------------------------------------\n')
        print('Please enter your option number: ', end="")
        a = int(input())

        if a == -1:
          clear()
          quit()

        elif a == 1:
          clear()
          Add_Bucket()
          print()
        
        elif a == 2:
          clear()
          groupnumber = input("Enter the group number of the bucket you would like to update: ")
          bktIndex = search_Edit(groupnumber)
          if bktIndex >= 0:
            buckets[bktIndex][0] = input("Enter Updated Group Number: ")
            buckets[bktIndex][1] = input("Enter Updated Machine: ")
            buckets[bktIndex][2] = input("Enter Updated Pin On / Coupler: ")
            buckets[bktIndex][3] = input("Enter Updated Capacity: ")
            buckets[bktIndex][4] = input("Enter Updated Width: ")
            buckets[bktIndex][5] = input("Enter Updated Profile: ")
            buckets[bktIndex][6] = input("Enter Updated Weight: ")
            buckets[bktIndex][7] = input("Enter Updated Notes & Updates: ")
            buckets[bktIndex][8] = input("Enter Updated Coupler Type: ")
            buckets[bktIndex][9] = input("Enter Updated Large Notes: ")
            print("\nBucket information has been updated successfully.\n")
            input("Press ENTER to return to the main menu.")

            clear()

          else:

            clear()
            print("Bucket " + groupnumber + " is not found.\n")
            input("Press ENTER to return to the main menu.")

            clear()

        elif a == 3:
          export_bkt(buckets)

          clear()
          print("Data Successfully Exported.\n")
          input("Press ENTER to return to the main menu.")

          clear()
        elif a == 4:
          clear()
          buckets = import_bkt("PushoutBuckets.txt")
          count = count + len(buckets)
          print("Data Successfully Loaded.\n")
          input("Press ENTER to return to the main menu.")

          clear()

      else:
        print('Incorrect Password!\n')
        input('Press ENTER to return to the main menu.')

        clear()

    else:

        clear()
        print('Invalid Option.\n')
        input("Press ENTER to return to the main menu.")

        clear()

main()
