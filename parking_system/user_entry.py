import mysql.connector
import tkinter as tk
import random

""" USER WINDOW CLASS """
class UserEntryWindow(tk.Tk):
    def __init__(self, argDB: any, argCursor: any) -> None:
        super().__init__()
        self.title("Parking system - user entry")
        self.geometry("300x300")
        self.resizable(False, False)

        #Variables
        self.argDB = argDB
        self.argCursor = argCursor

        self.getTicketLbl = tk.Label(master=self, 
                                    text="TICKET", 
                                    font="Calibri 20 bold")
        self.getTickerBtn = tk.Button(master=self, 
                                    text="Get ticket",
                                    width=15, 
                                    command=self.getTicket)

        #Mainloop
        self.packWidgets()
        self.mainloop()

    #Get ticket function
    def getTicket(self) -> None:
        sql = "INSERT INTO `Tickets` (ticket_date, ticket_time, parking_time, fee, ticket_ID) VALUES (CURRENT_DATE, CURRENT_TIME, %s, %s, %s)"
        val = (0, 0, self.genTicketID())
        self.argCursor.execute(sql, val)
        self.argDB.commit()

    #Generate ticketID
    def genTicketID(self) -> str:
        genID = ""
        abc = "QWERTYUIOPASDFGHJKLZXCVBNM"
        nums = "123456789"

        for i in range(5):
            if i == 0:
                randNum = nums[random.randrange(len(nums))]
                genID = genID + randNum
            elif i % 2 == 0:
                randLetter = abc[random.randrange(len(abc))]
                genID = genID + randLetter
            else:
                randNum = nums[random.randrange(len(nums))]
                genID = genID + randNum

        return genID

    #Pack function
    def packWidgets(self) -> None:
        self.getTicketLbl.pack(pady=50)
        self.getTickerBtn.pack()


""" DATABASE CONNECTION """
mainDB = mysql.connector.connect(
    host="b9zwuf9k9awvthq1z5r1-mysql.services.clever-cloud.com",
    user="ubhyrtpkdvjshhsa",
    password="Nul8kN9sDTonpg30CZZr",
    database="b9zwuf9k9awvthq1z5r1"
)

""" CURSOR """
mainCursor = mainDB.cursor()

""" MAIN DRIVER """
if __name__ == "__main__":
    userWindow = UserEntryWindow(mainDB, mainCursor)