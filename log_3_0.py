import pandas as pd
import datetime
# Get the current date and time, and format it as a string
now = datetime.datetime.now()
print(now.strftime("%Y-%m-%d %H-%M-%S"))
# Initialize an empty list for storing user input
num_rows = 10
num_columns = 20
data = [['' for _ in range(num_columns)] for _ in range(num_rows)]
column_names = [f'{i+1}' for i in range(num_columns)]
# Collect user input until the user enters a space
data[0][0] ="C"
data[1][0] ="G"
data[2][0] ="T"
data[3][0] ="EC"
data[4][0] ="H"
data[5][0] ="SC"
data[6][0] ="I"
data[7][0] ="L"
data[8][0] ="Diary"
Col = 1
count = 0
times = ''
time_all = 0
good = 0
bad = 0
while True:
    Row = 0
    user_input = input("the name of this project(type blank to quit!)")
    if user_input == " ":
        break
    count = count +1
    data[Row][Col] = user_input
    data[1][Col] = input("the general goal of this project")
    times=input("the time consumed by this project(h)")
    time_all=time_all+float(times)
    data[2][Col] = times
    learning_condition = input("evaluate the efficiency of this project(good/common/bad)")
    data[3][Col] = learning_condition
    if learning_condition == 'good':
        good=good+1
    elif learning_condition == 'bad':
        bad = bad +1
    while True:
        harvest = input("type you harvest")
        word_count = len(harvest.split())
        if word_count > 5:
            data[4][Col] = harvest
            break
        else:
            print("You have to type at least 5 words so that you can truly think. Please retype!")
    while True:
        shortcoming = input("the shortcoming of your project")
        word_count = len(shortcoming.split())
        if word_count > 5:
            data[5][Col] = shortcoming
            break
        else:
            print("You have to type at least 5 words so that you can truly think. Please retype!")
    while True:
        improvement = input("How can you improve it?type your solution")
        word_count = len(improvement.split())
        if word_count > 5:
            data[6][Col] = improvement
            break
        else:
            print("You have to type at least 5 words so that you can truly think. Please retype!")
    while True:
        law = input("what law can you conclude from your project/harvest/improvment or soulution")
        word_count = len(improvement.split())
        if word_count > 5:
            data[7][Col] = improvement
            break
        else:
            print("You have to type at least 5 words so that you can truly think. Please retype!")
    Col = Col +1
data[0][Col] = 'G'
data[1][Col] = input("recall your general goal")
data[2][Col] = str(time_all)
data[3][Col] = input("how do you feel about today's learning?")
data[4][Col] = ''
while True:
    shortcoming_of_today = input("shortcoming of today's learning")
    word_count = len(shortcoming_of_today.split())
    if word_count > 5:
        data[5][Col] = shortcoming_of_today
        break
    else:
        print("You have to type at least 5 words so that you can truly think. Please retype!")
while True:
    improvement_of_today = input("how to improve it?")
    word_count = len(improvement_of_today.split())
    if word_count > 5:
        data[6][Col] = improvement_of_today
        break
    else:
        print("You have to type at least 5 words so that you can truly think. Please retype!")
while True:
    law_of_today = input("the laws behind your solution")
    word_count = len(law_of_today.split())
    if word_count > 5:
        data[7][Col] = law_of_today
        break
    else:
        print("You have to type at least 5 words so that you can truly think. Please retype!")
Col=Col+1
data[1][Col] = "the percent of good is:"+str(good/count)
data[2][Col] = "the percent of bad is:"+str(bad/count)
while True:
    input_lines = []
    while True:
        line = input("write your diary.(type 'q' to quit)")
        if line == "q":
            break
        input_lines.append(line)
    word_count = sum(len(line.split()) for line in input_lines)
    if word_count >= 10:
        data[8][1] = "\n".join(input_lines)
        break
    else:
        print("You have to type at least 10 words so that you can truly think. Please retype!")

# Convert the list to a pandas DataFrame with a single column named "Projects"
df = pd.DataFrame(data, columns=column_names)
# Export the DataFrame to an Excel file with the current date and time as the filename
df.to_excel(now.strftime("%Y-%m-%d %H-%M-%S")+'.xlsx', index=False)
print(count)