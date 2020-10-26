from tkinter import*
import requests


def format_response(weather):
	try:
		name = weather['name']
		desc = weather['weather'][0]['description']
		temp = weather['main']['temp']


		my_weather = 'City: %s \nConditions: %s \nTemperature (°C) : %s' % (name, desc, temp)
	except:
		my_weather = 'There was a problem retrieving the information'

	return my_weather

def get_weather(city):
	weather_key = 'a4aa5e3d83ffefaba8c00284de6ef7c3'
	url = 'https://api.openweathermap.org/data/2.5/weather'
	params = {'APPID': weather_key, 'q': city, 'units':'metric'}
	response = requests.get(url, params=params)
	weather = response.json()

	label['text'] = format_response(weather)







root = Tk()
root.geometry("500x600")
root.title("Weather Get")
background_image = PhotoImage(file="C:\\Users\\Rajat Khajuria\\Desktop\\image\\beautiful.png")
background_label = Label(root, image = background_image)
background_label.place(x=0,y=0,relwidth=1,relheight=1)
#######################################################button

button = Button(root,text = "Get Weather", bg ="floral white",fg ="deep pink",command=lambda: get_weather(entry.get()))
button.place(x= 280,y=100,height =40)
################################################################labels
labels = Label(root,text ="Welcome to Weather Get",bg ="misty rose")
labels.place(x=170,y=50)
###################################################################entry
entry = Entry(root,bg ="yellow",width = 30)
entry.place(x=100,y=100,height =40)





lower_frame = Frame(root,bg="navajo white2",bd =10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = Label(lower_frame)
label.place(relwidth=1, relheight=1)







root.mainloop()

