from tkinter import *
from tkinter import messagebox

app = Tk()
app.title('Aplikasi Kasir')

# variabel
sekop = StringVar()
semen = StringVar()
paku = StringVar()
meteran = StringVar()
tekstotal = StringVar()
teksaung = StringVar()
total = 0

# buat function
def totalbeli():
    global sekop, semen, paku, meteran, tekstotal, total
    hsekop = int(sekop.get()) * 3000
    hsemen = int(semen.get()) * 4500
    hpaku = int(paku.get()) * 2000
    hmeteran = int(meteran.get()) * 1500
    total = hsekop + hsemen + hpaku + hmeteran
    tekstotal.set(str(total))

def kembalian():
    global total
    uang = int(teksaung.get())

    if uang >= total:
        kembalian = uang - total
        messagebox.showinfo(message='Kembalian kamu sebesar {}'.format(str(kembalian)))
    else:
        messagebox.showerror(message='maaf uang kamu kurang')

def clear():
        sekop.set('0')
        semen.set('0')
        paku.set('0')
        meteran.set('0')
        tekstotal.set('0')
        teksaung.set('0')


app.geometry('750x600') # membuat ukuran
app.configure(bg='#31c6d4') # membuat backgroung warna

# membuat properti tulisan title
Label(app, text='TOKO ALAT DAI', bg='#31c6d4', foreground='#fef5ac', font='arial 18 bold').place(x=260,y=30)

# membuat label nama menu
Label(app, text='1. sekop', bg='#31c6d4', foreground='#fef5ac', font='arial 12 bold').place(x=100,y=100)
Label(app, text='2. semen 1 karung', bg='#31c6d4', foreground='#fef5ac', font='arial 12 bold').place(x=100,y=140)
Label(app, text='3. paku 1 bungkus', bg='#31c6d4', foreground='#fef5ac', font='arial 12 bold').place(x=100,y=180)
Label(app, text='4. meteran', bg='#31c6d4', foreground='#fef5ac', font='arial 12 bold').place(x=100,y=220)

# membuat label harga
Label(app, text='Rp. 3000', bg='#31c6d4', foreground='#fef5ac', font='arial 12 bold').place(x=350,y=100)
Label(app, text='Rp. 4500', bg='#31c6d4', foreground='#fef5ac', font='arial 12 bold').place(x=350,y=140)
Label(app, text='Rp. 2000', bg='#31c6d4', foreground='#fef5ac', font='arial 12 bold').place(x=350,y=180)
Label(app, text='Rp. 1500', bg='#31c6d4', foreground='#fef5ac', font='arial 12 bold').place(x=350,y=220)

# membuat spinbox
Spinbox(app, from_=0, to=100, width=4, font='arial 10', textvariable=sekop, command=totalbeli).place(x=550,y=100)
Spinbox(app, from_=0, to=100, width=4, font='arial 10', textvariable=semen, command=totalbeli).place(x=550,y=140)
Spinbox(app, from_=0, to=100, width=4, font='arial 10', textvariable=paku, command=totalbeli).place(x=550,y=180)
Spinbox(app, from_=0, to=100, width=4, font='arial 10', textvariable=meteran, command=totalbeli).place(x=550,y=220)

# membuat label pembayaran
Label(app, text='Masukan uang anda', bg='#31c6d4', foreground='#fef5ac', font='arial 12 ').place(x=100,y=280)

# membuat entry jumlah uang
Entry(app, textvariable=teksaung).place(x=100,y=300)

# membuat label total
Label(app, text='Rp. ', bg='#31c6d4', foreground='#fef5ac', font='arial 12 bold').place(x=350,y=300)
Label(app, textvariable=tekstotal, bg='#31c6d4', foreground='#fef5ac', font='arial 12 bold').place(x=380,y=300)

# membuat tombol
Button(app, text='Total', foreground='white', bg='#36ae7c', width=10, command=kembalian).place(x=100,y=400)
Button(app, text='Clear', foreground='white', bg='#ff1e1e', width=10, command=clear).place(x=250,y=400)

# footer text
Label(app, text='Modify', bg='#31c6d4', foreground='#fef5ac', font='arial 10 ').place(x=360,y=550)

app.mainloop() # menampilkan aplikasi