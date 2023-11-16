from tkinter import *
from tkinter.messagebox import *
from tkinter import ttk

root=Tk()
root.title('Temperature Converter')
root.geometry('700x700+50+50')
root.configure(bg='grey')
f=('Arial',20)
f1=('Algerian',20,'underline')
f2=('Arial',20,'underline')

lab_temp=Label(root,text='Temperature Conversion',font=f1,bg='grey')
lab_temp.pack(pady=30)
lab_temp1=Label(root,text='Enter Temperature',font=f,bg='grey',fg='white')
lab_temp1.place(x=50,y=100)
ent_temp=Entry(root,font=f,bg='grey',fg='white')
ent_temp.place(x=300,y=100)
combo_temp=ttk.Combobox(root,values=['Fahrenheit','Kelvin','Celsius'])
combo_temp.place(x=300,y=160)
lab_temp1=Label(root,text='TO',font=f,bg='grey',fg='white')
lab_temp1.place(x=350,y=190)
combo_temp1=ttk.Combobox(root,values=['Fahrenheit','Kelvin','Celsius'])
combo_temp1.place(x=300,y=235)

def conv():
	a=combo_temp.get()
	b=combo_temp1.get()

	try:
		c=float(ent_temp.get())
	except:
		showerror('Issue','Enter Valid Temperature')
		return

	if a=='' or b=='':
		showerror('Issue','Select an option!')
		return
	elif a=='Celsius' and b=='Kelvin':
		try:
			c=float(ent_temp.get())
		except Exception as e:
			showerror('Issue',e)
			return
		k=c*274.15
		showinfo('Conversion',(round(k,2),'Kelvin'))
	elif a=='Celsius' and b=='Fahrenheit':
		try:
			c=float(ent_temp.get())
		except Exception as e:
			showerror('Issue',e)
			return
		f=c*33.8
		showinfo('Conversion',(round(f,2),'Fahrenheit'))
	elif a=='Kelvin' and b=='Celsius':
		try:
			k=float(ent_temp.get())
		except Exception as e:
			showerror('Issue',e)
			return
		c=k*(-272.15)
		showinfo('Conversion',(round(c,2),'Celsius'))
	elif a=='Kelvin' and b=='Fahrenheit':
		try:
			k=float(ent_temp.get())
		except Exception as e:
			showerror('Issue',e)
			return
		f=k*(-457.87)
		showinfo('Conversion',(round(f,2),'Fahrenheit'))
	elif a=='Fahrenheit' and b=='Celsius':
		try:
			f=float(ent_temp.get())
		except Exception as e:
			showerror('Issue',e)
			return
		c=f*(-17.22)
		showinfo('Conversion',(round(c,2),'Celsius'))
	elif a=='Fahrenheit' and b=='Kelvin':
		try:
			f=float(ent_temp.get())
		except Exception as e:
			showerror('Issue',e)
			return
		k=f*(255.92)
		showinfo('Conversion',(round(k,2),'Kelvin'))
	else:
		showerror('Issue','Invalid Parameters')
		return

btn_conv=Button(root,text='Convert',font=f2,bg='lightblue',command=conv)
btn_conv.place(x=300,y=300)

root.mainloop()