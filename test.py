# #Importaciones necesarias...
# from Tkinter import *
# import tkMessageBox
# import bluetooth
# import RPi.GPIO as GPIO 
# from NeuroPy import NeuroPy
# import matplotlib.pyplot as plt
# from time import sleep

# GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False) 

# st1 = 26
# st2 = 21
# st3 = 20
# st4 = 19
# st5 = 16
# st6 = 13

# GPIO.setup(st1, GPIO.OUT) 
# GPIO.setup(st2, GPIO.OUT)
# GPIO.setup(st3, GPIO.OUT)
# GPIO.setup(st4, GPIO.OUT)
# GPIO.setup(st5, GPIO.OUT)
# GPIO.setup(st6, GPIO.OUT)

# promedio = []
# dat_lalfa = []
# dat_halfa = []
# dat_lbeta = []
# dat_hbeta = []
# dat_lgama = []
# dat_mgama = []
# att=0
# lga=0
# mga=0
# lbe=0
# hbe=0  

# def defcoman():
#     def guarda():
#         global att
#         global lga
#         global mga
#         global lbe
#         global hbe

#         att=float(caja1.get())
#         lga=float(caja2.get())
#         mga=float(caja3.get())
#         lbe=float(caja4.get())
#         hbe=float(caja5.get())
#         tkMessageBox.showinfo("Configuración","Éxito en la configuración ")
#         caja1.delete(0,20)
#         caja2.delete(0,20)
#         caja3.delete(0,20)
#         caja4.delete(0,20)
#         caja5.delete(0,20)
#         gui2.destroy()
       
#     gui2=Toplevel()
#     gui2.title("Definir rangos")
#     gui2.geometry("310x380+405+35")
#     boton4=Button(gui2,text='Cancelar',command=gui2.destroy)
#     boton4.grid(row=6, column=1,padx=5,pady=5)
#     boton5=Button(gui2,text='Ok',command=guarda)
#     boton5.grid(row=6, column=0,padx=5,pady=5)
#     label=Label(gui2)
#     label.grid(row=0, column=0,padx=20,pady=30)
#     Label(gui2,text="  Ingresar los Rangos  ",relief="groove",font=(18),fg="blue",height = 2).place(x=65,y=20)
#     #1
#     var1 = StringVar()
#     var1.set("Defina atención:")
#     label1 = Label(gui2,textvariable=var1,height = 2)
#     label1.grid(row=1, column=0,padx=10,pady=10)

#     numero1=StringVar()
#     caja1=Entry(gui2,bd=4,textvariable=numero1)
#     caja1.grid(row=1, column=1)
#     caja1.config(justify="center")
#     #2
#     var2 = StringVar()
#     var2.set("Defina low gama:")
#     label2 = Label(gui2,textvariable=var2,height = 2)
#     label2.grid(row=2, column=0,padx=10,pady=10)
        
#     numero2=StringVar()
#     caja2=Entry(gui2,bd=4,textvariable=numero2)
#     caja2.grid(row=2, column=1)
#     caja2.config(justify="center")
#     #3
#     var3 = StringVar()
#     var3.set("Defina Mid Gama:")
#     label3 = Label(gui2,textvariable=var3,height = 2)
#     label3.grid(row=3, column=0,padx=10,pady=10)

#     numero3=StringVar()
#     caja3=Entry(gui2,bd=4,textvariable=numero3)
#     caja3.grid(row=3, column=1)
#     caja3.config(justify="center")
#     #4
#     var4 = StringVar()
#     var4.set("Defina Low Beta:")
#     label4 = Label(gui2,textvariable=var4,height = 2)
#     label4.grid(row=4, column=0,padx=10,pady=10)

#     numero4=StringVar()
#     caja4=Entry(gui2,bd=4,textvariable=numero4)
#     caja4.grid(row=4, column=1)
#     caja4.config(justify="center")
#     #5
#     var5 = StringVar()
#     var5.set("Defina High Beta:")
#     label5 = Label(gui2,textvariable=var5,height = 2)
#     label5.grid(row=5, column=0,padx=10,pady=10)

#     numero5=StringVar()
#     caja5=Entry(gui2,bd=4,textvariable=numero5)
#     caja5.grid(row=5, column=1)
#     caja5.config(justify="center")
    
# def conexion():
#     global neuropy
#     neuropy = NeuroPy("/dev/rfcomm1", 57600) 
#     neuropy.start()
#     sleep(2)
#     tkMessageBox.showinfo("Conexión", "  Conexión realizada  ")
#     #tkMessageBox.showwarning("Error"," Sensor sin Medición ")
    
