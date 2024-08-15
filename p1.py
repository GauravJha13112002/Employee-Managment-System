from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import *
import requests
import matplotlib.pyplot as plt
import pandas as pd
import csv

root = Tk()
root.title("EMPLOYEE MANAGMENT SYSTEM")
root.geometry("1000x900+200+50")
f=("Arial",30,"bold")
root.configure(bg="Green")

def f1():
	root.withdraw()
	ae.deiconify()
def f2():
	root.withdraw()
	ve.deiconify()
	ve_st_data.delete(1.0,END)
	con = None
	try :
		con = connect("RAM.db")
		cursor=con.cursor()
		sql = "select * from emp order by id"
		cursor.execute(sql)
		data=cursor.fetchall()
		info=""
		for d in data :
			info = info + "id =" +str(d[0])+ "name =" +str(d[1])+ "salary = " +str(d[2])+ "\n"
		ve_st_data.insert(INSERT,info)
	except Exception as e :
		showerror("issue" , e)
	finally :
		if con is not None :
			con.close()
def f3():
	root.withdraw()
	ue.deiconify()
def f13():
	con=None
	try:
		con=connect('RAM.db')
		cursor=con.cursor()
		sql="update emp set name='%s', salary='%s' where id='%s' "
		id=ue_ent_id.get()
		name=ue_ent_name.get()
		salary=ue_ent_salary.get()
		cursor.execute(sql %(name, salary, id))

		if id.isalpha():
			showerror('Failure','ID should be integers not in alphabets, It should be in +ve integers')
		elif len(id)==0:
			showerror('Failure','ID should not be empty, It should be in +ve integers')

		elif '-' in id:
			showerror('Failure','ID should not be -ve, It should be in +ve integers')
		elif id.isdigit():
			id1=int(id)
			if id==0:
				showerror('Failure','ID should be not zero')
			else:
				if name.isdigit():
					showerror('Failure','Name shoulde be in alphabets not in numbers')
				elif len(name)==0:
					showerror('Failure','Name should not be empty')
				elif  name.isalpha() and len(name)<2 :
					showerror('Failure',' at least it has 2 alphabets')

				elif name.isalpha() and len(name)>=2:
					if salary.isalpha() :
						showerror('Failure','Salary should  be in integers ')
					elif len(salary)==0:
						showerror('Failure','Salary should not be empty')

					elif salary.isdigit():
						salary1=int(salary)
						if salary1<8000:
							showerror('Failure','Salary should not be less than 8000')
					elif salary.isalnum():
						showerror('Failure','Salary contain alphanumeric value, it should contain only +ve integers')
				elif name.isalnum():
					showerror('Failure','Name contain alphanumeric value, it should contain atleast  2 alphabets')
		elif id.isalnum():
			showerror('Failure','ID contain alphanumeric value, it should contain only +ve integers')



		if (id.isalpha() or id.isalnum() or id.isdigit() or (len(id)==0)):
			if (name.isalpha() or name.isalnum() or name.isdigit() or (len(name)==0)):
				if (salary.isalpha() or salary.isalnum() or salary.isdigit() or (len(salary)==0)):
					if (not name.isalnum() ) or name.isalpha():

						if cursor.rowcount==1 and int(id)>0 and len(name)>2 and int(salary)>8000 :
							con.commit()
							showinfo('updated',str(id)+' is updated')
						elif cursor.rowcount==0 and id.isdigit():
							showerror('Failure',str(id)+' is not exists')
				
				else:
					showerror('Failure','Salary is invalid, It should be in +ve integers')					
			else:
				showerror('Failure','Name is invalid, It should be in alphabets')
		else:
			showerror('Failure','ID is invalid, It should be in +ve integers')


	#except Exception as e:
		pass
	finally:
		if con is not None:
			con.close()
	ue_ent_id.delete(0,END)
	ue_ent_name.delete(0,END)
	ue_ent_salary.delete(0,END)
	ue_ent_id.focus()
def f7():
	ue.withdraw()
	root.deiconify()
			
			
def f4():
	root.withdraw()
	de.deiconify()
