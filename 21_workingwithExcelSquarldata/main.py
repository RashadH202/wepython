import pands as pd

#using just file methods
with open("weather_data.csv") as data_file:
    data = data_file.readlines()
    print(data)

#using csv library
    with open("weather-data.csv") as data_file:
        data = csv.reader(data_file)
        tempertures = [int(row[1]) for row in data if row[1] != "temp"]
        print(tempertures)

# using The pands library
    data = pd.read_csv("weather_data.csv")
    print(type(data))
    print(type(data["temp"]))

    data_dict = data.to_dict()
    print(data_dict)

    temp_list = data["temp"].to_list()
    print(len(temp_list))

    print(data["temp"].mean())
    print(data["temp"].max())

    #get data in columns

    print(data["condition"])
    print(data.condition)

    #get Data in Row

    print(data[data.day == "Monday"])
    print(data[data.temp == data.temp.max()])

    #get row data value 
    monday= data[data.day == "Monday"]
    monday_temp = int(int(monday.temp))
    monday_temp_F = monday_temp * 9/5 +32
    print(monday_temp_F)

    #create a dataframe from scratch
    data_dict = {
        "students": ["Amy", "James", "Angela"],
        "scores": [76, 56, 65]
    }

    data = pd.DataFrame(data_dict)
    data.to_csv("new_data.csv")


    #central park squirrel data analysis
    data = pd.read_csv("2018_Central_Park_Squirrel_-_squirrel_data.csv")

    #count squirrels by fur color
    squirrel_counts = data["Primary Fur Color"].value_counts()
    print(squirrel_counts)

    #save squirrel counts to a new csv file

    squirrel_counts.to_csv("squirrel_count.csv", header=["Fur Color", "Count" ])