# def grafica():
#     tkMessageBox.showwarning("Gráfica","Cierre la gráfica para continuar ")
#     a = dat_lalfa
#     b = dat_halfa
#     c = dat_lbeta
#     d = dat_hbeta
#     e = dat_lgama
#     f = dat_mgama
#     plt.plot(a)
#     plt.plot(b)
#     plt.plot(c)
#     plt.plot(d)
#     plt.plot(e)
#     plt.plot(f)
#     plt.ylim(ymax=200000)
#     plt.ylim(ymin=0)
#     plt.xlim(xmax=15)
#     plt.xlim(xmin=0)
#     plt.title("Medicion")
#     plt.xlabel("Tiempo")
#     plt.ylabel("Valor")
#     plt.plot(a,marker='.',linestyle='-',color='g',label="Low Alfa")
#     plt.plot(b,marker='.',linestyle='-',color='b',label="High Alfa")
#     plt.plot(c,marker='.',linestyle='-',color='r',label="Low Beta")
#     plt.plot(d,marker='.',linestyle='-',color='y',label="High Beta")
#     plt.plot(e,marker='.',linestyle='-',color='m',label="Low Gama")
#     plt.plot(f,marker='.',linestyle='-',color='c',label="Mid Gama")
#     plt.legend(loc="upper right")
#     plt.show()
    
# def lectura():
#     if neuropy.attention != 0:
#         global dat_lalfa
#         global dat_halfa
#         global dat_lbeta
#         global dat_hbeta
#         global dat_lgama
#         global dat_mgama
#         promedio = []
#         dat_lalfa = []
#         dat_halfa = []
#         dat_lbeta = []
#         dat_hbeta = []
#         dat_lgama = []
#         dat_mgama = []
#         p_lalfa = 0
#         p_halfa = 0
#         p_lbeta = 0
#         p_hbeta = 0
#         p_lgama = 0
#         p_mgama = 0
#         for i in range(15):
#             sleep(0.7)
#             lalfa = neuropy.lowAlpha
#             dat_lalfa.append(lalfa)
#             halfa = neuropy.highAlpha
#             dat_halfa.append(halfa)
#             lbeta = neuropy.lowBeta
#             dat_lbeta.append(lbeta)
#             hbeta = neuropy.highBeta
#             dat_hbeta.append(hbeta)         
#             lgama = neuropy.lowGamma
#             dat_lgama.append(lgama)
#             mgama = neuropy.midGamma
#             dat_mgama.append(mgama)
#         for i in range(15):
#             p_lalfa += dat_lalfa[i]
#             p_halfa += dat_halfa[i]
#             p_lbeta += dat_lbeta[i]
#             p_hbeta += dat_hbeta[i]
#             p_lgama += dat_lgama[i]
#             p_mgama += dat_mgama[i]
        
#         tkMessageBox.showinfo("Lectura","   Lectura Realizada   ") 
#     else:    
#         tkMessageBox.showwarning("Error"," Sensor sin Medición ")
    
# def rangos():
#     gui3=Toplevel()
#     gui3.title("Lectura Realizada")
#     gui3.geometry("910x400+405+35")
#     boton5=Button(gui3,text='Ok',command=gui3.destroy)
#     boton5.grid(row=7, column=0,padx=5,pady=5)
#     label=Label(gui3)
#     label.grid(row=0, column=0,padx=20,pady=30)
#     Label(gui3,text="  Última Lectura  ",relief="groove",font=(18),fg="blue",height = 2).place(x=400,y=20)

#     label2 = Label(gui3,text="Low Alfa:",height = 3)
#     label2.grid(row=1, column=0,padx=10)
#     numero2=StringVar()
#     numero2.set(dat_lalfa)
#     caja2=Entry(gui3,bd=4,textvariable=numero2,width=100)
#     caja2.grid(row=1, column=1)
#     caja2.config(justify="center")
    
#     label2 = Label(gui3,text="High Alfa:",height = 3)
#     label2.grid(row=2, column=0,padx=10)
#     numero2=StringVar()
#     numero2.set(dat_halfa)
#     caja2=Entry(gui3,bd=4,textvariable=numero2,width=100)
#     caja2.grid(row=2, column=1)
#     caja2.config(justify="center")

#     label2 = Label(gui3,text="Low Beta:",height = 3)
#     label2.grid(row=3, column=0,padx=10)
#     numero2=StringVar()
#     numero2.set(dat_lbeta)
#     caja2=Entry(gui3,bd=4,textvariable=numero2,width=100)
#     caja2.grid(row=3, column=1)
#     caja2.config(justify="center")