def f14():
	con=None
	try:
		con=connect("RAM.db")
		cursor=con.cursor()
		sql="delete from emp where id='%s' "
		id= de_ent_id.get()
		cursor.execute(sql %(id))
		if id.isalpha() :
		    showerror("failed","id should be integers not in alphabets")
		elif len(id)==0:
			showerror("failed","id should not be empty")
		elif '-' in id:
		    showerror("failed","ID should not be -ve")
		elif id.isdigit():
			id1=int(id)
			if id==0:
				showerror('ID should be +ve integer')
			else:
				con.commit()
			if cursor.rowcount==0:
				showerror('Failure',str(id)+'  record does  not exists')
			else:
				showinfo('Success',str(id)+' id is deleted')
	except ValueError:
		showerror('Error','Enter id correct')
	except Exception as e:
		showerror(id1,' not exists')
	finally:
		if con is not None:
			con.close()
		de_ent_id.delete(0,END)
		de_ent_id.focus()
def f5():
	ae.withdraw()
	root.deiconify()
def f6():
	ve.withdraw()
	root.deiconify()

def f8():
	de.withdraw()
	root.deiconify()


def f11() :
	con = None
	try :
		con = connect("RAM.db")
		cursor=con.cursor()
		cursor.execute("select* from emp order by salary DESC limit 5 ;")
		with open("boss.csv", 'w', newline = '')as csv_file:
			csv_writer=csv.writer(csv_file)
			csv_writer.writerow([i[0] for i in cursor.description])
			csv_writer.writerows(cursor)
		con.close()

		data = pd.read_csv("boss.csv")
		name = data["name"]
		salary = data["salary"]
		plt.bar(name,salary,width=0.30,color="red")
		plt.xlabel("NAME")
		plt.ylabel("SALARY")
		plt.show()
	
	finally :
		if con is not None :
			con.close()

def message():
	try:
		wa="https://ipinfo.io/"
		res= requests.get(wa)
		data= res.json()
		city= data["city"]
		msg=str("Location:- ")+ city
		#lab_msg.configure(text=msg) 
		a1 = "https://api.openweathermap.org/data/2.5/weather"
		a2 = "?q=" + city
		a3 = "&appid=" + "c6e315d09197cec231495138183954bd"
		a4 = "&units=" + "metric"
		wa=a1+a2+a3+a4
		res=requests.get(wa)
		data=res.json()
		temp=data['main']['temp']
		temp1=round(temp,1)
		msg1=str("Location: ")+city+str('    Temp: ')+ str(temp1)+"8\u00b0"+str('C')
		lab_msg1.configure(text=msg1)
		
	except Exception as e :
		print("issue", e)

lab_msg1=Label(root,font=f,bg='SpringGreen2')
lab_msg1.pack(pady=15)

message()






	
def f9():
	con=None
	try:
		con=connect("RAM.db")
		cursor=con.cursor()
		sql="insert into emp values('%d','%s','%d')"
		id=ae_ent_id.get()
		name=ae_ent_name.get()
		salary=ae_ent_salary.get()
		if id.isalpha() :
			showerror('Failure','id is alphabets')
		elif len(id)==0:
			showerror('Failure','id is empty')
		elif '-' in id:
			showerror('Failure','id is negative')
		elif id.isdigit():
			id1=int(id)
			if id==0:
				showerror('id is 0')
			else:
				if name.isdigit():
					showerror('Failure','name has numbers')
				elif len(name)==0:
					showerror('Failure','name is empty')
				elif name.isalpha and len(name)<2:
					showerror('Failure','name is too short')
				elif name.isalpha() and len(name)>=2:
					if salary.isalpha() :
						showerror('Failure','salary has alphabets')
					elif len(salary)==0:
						showerror('Failure','salary is empty')
					elif salary.isdigit():
						salary1=int(salary)
						if salary1<8000:
							showerror('Failure','salary is less than 8000')
						elif salary1>8000:
							cursor.execute(sql%(id1,name,salary1))
							con.commit()
							showinfo("success", str(id1)+" is succesfully added")
					else:
						showerror('Failure','salary is alphabets num')
				else:
					showerror('Failure','wrong name')  
		elif id.isalnum():
			showerror('Failure','id is alphabets num') 
		else:
			showerror('Failure','id is not valid')
	except Exception as e :
		showerror("failed", str(id1)+ " already exist")
 
	except Exception as e:
		con.rollback()
		showerror('issue',e)
		print(e)
	finally:
		if con is not None :
			con.close()
	ae_ent_id.delete(0,END)
	ae_ent_name.delete(0,END)
	ae_ent_salary.delete(0,END)
	ae_ent_id.focus()
			


