from tkinter import *

import tkinter.messagebox

class Library:

	def __init__(self,root):
		self.root = root
		self.root.title("Library Management System")
		self.root.geometry("1350x750+0+0")

		MTy = StringVar()
		Ref = StringVar()
		Tit = StringVar()
		fna = StringVar()
		sna = StringVar()
		Adr1 = StringVar()
		Adr2 = StringVar()
		pcd = StringVar()
		MNo = StringVar()
		BkID = StringVar()
		Bkt = StringVar()
		BkT = StringVar()
		Atr = StringVar()
		DBo = StringVar()
		Ddu = StringVar()
		sPr = StringVar()
		LrF = StringVar()
		DoD = StringVar()
		DonL = StringVar()

		#===============================================Frames==============

		MainFrame = Frame(self.root)
		MainFrame.grid()

		TitFrame = Frame(MainFrame,bd =2, padx=40, pady=8,bg = "Cadet blue",relief = RIDGE )
		TitFrame.pack(side = TOP)

		self.lblTit = Label(TitFrame, font=('arial',46,'bold'),text="Library Management System")

		self.lblTit.grid(sticky=W)

		ButtonFrame = Frame(MainFrame,bd=2,width=1350,height=100,padx=20,pady=20,bg="Cadet Blue",relief=RIDGE)
		ButtonFrame.pack(side=BOTTOM)

		FrameDetail = Frame(MainFrame,bd=0,width=1350,height=50,padx=20,relief=RIDGE)
		FrameDetail.pack(side=BOTTOM)

		DataFrame = Frame(MainFrame,bd=1,width=1300,height=400,padx=20,pady=20,relief=RIDGE)
		DataFrame.pack(side=BOTTOM)

		DataFrameLEFT = LabelFrame(DataFrame , bd=1,width=800,height=300,padx=20,relief=RIDGE
						,font=('arial',12,"bold"),text="Library Membership Info:",bg="Cadet Blue")

		DataFrameLEFT.pack(side=LEFT)

		DataFrameRIGHT = LabelFrame(DataFrame,bd =1,width=450,height=300,padx=20,pady=3,relief=RIDGE
							,font=('arial',12,"bold"),text="Book Details:",bg="Cadet Blue")

		DataFrameRIGHT.pack(side=RIGHT)


		#===============================================Frames==============

		self.lblMemberType = Label(DataFrameLEFT,font=('arial',12,'bold'),text="Member Type",padx=2,pady=2,
								bg="Cadet Blue")
		self.lblMemberType.grid(row=0,column=0,sticky=W)

		self.txtMType = Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=MTy,width=25)
		self.txtMType.grid(row=0,column=1)



		self.lblBkID = Label(DataFrameLEFT,font=('arial',12,'bold'),text="Book ID",padx=2,pady=2,
								bg="Cadet Blue")
		self.lblBkID.grid(row=0,column=2,sticky=W)
		self.txtBkID = Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=BkID,width=25)
		self.txtBkID.grid(row=0,column=3)


		self.lblRef = Label(DataFrameLEFT,font=('arial',12,'bold'),text="Reference No:",padx=2,pady=2,
								bg="Cadet Blue")
		self.lblRef.grid(row=1,column=0,sticky=W)
		self.txtRef = Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=Ref,width=25)
		self.txtRef.grid(row=1,column=1)


		self.lblBkt = Label(DataFrameLEFT,font=('arial',12,'bold'),text="Book Title",padx=2,pady=2,
								bg="Cadet Blue")
		self.lblBkt.grid(row=1,column=2,sticky=W)
		self.txtBkt = Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=Bkt,width=25)
		self.txtBkt.grid(row=1,column=3)


		self.lblTit = Label(DataFrameLEFT,font=('arial',12,'bold'),text="Title",padx=2,pady=2,
								bg="Cadet Blue")
		self.lblTit.grid(row=2,column=0,sticky=W)
		self.txtTit = Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=Tit,width=25)
		self.txtTit.grid(row=2,column=1)


		self.lblAtr = Label(DataFrameLEFT,font=('arial',12,'bold'),text="Author",padx=2,pady=2,
								bg="Cadet Blue")
		self.lblAtr.grid(row=2,column=2,sticky=W)
		self.txtAtr = Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=Atr,width=25)
		self.txtAtr.grid(row=2,column=3)


		self.lblfna = Label(DataFrameLEFT,font=('arial',12,'bold'),text="Firstname",padx=2,pady=2,
								bg="Cadet Blue")
		self.lblfna.grid(row=3,column=0,sticky=W)
		self.txtfna = Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=fna,width=25)
		self.txtfna.grid(row=3,column=1)


		self.lblDBo = Label(DataFrameLEFT,font=('arial',12,'bold'),text="Date Borrowed:",padx=2,pady=2,
								bg="Cadet Blue")
		self.lblDBo.grid(row=3,column=2,sticky=W)
		self.txtDBo = Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=DBo,width=25)
		self.txtDBo.grid(row=3,column=3)


		self.lblsna = Label(DataFrameLEFT,font=('arial',12,'bold'),text="Surname",padx=2,pady=2,
								bg="Cadet Blue")
		self.lblsna.grid(row=4,column=0,sticky=W)
		self.txtsna = Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=sna,width=25)
		self.txtsna.grid(row=4,column=1)


		self.lblDdu = Label(DataFrameLEFT,font=('arial',12,'bold'),text="Date due:",padx=2,pady=2,
								bg="Cadet Blue")
		self.lblDdu.grid(row=4,column=2,sticky=W)
		self.txtDdu = Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=Ddu,width=25)
		self.txtDdu.grid(row=4,column=3)


		self.lblAdr1 = Label(DataFrameLEFT,font=('arial',12,'bold'),text="Address 1:",padx=2,pady=2,
								bg="Cadet Blue")
		self.lblAdr1.grid(row=5,column=0,sticky=W)
		self.txtAdr1 = Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=Adr1,width=25)
		self.txtAdr1.grid(row=5,column=1)


		self.lblDonL = Label(DataFrameLEFT,font=('arial',12,'bold'),text="Days on loan:",padx=2,pady=2,
								bg="Cadet Blue")
		self.lblDonL.grid(row=5,column=2,sticky=W)
		self.txtDonL = Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=DonL,width=25)
		self.txtDonL.grid(row=5,column=3)


		self.lblAdr2 = Label(DataFrameLEFT,font=('arial',12,'bold'),text="Address 2:",padx=2,pady=2,
								bg="Cadet Blue")
		self.lblAdr2.grid(row=6,column=0,sticky=W)
		self.txtAdr2 = Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=Adr2,width=25)
		self.txtAdr2.grid(row=6,column=1)


		self.lblLrF = Label(DataFrameLEFT,font=('arial',12,'bold'),text="Late return fine:",padx=2,pady=2,
								bg="Cadet Blue")
		self.lblLrF.grid(row=6,column=2,sticky=W)
		self.txtLrF = Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=LrF,width=25)
		self.txtLrF.grid(row=6,column=3)



		self.lblpcd = Label(DataFrameLEFT,font=('arial',12,'bold'),text="Post Code",padx=2,pady=2,
								bg="Cadet Blue")
		self.lblpcd.grid(row=7,column=0,sticky=W)
		self.txtpcd = Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=pcd,width=25)
		self.txtpcd.grid(row=7,column=1)


		self.lblDoD = Label(DataFrameLEFT,font=('arial',12,'bold'),text="Date over due",padx=2,pady=2,
								bg="Cadet Blue")
		self.lblDoD.grid(row=7,column=2,sticky=W)
		self.txtDoD = Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=DoD,width=25)
		self.txtDoD.grid(row=7,column=3)


		self.lblMNo = Label(DataFrameLEFT,font=('arial',12,'bold'),text="Mobile No:",padx=2,pady=2,
								bg="Cadet Blue")
		self.lblMNo.grid(row=8,column=0,sticky=W)
		self.txtMNo = Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=MNo,width=25)
		self.txtMNo.grid(row=8,column=1)


		self.lblsPr = Label(DataFrameLEFT,font=('arial',12,'bold'),text="Selling Price",padx=2,pady=2,
								bg="Cadet Blue")
		self.lblsPr.grid(row=8,column=2,sticky=W)
		self.txtsPr = Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=sPr,width=25)
		self.txtsPr.grid(row=8,column=3)







if __name__ == "__main__":
	root = Tk()
	application = Library(root)
	root.mainloop()
