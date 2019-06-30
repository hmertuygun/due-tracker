import webbrowser, os, json, random, time
from tabulate import tabulate
import tkinter as tk
from tkinter import ttk
import datetime        
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from tkinter import messagebox                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              

cred = credentials.Certificate('//add-file//')
firebase_admin.initialize_app(cred, {
    'databaseURL': '//file-url//'
})
LARGE_FONT= ("Verdana", 12)


class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo, PageThree):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)
    
    
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        print(cont)

    def getform(self, arr, swi):
        if swi == "yenivilla":
            new_arr = {
                "villa_no": arr[0],
                "ad_soyad": arr[1],
                "tel_no": arr[2],
                "email": arr[3],
                "address": arr[4]
            }
            print(new_arr)
            ref = db.reference('villalar')
            new_box_ref = ref.push(new_arr)
            if new_box_ref.key:
                messagebox.showinfo("Villa Eklendi", "İşlem başarıyla gerçekleşti.")

        elif swi == "odeme":
            new_arr = {
                "tip": arr[0],
                "villa_no": arr[1],
                "tutar": arr[2],
                "aciklama": arr[3],
                "ode_ay": arr[4]
            }
            print(new_arr)
            ref = db.reference('odemeler')
            new_box_ref = ref.push(new_arr)
            if new_box_ref.key:
                messagebox.showinfo("Ödeme Eklendi", "İşlem başarıyla gerçekleşti.")
        elif swi == "harcama":
            new_arr = {
                "tutar": arr[0],
                "aciklama": arr[1]
            }
            print(new_arr)
            ref = db.reference('harcamalar')
            new_box_ref = ref.push(new_arr)
            if new_box_ref.key:
                messagebox.showinfo("Harcama Eklendi", "İşlem başarıyla gerçekleşti.")

    def logs(self, cont, swd):
        if swd == "Aidat":
            ref = db.reference('odemeler')
            dat = ref.get()
            top = tk.Toplevel()
            e = 1
            b = tk.Label(top, text="Villa No", borderwidth=2, relief="groove")
            d = tk.Label(top, text="Açıklama", borderwidth=2, relief="groove")
            l = tk.Label(top, text="Ödenen Ay", borderwidth=2, relief="groove")
            f = tk.Label(top, text="Odenen Tutar", borderwidth=2, relief="groove")
            g = tk.Label(top, text="Kalan Borç", borderwidth=2, relief="groove")
            b.grid(row=0, column=0)
            d.grid(row=0, column=1)
            l.grid(row=0, column=2)
            f.grid(row=0, column=3)
            g.grid(row=0, column=4)

            for i in dat:
                if dat[i]["tip"] == "Aidat":
                    b = tk.Label(top, text=dat[i]["villa_no"], borderwidth=2, relief="groove")
                    d = tk.Label(top, text=dat[i]["aciklama"], borderwidth=2, relief="groove")
                    j = tk.Label(top, text=dat[i]["ode_ay"], borderwidth=2, relief="groove")
                    f = tk.Label(top, text=dat[i]["tutar"], borderwidth=2, relief="groove")
                    g = tk.Label(top, text="0", borderwidth=2, relief="groove")
                    b.grid(row=e, column=0)
                    d.grid(row=e, column=1)
                    j.grid(row=e, column=2)
                    f.grid(row=e, column=3)
                    g.grid(row=e, column=4)
                    print(i)
                    e = e + 1
        elif swd == "Bilgi":
            ref = db.reference('villalar')
            dat = ref.get()
            top = tk.Toplevel()
            e = 1
            b = tk.Label(top, text="Villa No", borderwidth=2, relief="groove")
            d = tk.Label(top, text="Ad Soyad", borderwidth=2, relief="groove")
            l = tk.Label(top, text="Adres", borderwidth=2, relief="groove")
            f = tk.Label(top, text="Email", borderwidth=2, relief="groove")
            g = tk.Label(top, text="Telefon", borderwidth=2, relief="groove")
            b.grid(row=0, column=0)
            d.grid(row=0, column=1)
            l.grid(row=0, column=2)
            f.grid(row=0, column=3)
            g.grid(row=0, column=4)

            for i in dat:
                b = tk.Label(top, text=dat[i]["villa_no"], borderwidth=2, relief="groove")
                d = tk.Label(top, text=dat[i]["ad_soyad"], borderwidth=2, relief="groove")
                j = tk.Label(top, text=dat[i]["address"], borderwidth=2, relief="groove")
                f = tk.Label(top, text=dat[i]["email"], borderwidth=2, relief="groove")
                g = tk.Label(top, text=dat[i]["tel_no"], borderwidth=2, relief="groove")
                b.grid(row=e, column=0)
                d.grid(row=e, column=1)
                j.grid(row=e, column=2)
                f.grid(row=e, column=3)
                g.grid(row=e, column=4)
                print(i)
                e = e + 1
        elif swd == "Odeme":
            ref = db.reference('odemeler')
            dat = ref.get()
            top = tk.Toplevel()
            e = 1
            b = tk.Label(top, text="Villa No", borderwidth=2, relief="groove")
            d = tk.Label(top, text="Açıklama", borderwidth=2, relief="groove")
            l = tk.Label(top, text="Ödenen Ay", borderwidth=2, relief="groove")
            f = tk.Label(top, text="Odenen Tutar", borderwidth=2, relief="groove")
            g = tk.Label(top, text="Kalan Borç", borderwidth=2, relief="groove")
            b.grid(row=0, column=0)
            d.grid(row=0, column=1)
            l.grid(row=0, column=2)
            f.grid(row=0, column=3)
            g.grid(row=0, column=4)

            for i in dat:
                if dat[i]["tip"] == "Ekstra":
                    b = tk.Label(top, text=dat[i]["villa_no"], borderwidth=2, relief="groove")
                    d = tk.Label(top, text=dat[i]["aciklama"], borderwidth=2, relief="groove")
                    j = tk.Label(top, text=dat[i]["ode_ay"], borderwidth=2, relief="groove")
                    f = tk.Label(top, text=dat[i]["tutar"], borderwidth=2, relief="groove")
                    g = tk.Label(top, text="0", borderwidth=2, relief="groove")
                    b.grid(row=e, column=0)
                    d.grid(row=e, column=1)
                    j.grid(row=e, column=2)
                    f.grid(row=e, column=3)
                    g.grid(row=e, column=4)
                    print(i)
                    e = e + 1
        elif swd == "Harcama":
            ref = db.reference('harcamalar')
            dat = ref.get()
            top = tk.Toplevel()
            e = 1
            b = tk.Label(top, text="Açıklama", borderwidth=2, relief="groove")
            d = tk.Label(top, text="Tutar", borderwidth=2, relief="groove")
            b.grid(row=0, column=0)
            d.grid(row=0, column=1)
            for i in dat:
                b = tk.Label(top, text=dat[i]["aciklama"], borderwidth=2, relief="groove")
                d = tk.Label(top, text=dat[i]["tutar"], borderwidth=2, relief="groove")
                b.grid(row=e, column=0)
                d.grid(row=e, column=1)
                print(i)
                e = e + 1
        

        
    def newIPFrame(self, cont):
        top = tk.Toplevel()
        tk.Label(top, text="Villa Numarası").grid(row=0, padx=5, pady=5)
        tk.Label(top, text="Adı Soyadı").grid(row=1, padx=5, pady=5)
        tk.Label(top, text="Telefon No").grid(row=2, padx=5, pady=5)
        tk.Label(top, text="E-mail").grid(row=3, padx=5, pady=5)
        tk.Label(top, text="Adres").grid(row=4, padx=5, pady=5)

        e1 = tk.Entry(top)
        e2 = tk.Entry(top)
        e3 = tk.Entry(top)
        e4 = tk.Entry(top)
        e5 = tk.Entry(top)

        e1.grid(row=0, column=1, padx=5, pady=5)
        e2.grid(row=1, column=1, padx=5, pady=5)
        e3.grid(row=2, column=1, padx=5, pady=5)
        e4.grid(row=3, column=1, padx=5, pady=5)
        e5.grid(row=4, column=1, padx=5, pady=5)
        button1 = tk.Button(top, text="Kaydet",
                            command=lambda: self.getform([e1.get(), e2.get(), e3.get(), e4.get(),e5.get()], "yenivilla"))
        button1.grid(row=6, column=1 , padx=10, pady=10)
    def odeme(self, cont):
        top = tk.Toplevel()
        tk.Label(top, text="Ödeme Tipi").grid(row=0, padx=5, pady=5)
        tk.Label(top, text="Villa Numarası").grid(row=1, padx=5, pady=5)
        tk.Label(top, text="Tutar").grid(row=2, padx=5, pady=5)
        tk.Label(top, text="Açıklama").grid(row=3, padx=5, pady=5)
        tk.Label(top, text="Ödenen Ay").grid(row=4, padx=5, pady=5)

        c1 = ttk.Combobox(top, values=["Ekstra", "Aidat"])
        e2 = tk.Entry(top)
        e3 = tk.Entry(top)
        e4 = tk.Entry(top)
        c2 = ttk.Combobox(top, values=["Ocak", "Şubat", "Mart", "Nisan","Mayıs", "Haziran","Temmuz", "Ağustos","Eylül", "Ekim","Kasım", "Aralık",])

        c1.grid(row=0, column=1, padx=5, pady=5)
        e2.grid(row=1, column=1, padx=5, pady=5)
        e3.grid(row=2, column=1, padx=5, pady=5)
        e4.grid(row=3, column=1, padx=5, pady=5)
        c2.grid(row=4, column=1, padx=5, pady=5)
        button1 = tk.Button(top, text="Kaydet",
                            command=lambda: self.getform([c1.get(), e2.get(), e3.get(), e4.get(),c2.get()], "odeme"))
        button1.grid(row=6, column=1 , padx=10, pady=10)

    def harcama(self, cont):
        top = tk.Toplevel()
        tk.Label(top, text="Tutar").grid(row=0, padx=5, pady=5)
        tk.Label(top, text="Açıklama").grid(row=1, padx=5, pady=5)

        e1 = tk.Entry(top)
        e2 = tk.Entry(top)

        e1.grid(row=0, column=1, padx=5, pady=5)
        e2.grid(row=1, column=1, padx=5, pady=5)
        button1 = tk.Button(top, text="Kaydet",
                            command=lambda: self.getform([e1.get(), e2.get()], "harcama"))
        button1.grid(row=6, column=1 , padx=10, pady=10)
        
        
        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Site Takip Sistemi", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        button4 = tk.Button(self, text="Villalar",
                            command=lambda: controller.show_frame(PageTwo))
        button4.pack(side=tk.LEFT, padx=5, pady=5)

        button4 = tk.Button(self, text="Ödemeler",
                            command=lambda: controller.show_frame(PageThree))
        button4.pack(side=tk.LEFT, padx=5, pady=5)

        button2 = tk.Button(self, text="Harcamalar",
                            command=lambda:  controller.show_frame(PageOne))
        button2.pack(side=tk.LEFT, padx=5, pady=5)

        button2 = tk.Button(self, text="Villa Ekle",
                            command=lambda: controller.newIPFrame("ipPage"))
        button2.pack(side=tk.LEFT, padx=5, pady=5)
        

