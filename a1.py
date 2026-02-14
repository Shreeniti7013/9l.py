import tkinter as tk
from tkinter import ttk,messagebox

class Restro:
    def __init__(self,root):
       self.root=root
       self.root.title("Resturant Managment")
       self. menu_items={
           "Burger":200,
           "Pizza":400
       }
       bgwidth,bgheight=600,600
       canvas=tk.Canvas(root,width=bgwidth,height=bgheight)
       canvas.pack()
       frame=ttk.Frame(root)
       frame.place(relx=0.5,rely=0.5,anchor=tk.CENTER)
       ttk.Label(frame,text="Pizza Express Resturant")
       self.menu_label={}
       self.menu_quantity={}
       for i,(item,price)in enumerate(self.menu_items.items(),start=1):
           label=ttk.Label(frame,text=f"{item}(Rs{price}:")
           label.grid(row=i,column=0,padx=10,pady=5)
           self.menu_label[item]=label
           quantity_entry=ttk.Entry(frame,width=5)
           quantity_entry.grid(row=i,column=1,padx=10,pady=5)
            
           self.menu_quantity[item]=quantity_entry

       order_button=ttk.Button(frame,text="Place Order",command=self.place_order)
       order_button.grid(row=len(self.menu_items)+2,columnspan=3,padx=10,pady=10)
    def place_order(self):
       total_cost=0
       order_summary="Order Summary:\n"
       symbol="$"
       for item,entry in self.menu_quantity.items():
          quantity=entry.get()
          price=self.menu_items[item]
          cost=quantity*price
          total_cost+=cost
          order_summary+=f"{item}:{quantity}X {symbol}{price}={symbol}{cost}\n"
if __name__=="__main__":
   root=tk.Tk()
   app=Restro(root)
   root.geometry("600x600")