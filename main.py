from tkinter import * 
from tkinter import ttk
import mysql.connector
from mysql.connector import Error
from tkinter import messagebox
from tkinter import filedialog
class window1:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1160x418")
        self.root.title("Mobile Number System")
        self.root.config(bg='White') 
        self.product_id=StringVar()
        self.product_name=StringVar()
        self.sell_price=IntVar()
        self.quantity=IntVar()
        self.insertdesign()    

    def insertdesign(self):

        bgc="white"        
 
        self.f1=LabelFrame(self.root,bd=7,relief=GROOVE,text="Inventory Management",font=("times new roman",15,"bold"),fg="Blue",bg='White')
        self.f1.place(x=0,y=10,width=350,height=400)  

        self.lab1=Label(self.f1,text="Product Id",font=("times new roman",15,"bold"),fg="black").grid(row=2,column=3)
        self.txt1=Entry(self.f1,width=15,text="id",font=("times new roman",15,"bold"),bd=5,relief=SUNKEN,textvariable=self.product_id).grid( row=2, column=5,padx=10,pady=10)
        self.lab2=Label(self.f1,text="Product Name",font=("times new roman",15,"bold"),fg="black").grid(row=4,column=3,padx=10,pady=10)
        self.txt2=Entry(self.f1,width=15,text="name",font=("times new roman",15,"bold"),bd=5,relief=SUNKEN,textvariable=self.product_name).grid( row=4, column=5,padx=10,pady=10)
        self.lab1=Label(self.f1,text="Selling Price",font=("times new roman",15,"bold"),fg="black").grid(row=6,column=3)
        self.txt1=Entry(self.f1,width=15,text="price",font=("times new roman",15,"bold"),bd=5,relief=SUNKEN,textvariable=self.sell_price).grid( row=6, column=5,padx=10,pady=10)
        self.lab2=Label(self.f1,text="Quantity",font=("times new roman",15,"bold"),fg="black").grid(row=8,column=3,padx=10,pady=10)
        self.txt2=Entry(self.f1,width=15,text="quantity",font=("times new roman",15,"bold"),bd=5,relief=SUNKEN,textvariable=self.quantity).grid( row=8, column=5,padx=10,pady=10)

        button1=Button(self.f1,text="Insert",bg="blue",fg="white",pady=5,width=8,font="arial 10 bold",command=self.getdata).place(x=40,y=250)
        button2=Button(self.f1,text="Show",bg="blue",fg="white",pady=5,width=8,font="arial 10 bold",command=self.showdata).place(x=130,y=250)
        button3=Button(self.f1,text="clear",bg="blue",fg="white",pady=5,width=8,font="arial 10 bold",command=self.cleardata).place(x=220,y=250)
        
        self.f2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Product List",font=("times new roman",15,"bold"),fg="Blue",bg='white')
        self.f2.place(x=360,y=10,width=800,height=400)
        verscroll=ttk.Scrollbar(self.f2,orient=VERTICAL)
                
        self.txttt=ttk.Treeview(self.f2,columns=('Product id','Name','Selling Price','Quantity'),yscrollcommand=verscroll.set)
        self.txttt.heading("Product id",text="Product Id")
        self.txttt.heading("Name",text="Name")
        self.txttt.heading("Selling Price",text="Selling Price")
        self.txttt.heading("Quantity",text="Quantity")
        self.txttt['show']='headings'
        self.txttt.column("Product id",width=60)
        self.txttt.column("Name",width=100)
        self.txttt.column("Selling Price",width=80)
        self.txttt.column("Quantity",width=80)
        verscroll.pack(side=RIGHT,fill=Y)
        verscroll.config(command=self.txttt.yview)
        self.txttt.pack(fill=BOTH,expand=1)
        
    def getdata(self):
        id=self.product_id.get()
        name=self.product_name.get()
        price=self.sell_price.get()
        quantity=self.quantity.get()
        
        connection=mysql.connector.connect(user="root",password="",host="localhost",database="inventorysys")
        if(id=="" or name=="" or price<1 or quantity<1 ):
            messagebox.showerror("Error","please fill in all the required details")      
        else:
            try:
                cursor=connection.cursor()
                insert_query=(
                            """INSERT INTO invdetail(p_id,product_name,selling_price,Quantity) VALUES(%s,%s,%s,%s)"""
                            )

                data=(id,name,price,quantity)
                cursor.execute(insert_query,data)
                connection.commit()
                messagebox.showinfo("Success","Insert Data Susscessfull")
                self.product_id.set("")
                self.product_name.set("")
                self.sell_price.set()
                self.quantity.set()
                
            except Error as e:
                messagebox.showerror("Error","Product Id already exist")
            
    def showdata(self):
        
            connection=mysql.connector.connect(user="root",password="",host="localhost",database="inventorysys")
            cursor=connection.cursor()
            My_Query="Select * from invdetail"
            cursor=connection.cursor()
            cursor.execute(My_Query)
            result=cursor.fetchall()   
            for i in result:
                self.txttt.insert("",END,values=i)

    def cleardata(self):
            for row in self.txttt.get_children():
                self.txttt.delete(row)
            self.product_id.set("")
            self.product_name.set("")
            self.sell_price.set()
            self.quantity.set()


root=Tk()
obj=window1(root)
root.mainloop()       