class PageTwo(tk.Frame):
    
     def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Villalar", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        button1 = tk.Button(self, text="Aidatlar",
                            command=lambda: controller.logs("ipPage", "Aidat"))
        button1.pack(side=tk.LEFT, padx=5, pady=5)
        button1 = tk.Button(self, text="Villa Bilgileri",
                            command=lambda: controller.logs("ipPage", "Bilgi"))
        button1.pack(side=tk.LEFT, padx=5, pady=5)

        button2 = tk.Button(self, text="Geri Dön",
                            command=lambda: controller.show_frame(StartPage))
        button2.pack(side=tk.LEFT, padx=5, pady=5)
class PageThree(tk.Frame):
    
     def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Ödemeler", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        button1 = tk.Button(self, text="Ödeme Geçmişi",
                            command=lambda: controller.logs("ipPage", "Odeme"))
        button1.pack(side=tk.LEFT, padx=5, pady=5)
        button1 = tk.Button(self, text="Ödeme Ekle",
                            command=lambda: controller.odeme("ipPage"))
        button1.pack(side=tk.LEFT, padx=5, pady=5)

        button2 = tk.Button(self, text="Geri Dön",
                            command=lambda: controller.show_frame(StartPage))
        button2.pack(side=tk.LEFT, padx=5, pady=5)

class PageOne(tk.Frame):
    
     def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Harcamalar", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        button1 = tk.Button(self, text="Harcama Geçmişi",
                            command=lambda: controller.logs("ipPage", "Harcama"))
        button1.pack(side=tk.LEFT, padx=5, pady=5)
        button1 = tk.Button(self, text="Harcama Ekle",
                            command=lambda: controller.harcama("ipPage"))
        button1.pack(side=tk.LEFT, padx=5, pady=5)

        button2 = tk.Button(self, text="Geri Dön",
                            command=lambda: controller.show_frame(StartPage))
        button2.pack(side=tk.LEFT, padx=5, pady=5)



app = SeaofBTCapp()
app.title("Site Yönetim Sistemi")
app.mainloop()
