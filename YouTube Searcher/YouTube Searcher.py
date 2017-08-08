import requests
from bs4 import BeautifulSoup
from tkinter import *
import webbrowser
from PIL import ImageTk,Image

isim1 = []
link1 = []

class YouTube:
    def main_window(self):
        window = Tk()
        window.title("Youtube Search")
        def get():
            search = text.get()
            sınıf = YouTube()
            ara = sınıf.search(search)
            sınıf.result(ara)
            sınıf.result_window()

        window.geometry("200x100")
        text = Entry()
        text.pack(pady=15,padx=10)
        buton = Button(text="Search", command=get)
        buton.pack()

        mainloop()

    def result_window(self):
        winndow=Toplevel()
        winndow.title("Results")
        winndow.maxsize(width=1230,height=726)
        def on_configure(event):
            # update scrollregion after starting 'mainloop'
            # when all widgets are in canvas
            canvas.configure(scrollregion=canvas.bbox('all'))

        def open_link(url):
            url = "https://www.youtube.com" + url
            webbrowser.open_new(url)

        canvas = Canvas(winndow)
        canvas.pack(side=LEFT)
        canvas.config(width=968, height=550)

        scrollbar = Scrollbar(winndow, command=canvas.yview)
        scrollbar.pack(side=LEFT, fill='y')

        canvas.configure(yscrollcommand=scrollbar.set)

        # update scrollregion after starting 'mainloop'
        # when all widgets are in canvas
        canvas.bind('<Configure>', on_configure)

        # --- put frame in canvas ---

        frame = Frame(canvas)
        canvas.create_window((0, 0), window=frame, anchor='nw')
        for i, url in enumerate(link1):
            img = PhotoImage(file='')
            cerceve=Frame(frame, width=963, height=188,borderwidth=4,relief=SUNKEN)
            cerceve.pack()
            cerceve.pack_propagate(False)
            panel = Button(cerceve, image=img,text="THUMBNAIL",height = 188, width = 300)
            panel.pack()
            panel.place(x=0,y=0)
            yazi = Label(cerceve, text="{}".format(isim1[i]), fg="blue", cursor="hand2",)
            yazi.pack()
            yazi.place(x=400,y=75)
            yazi.bind("<Button-1>", lambda i, url=url: open_link(url))

    def search(self,gelen):
        arama = gelen
        arti = "+"
        asd = arama.split(' ')
        search = "https://www.youtube.com/results?search_query=" + arti.join(asd)
        return search

    def result(self,link):
        r = requests.get(link)
        soup = BeautifulSoup(r.content, "html.parser")
        all_data = soup.find_all("ol", {"class": "section-list"})

        ol = (all_data[0].contents)[len(all_data[0].contents)-2]
        ol = ol.find_all("div", {"class": "yt-lockup-content"})
        for i in ol:
            title = i.find_all("h3", {"class": "yt-lockup-title "})
            title2 = title[0].text
            isim1.append(title2)
        for film in ol:
            title = film.find_all("h3", {"class": "yt-lockup-title "})
            for a in title[0].find_all('a', href=True):
                link = a['href']
                link1.append(link)



deneme = YouTube()
deneme.main_window()