btn_add =Button(root,text="ADD THE EMPLOYEE",font=f,command=f1)
btn_add.pack(pady=10)
btn_view = Button(root,text="VIEW THE EMPLOYEE",font=f,command=f2)
btn_view.pack(pady=10)
btn_update = Button(root,text="UPDATE THE EMPLOYEE",font=f,command=f3)
btn_update.pack(pady=10)
btn_delete = Button(root,text="DELETE THE EMPLOYEE",font=f,command=f4)
btn_delete.pack(pady=10)
btn_charts = Button(root,text="CHARTS",font=f,command = f11)
btn_charts.pack(pady=10)






ae=Toplevel(root)
ae.title("ADD THE EMPLOYEE")
ae.geometry("1000x700+200+50")
f=("Arial",30,"bold")
ae.configure(bg="Blue")


ae_lab_id=Label(ae,text="ENTER THE ID",font=f)
ae_lab_id.pack(pady=10)
ae_ent_id=Entry(ae,font=f)
ae_ent_id.pack(pady=10)
ae_lab_name=Label(ae,text="ENTER THE NAME",font=f)
ae_lab_name.pack(pady=10)
ae_ent_name=Entry(ae,font=f)
ae_ent_name.pack(pady=10)
ae_lab_salary=Label(ae,text="ENTER THE SALARY",font=f)
ae_lab_salary.pack(pady=10)
ae_ent_salary=Entry(ae,font=f)
ae_ent_salary.pack(pady=10)
ae_btn_save=Button(ae,text="SAVE",font=f,command=f9)
ae_btn_save.pack(pady=10)
ae_btn_back=Button(ae,text="BACK",font=f,command=f5)
ae_btn_back.pack(pady=10)
ae.withdraw()


ve=Toplevel(root)
ve.title("VIEW THE EMPLOYEE")
ve.geometry("1000x800+100+50")
f=("Arial",30,"bold")
ve.configure(bg="Pink")
ve_st_data=ScrolledText(ve,width=40,height=10,font=f)
ve_st_data.pack(pady=10)
ve_btn_back=Button(ve,text="BACK",font=f,command=f6)
ve_btn_back.pack(pady=10)
ve.withdraw()




ue=Toplevel(root)
ue.title("UPDATE THE EMPLOYEE")
ue.configure(bg="Red")
ue.geometry("1000x800+100+50")
f=("Arial",30,"bold")
ue.configure(bg="Orange")








ue_lab_id=Label(ue,text="ENTER THE ID",font=f)
ue_lab_id.pack(pady=10)
ue_ent_id=Entry(ue,font=f)
ue_ent_id.pack(pady=10)
ue_lab_name=Label(ue,text="ENTER THE NAME",font=f)
ue_lab_name.pack(pady=10)
ue_ent_name=Entry(ue,font=f)
ue_ent_name.pack(pady=10)
ue_lab_salary=Label(ue,text="ENTER THE SALARY",font=f)
ue_lab_salary.pack(pady=10)
ue_ent_salary=Entry(ue,font=f)
ue_ent_salary.pack(pady=10)
ue_btn_save=Button(ue,text="SAVE",font=f,command=f13)
ue_btn_save.pack(pady=10)
ue_btn_back=Button(ue,text="BACK",font=f,command=f7)
ue_btn_back.pack(pady=10)
ue.withdraw()





de=Toplevel(root)
de.title("DELETE THE EMPLOYEE")
de.geometry("1000x800+100+50")
f=("Arial",30,"bold")
de.configure(bg="yellow")
de_lab_id=Label(de,text="ENTER THE ID",font=f)
de_lab_id.pack(pady=10)
de_ent_id=Entry(de,font=f)
de_ent_id.pack(pady=10)
de_btn_save=Button(de,text="SAVE",font=f,command=f14)
de_btn_save.pack(pady=10)
de_btn_back=Button(de,text="BACK",font=f,command=f8)
de_btn_back.pack(pady=10)
de.withdraw()



root.mainloop()