#     label2 = Label(gui3,text="High Beta:",height = 3)
#     label2.grid(row=4, column=0,padx=10)
#     numero2=StringVar()
#     numero2.set(dat_hbeta)
#     caja2=Entry(gui3,bd=4,textvariable=numero2,width=100)
#     caja2.grid(row=4, column=1)
#     caja2.config(justify="center")

#     label2 = Label(gui3,text="Low Gama:",height = 3)
#     label2.grid(row=5, column=0,padx=10)
#     numero2=StringVar()
#     numero2.set(dat_lgama)
#     caja2=Entry(gui3,bd=4,textvariable=numero2,width=100)
#     caja2.grid(row=5, column=1)
#     caja2.config(justify="center")

#     label2 = Label(gui3,text="Mid Gama:",height = 3)
#     label2.grid(row=6, column=0,padx=10)
#     numero2=StringVar()
#     numero2.set(dat_mgama)
#     caja2=Entry(gui3,bd=4,textvariable=numero2,width=100)
#     caja2.grid(row=6, column=1)
#     caja2.config(justify="center")


# def dron():
#     #att,lga,mga,lbe,hbe
#     des=att-30
#     up=0
#     down=0
#     if neuropy.attention != 0:
#             if(neuropy.attention>=att): #Elevar dron
#                 if (up==0):
#                     GPIO.output(st1,1)
#                     sleep(0.5)
#                     GPIO.output(st1,0)
#                     up=1
#                     down=1
                
#             if(neuropy.attention<=des): #desender dron
#                 if (down==1):
#                     GPIO.output(st2,1)
#                     sleep(0.5)
#                     GPIO.output(st2,0)
#                     down=0
#                     up=0

#             if(neuropy.attention>=mga): #derecha dron
#                 GPIO.output(st3,1)
#                 sleep(0.5)
#                 GPIO.output(st3,0)
                
#             if(neuropy.attention>=lga): #izquierda dron
#                 GPIO.output(st4,1)
#                 sleep(0.5)
#                 GPIO.output(st4,0)

#             if(neuropy.attention>=lbe): #adelante dron
#                 GPIO.output(st5,1)
#                 sleep(0.5)
#                 GPIO.output(st5,0)

#             if(neuropy.attention>=hbe): #atras dron
#                 GPIO.output(st6,1)
#                 sleep(0.5)
#                 GPIO.output(st6,0)

#             sleep(0.5)
#     else:
#         tkMessageBox.showwarning("Error"," Sensor sin Medición ")
   
# #Creacion del GUI
# gui = Tk()
# gui.title("EEG del Dron")
# gui.geometry("400x650+0+35")

# #texto en la pantalla
# nombreLabel=Label(gui)
# nombreLabel.grid(row=1, column=0,padx=10,pady=100)
# label1=Label(gui)
# label1.grid(row=0, column=0)
# Label(gui,text="  Control de un dron a través de la mente  ",relief="groove",fg="blue",font=(18),height = 2).place(x=20,y=20)
# Label(gui,text="Primero establezca conexión",height = 2).place(x=20,y=95)
# Label(gui,text="con el sensor E.E.G. ",height = 2).place(x=20,y=120)
# Label(gui,text="Seleccione cualquier boton para activar las funciones",height = 2).place(x=20,y=180)
# Label(gui,text="Araya Nicolás",height = 2).place(x=300,y=600)
# Label(gui,text="Méndez Pedro",height = 2).place(x=300,y=570)

# #Botones principales
# conexion = Button(gui, text = "Conectar",bg="#388eeb", command = conexion,width=11,height=5)
# conexion.grid(row=1, column=1,padx=5,pady=25)

# lectura= Button(gui, text = "Realizar una Lectura",bg="#55eb38", command = lectura,width=15,height=3)
# lectura.grid(row=2, column=0,padx=30,pady=20)

# grafica = Button(gui, text = "Mostrar el Gráfico",bg="#55eb38", command = grafica,width=15,height=3)
# grafica.grid(row=2, column=1,padx=5,pady=5)

# defcoman = Button(gui, text = "Definir los Rangos",bg="#ebe538", command = defcoman,width=15,height=3)
# defcoman.grid(row=3, column=0,padx=5,pady=5)

# rangos= Button(gui, text = "Rangos de la medición", command = rangos,bg="#ebe538",width=15,height=3)
# rangos.grid(row=3, column=1,padx=5,pady=5)

# dron= Button(gui, text = "Controlar el dron", command = dron,bg="#eb5838",width=10,height=5)
# dron.grid(row=4, column=0,padx=5,pady=30)

# #Cargar el GUI
# gui.mainloop()


