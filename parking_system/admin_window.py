import mysql.connector
import tkinter as tk

class AdminWindow(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        """ Window setup """
        self.title("Parking system - admin")
        self.geometry("400x300")
        self.resizable(False, False)

        """ MySQL CONNECTION """
        self.admin_DB = mysql.connector.connect(
            host="b9zwuf9k9awvthq1z5r1-mysql.services.clever-cloud.com",
            user="ubhyrtpkdvjshhsa",
            password="Nul8kN9sDTonpg30CZZr",
            database="b9zwuf9k9awvthq1z5r1"
        )

        """ MySQL CURSOR """
        self.admin_cursor = self.admin_DB.cursor()

        self.drawWidgets()
        self.packWidgets()
    
        #Mainloop
        self.mainloop()

    """ METHODS """
    def drawWidgets(self) -> None:
        self.id_label = tk.Label(self, text="Ticket ID")
        self.id_entry = tk.Entry(self, width=20)
        self.check_id_btn = tk.Button(self, text="Calculate Fee", command=self.sendFee)
        self.show_fee_label = tk.Label(self, text="Fee: 10€")

    def packWidgets(self) -> None:
        self.id_label.place(x=180, y=50)
        self.id_entry.place(x=140, y=75)
        self.check_id_btn.pack(pady=100)
        self.show_fee_label.place(x=175, y=140)

    def getEntryValue(self) -> str:
        return str(self.id_entry.get())

    """ SQL FUNCTIONALITY """
    def sendFee(self) -> None:
        print(self.calcFee())

    def findTicketTimeHour(self) -> int:
        self.admin_cursor.execute(str("SELECT ticket_time FROM Tickets WHERE ticket_ID = %s"), (self.getEntryValue(), ))
        ticket_time = str(self.admin_cursor.fetchall()[0][0])
        
        if ticket_time[0].isdigit() and ticket_time[1].isdigit():
            return int(ticket_time[0] + ticket_time[1])
        else:
            return int(ticket_time[0])

    def calcFee(self) -> float:
        self.admin_cursor.execute(
            str("UPDATE Tickets SET pay_time = CURRENT_TIME WHERE ticket_ID = %s AND charge = %s"), (self.getEntryValue(), "unpaid")
        )
        self.admin_DB.commit()

        self.admin_cursor.execute(str("SELECT pay_time FROM Tickets WHERE ticket_ID = %s"), (self.getEntryValue(), ))

        pay_time = str(self.admin_cursor.fetchall()[0][0])

        if pay_time[0].isdigit() and pay_time[1].isdigit():
            pay_time_hour = int(pay_time[0] + pay_time[1])
            fee = (pay_time_hour - self.findTicketTimeHour()) * 1.5
        else:
            pay_time_hour = int(pay_time[0])
            fee = (pay_time_hour - self.findTicketTimeHour()) * 1.5

        if fee == 1.5:
            return 0.0
        else:
            return fee

if __name__ == "__main__":
    admin_window = AdminWindow()