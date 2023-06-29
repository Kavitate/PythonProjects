while True:
  correct_answers = ['B','D','A','A','B','A','B','A','C','D','B','C','D','A','D','C','C','B','D','A']
  student_answers = []
  file_name = input("Enter file name: ")
  file_import = open(file_name, "r")

  for line in file_import:
    line = line.strip()
    student_answers.append(line)

  correct = 0
  incorrect = 0
  correct_list = []
  incorrect_list = []

  for i in range(20):
    if student_answers[i] == correct_answers[i]:
      correct += 1
      correct_list.append(i+1)
    else:
      incorrect += 1
      incorrect_list.append(i+1)

  if correct >= 15:
    import os
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("--------------------------", file_name, "has passed. ------------------------------\n")
  else:
    import os
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("--------------------------", file_name, "has failed. ------------------------------\n")

  print("Total correct answers: ", correct)
  print("Total incorrect answers: ", incorrect)
  print("Correct answers: ", correct_list)
  print("Incorrect answers: ", incorrect_list)
  print("------------------------------------------------------------------------------")
  input("\nPress ENTER to grade another test.")
  import os
  os.system('cls' if os.name == 'nt' else "printf '\033c'")
