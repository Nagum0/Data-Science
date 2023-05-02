import mysql.connector
import tkinter as tk 

class UserLeaveWindow(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        #Screen config
        self.title("User leave window")
        self.geometry("300x300")
        self.resizable(False, False)

        """ MySQL CONNECTION """
        self.user_DB = mysql.connector.connect(
            host="b9zwuf9k9awvthq1z5r1-mysql.services.clever-cloud.com",
            user="ubhyrtpkdvjshhsa",
            password="Nul8kN9sDTonpg30CZZr",
            database="b9zwuf9k9awvthq1z5r1"
        )

        """ MySQL CURSOR """
        self.user_cursor = self.user_DB.cursor()

        #Mainloop
        self.drawWidgets()
        self.placeWidgets()
        self.mainloop()

    def drawWidgets(self) -> None:
        self.enter_ID_lbl = tk.Label(self, text="Enter ID")
        self.enter_ID_entry = tk.Entry(self, width=25)
        self.fee_label = tk.Label(self, text="Fee: ?€")
        self.pay_charge_btn = tk.Button(self, text="Pay Charge", command=self.payCharge, height=3, width=15)

    def placeWidgets(self) -> None:
        self.enter_ID_lbl.pack(pady=30)
        self.enter_ID_entry.pack()
        self.fee_label.pack(pady=10)
        self.pay_charge_btn.pack(pady=20)

    def getEntryValue(self) -> str:
        return self.enter_ID_entry.get()

    def checkID(self) -> bool:
        self.user_cursor.execute(
            str("SELECT ticket_ID FROM Tickets WHERE ticket_ID = %s"), (self.getEntryValue(), )
        )

        temp_ID = self.user_cursor.fetchone()

        if temp_ID is not None:
            return True
        else:
            return False

    def changeFeeLabel(self) -> None:
        self.user_cursor.execute(
            str("SELECT fee FROM Tickets WHERE ticket_ID = %s"), (self.getEntryValue(), )
        )

        temp_fee = self.user_cursor.fetchone()[0]
        self.fee_label['text'] = f"Fee: {temp_fee}€"

    def payCharge(self) -> None:
        if self.checkID():
            self.changeFeeLabel()
            self.user_cursor.execute(
                str("UPDATE Tickets SET charge = %s WHERE ticket_ID = %s AND charge = %s"), ("paid", self.getEntryValue(), "unpaid")
            )
            self.user_DB.commit()
        else:
            print("Incorrect ID")

if __name__ == "__main__":
    user_leave = UserLeaveWindow()