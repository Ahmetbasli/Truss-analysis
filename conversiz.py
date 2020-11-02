from PyQt5.QtWidgets import  *
from PyQt5.uic import *
from PyQt5 import QtGui, QtCore
import sys
from test8 import Ui_MainWindow
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot,pyqtSignal
from PyQt5.QtGui import QIntValidator
from PyQt5 import QtCore, QtGui, QtWidgets
import array as arr
import numpy as np
from math import *
from functools import partial
from scipy import linalg







class conversiz(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)


#metarial data
        self.ym = -1
        self.area = -1
        self.ui.y_m1.returnPressed.connect(self.holdE)


        self.ui.cross_sec.returnPressed.connect(self.holdE)







#int validator
        self.ui.y_m1.setValidator(QIntValidator(-90000000,900000000,self))


        self.ui.m_n1.returnPressed.connect(self.holdN)

#material data



#creating add element geometry box and label
        self.ui.b=QtWidgets.QPushButton(self.ui.t2)
        self.ui.b.show()
        self.ui.b.setGeometry(650,150,50,40)


        self.lab = QLabel(self.ui.t2)
        self.lab.setText('Press Button to Add Elements' )
        self.lab.show()
        self.lab.setGeometry(580, 100 ,300, 20)
        if self.area == -1 or self.ym == -1:
            self.ui.b.setDisabled(True)


        p = 0
        lx1 = []
        ly1 = []
        lx2 = []
        ly2 = []
        self.ui.b.clicked.connect(partial(self.add, p, lx1, ly1, lx2, ly2))
#solve button
        self.ui.s5 = QtWidgets.QPushButton(self.ui.t5)
        self.ui.s5.show()
        self.ui.s5.setGeometry(900, 150, 40, 40)
        self.ui.s5.clicked.connect(self.solve)
        self.ui.s5.setDisabled(True)

#creating add boundry conditions

        self.ui.b4 = QtWidgets.QPushButton(self.ui.t4)
        self.ui.b4.show()
        self.ui.b4.setGeometry(900, 150, 40, 40)
        self.ui.b4.setDisabled(True)
        self.lab = QLabel(self.ui.t4)
        self.lab.setText('Press Button to Add  \n boundry conditions ')
        self.lab.show()
        self.lab.setGeometry(840, 100, 300, 30)

        enn=[]
        nnn=[]
        faxx=[]
        fayy=[]
        ffxx=[]
        ffyy=[]
        self.ui.b4.clicked.connect(partial(self.add_boundry,p,enn,nnn,faxx,fayy,ffxx,ffyy))

    def add_boundry(self,p,enn,nnn,faxx,fayy,ffxx,ffyy):
#creating checkboxs
        p=p+1

#dynamic lineedits
        self.en='en{}'.format(p)
        self.en = QtWidgets.QLineEdit(self.ui.scrollAreaWidgetContents_2)
        enn.append(self.en)
        self.ui.gridLayout_2.addWidget(self.en, p-1, 0, 1, 1)
        self.en.setObjectName(str(self.en))
        self.en.setValidator(QIntValidator(-5000, 5000, self))
        self.en.returnPressed.connect(partial(self.adjust_matrices,enn,nnn,faxx,fayy,ffxx,ffyy))





        self.nn='nn{}'.format(p)
        self.nn = QtWidgets.QLineEdit(self.ui.scrollAreaWidgetContents_2)
        nnn.append(self.nn)
        self.ui.gridLayout_2.addWidget(self.nn, p-1, 2, 1, 1)
        self.nn.setObjectName(str(self.nn))
        self.nn.setValidator(QIntValidator(-5000,5000, self))
        self.ui.gridLayout_2.addWidget(self.nn, p-1, 1, 1, 1)


        self.nn.returnPressed.connect(partial(self.adjust_matrices,enn,nnn,faxx,fayy,ffxx,ffyy))




        self.fax='fax{}'.format(p)
        self.fax = QtWidgets.QLineEdit(self.ui.scrollAreaWidgetContents_2)
        faxx.append(self.fax)
        self.ui.gridLayout_2.addWidget(self.fax, p - 1, 7, 1, 1)
        self.fax.setObjectName(str(self.fax))
        self.fax.setValidator(QIntValidator(-5000000, 5000000, self))
        self.fax.returnPressed.connect(partial(self.adjust_matrices,enn,nnn,faxx,fayy,ffxx,ffyy))



        self.fay='fay{}'.format(p)
        self.fay = QtWidgets.QLineEdit(self.ui.scrollAreaWidgetContents_2)
        fayy.append(self.fay)
        self.ui.gridLayout_2.addWidget(self.fay, p - 1, 9, 1, 1)
        self.fay.setObjectName(str(self.fay))
        self.fay.setValidator(QIntValidator(-9000000, 90000000, self))
        self.fay.returnPressed.connect(partial(self.adjust_matrices,enn,nnn,faxx,fayy,ffxx,ffyy))

#dynamic checkboxs

        self.ffx='ffx{}'.format(p)
        self.ffx = QtWidgets.QCheckBox(self.ui.scrollAreaWidgetContents_2)
        self.ffx.setChecked(False)
        ffxx.append(self.ffx)
        self.ffx.setObjectName(str(self.ffx))
        self.ui.gridLayout_2.addWidget(self.ffx, p-1, 3, 1, 1)


        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.ui.gridLayout_2.addItem(spacerItem, 0, 10, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.ui.gridLayout_2.addItem(spacerItem1, 0, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(90, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.ui.gridLayout_2.addItem(spacerItem2, 0, 6, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.ui.gridLayout_2.addItem(spacerItem3, 0, 4, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.ui.gridLayout_2.addItem(spacerItem4, 0, 8, 1, 1)



        self.ffx.stateChanged.connect(partial(self.adjust_matrices,enn,nnn,faxx,fayy,ffxx,ffyy))

        self.ffy='ffy{}'.format(p)
        self.ffy = QtWidgets.QCheckBox(self.ui.scrollAreaWidgetContents_2)
        self.ffy.setChecked(False)
        ffyy.append(self.ffy)
        self.ffy.setObjectName(str(self.ffy))
        self.ui.gridLayout_2.addWidget(self.ffy, p-1, 5, 1, 1)
        self.ffy.stateChanged.connect(partial(self.adjust_matrices,enn,nnn,faxx,fayy,ffxx,ffyy))

#update button
        self.ui.b4.deleteLater()
        self.ui.b4 = QtWidgets.QPushButton(self.ui.t4)
        self.ui.b4.show()
        self.ui.b4.setGeometry(900, 150, 40, 40)
        self.ui.b4.clicked.connect(partial(self.add_boundry, p,enn,nnn,faxx,fayy,ffxx,ffyy))

    def adjust_matrices(self,enn,nnn,faxx,fayy,ffxx,ffyy):

        cl1 = []
        cl2 = []
        cl3 = []
        cl4 = []
        cl5 = []
        cl6 = []
        self.dofx = []
        self.dofy = []
        self.dof = []
        self.odof = []

        for i in range(0, len(enn)):
            self.dofx.append('e')

        for i in range(0, len(enn)):
            self.dofy.append('e')



        self.F = np.zeros(2 * self.xx)

        for i in range(0,len(enn)):

            cl1.append(enn[i].text())
            cl2.append(nnn[i].text())
            cl3.append(ffxx[i].isChecked())
            cl4.append(ffyy[i].isChecked())
            cl5.append(faxx[i].text())
            cl6.append(fayy[i].text())

            if len(enn[i].text()) != 0  and len(nnn[i].text()) != 0 :


                if ffxx[i].isChecked() == True or ffyy[i].isChecked()== True or len(faxx[i].text()) != 0 or len(fayy[i].text()) != 0 :

                    for j in range(1,len(self.x1)):

                        if (cl1[i] == self.x1[j] and cl2[i] == self.y1[j]):
# adjust stifness matrix and force vektor according to checkbox and force

                                if cl3[i] == True:

                                    self.dofx[i]=2*self.n1g[j]-2
                                elif   len(cl5[i]) != 0:
                                    self.F[2 * self.n1g[j] - 2] = cl5[i]
                                if cl4[i] == True:
                                    self.dofy[i] = 2 * self.n1g[j] - 1
                                elif len(cl6[i]) != 0 :
                                    self.F[2 * self.n1g[j] - 1] = cl6[i]
                                break
#adjust stifness matrix and force vektor according to checkbox and force
                        elif (cl1[i] == self.x2[j] and cl2[i] == self.y2[j]):
                            if cl3[i] == True:
                                self.dofx[i] = 2 * self.n2g[j] - 2
                            elif len(cl5[i]) != 0:
                                self.F[2 * self.n2g[j] - 2] = cl5[i]

                            if cl4[i] == True:
                                self.dofy[i] = 2 * self.n2g[j] - 1
                            elif len(cl6[i]) != 0 :
                                self.F[2*self.n2g[j]-1] = cl6[i]
                            break

        print('force vektor')                    
        print(self.F)

        for i in self.dofx :
            if i != 'e':
                self.dof.append(i)
        for i in self.dofy:
            if i != 'e':
                self.dof.append(i)
        print('DOF vektor')
        print(self.dof)
        if len(self.dof) != 0:
            self.ui.s5.setDisabled(False)


    def solve(self):
        self.gsmms = np.array([])
        self.gsmms = self.gsmm
        self.Fs = np.array([])
        self.Fs = self.F
        self.sigma = []
        self.rdisp = []
        self.elecorx1 = []
        self.elecorx2 = []
        self.elecory1 = []
        self.elecory2 = []




        if len(self.dof) != 0:
            for i in sorted(self.dof,reverse= True):

                self.gsmms = np.delete(self.gsmms, i, axis=0)
                self.gsmms = np.delete(self.gsmms, i, axis=1)
                self.Fs = np.delete(self.Fs, i, axis=0)
               

            if np.linalg.det(self.gsmms) != 0  :


                self.disp = linalg.solve(self.gsmms, self.Fs)
                print('Displacements of the nodes')
                print(self.disp)
#calculate tension
                if len(self.odof) == 0:
                    for i in range(len(self.gsmm)) :
                        self.odof.append(i)

                    for i in sorted(self.dof):
                        self.odof.remove(i)
                        

                for i in range(1,len(self.x1)):

                    self.vektor = np.array([-self.cc[i-1], -self.ss[i-1], self.cc[i-1], self.ss[i-1]])
                    
                    if len(self.x1[i]) != 0 and len(self.x2[i]) != 0 and len(self.y2[i]) != 0 and len(self.y2[i]) != 0:
                        dis = [0 ,0 ,0 ,0]
                        disi = [2*self.n1g[i]-2 ,2*self.n1g[i]-1 ,2*self.n2g[i]-2 ,2*self.n2g[i]-1 ]
                        disi = sorted(disi)
                        
                       
                        for k in range(len(self.odof)) :
                           
                            for j in range(len(disi)) :
                              
                                if disi[j] == self.odof[k] :
                                    dis[j] = self.disp[k]
                    
                    self.rdis=np.dot(self.vektor, dis)

                    self.sigma.append(self.rdis*(self.ym/self.ll[i-1]))
                    self.rdisp.append(self.rdis)
                    
                    print(self.sigma)
                    print(self.rdisp)
                    self.elecorx1.append(self.x1[i])
                    self.elecorx2.append(self.x2[i])
                    self.elecory1.append(self.y1[i])
                    self.elecory2.append(self.y2[i])
                    print(self.elecorx1)
                    print(self.elecory1)
                    print(self.elecorx2)
                    print(self.elecory2)

        # label stress values to the screen
        
        for i in range(len(self.elecory2)):
            
            #element 1 element 2 ...
            self.labcor = QtWidgets.QLabel(self.ui.scrollAreaWidgetContents_3)
            self.labcor.setText('element '+ str(i+1))
            self.ui.gridLayout_4.addWidget(self.labcor, i, 0, 1, 1)

            # x coordinate node 1
            self.labcor = QtWidgets.QLabel(self.ui.scrollAreaWidgetContents_3)
            self.labcor.setText(str(self.elecorx1[i]))
            self.ui.gridLayout_4.addWidget(self.labcor, i, 1, 1, 1)

            #y coordinate node 1
            self.labcor = QtWidgets.QLabel(self.ui.scrollAreaWidgetContents_3)
            self.labcor.setText(str(self.elecory1[i]))
            self.ui.gridLayout_4.addWidget(self.labcor, i, 2, 1, 1)

            #x coordinate node 2
            self.labcor = QtWidgets.QLabel(self.ui.scrollAreaWidgetContents_3)
            self.labcor.setText(str(self.elecorx2[i]))
            self.ui.gridLayout_4.addWidget(self.labcor, i, 3, 1, 1)

            #y coordinate node 2
            self.labcor = QtWidgets.QLabel(self.ui.scrollAreaWidgetContents_3)
            self.labcor.setText(str(self.elecory2[i]))
            self.ui.gridLayout_4.addWidget(self.labcor, i, 4, 1, 1)
            
            #stress values
            self.labcor = QtWidgets.QLabel(self.ui.scrollAreaWidgetContents_3)
            self.labcor.setText(str(self.sigma[i]))
            self.ui.gridLayout_4.addWidget(self.labcor, i, 10, 1, 1)
            
            




            





    def element(self,lx1,ly1,lx2,ly2):

        self.x1 = []
        self.x2 = []
        self.y1 = []
        self.y2 = []
        self.n1g = []
        self.n2g = []
        self.cc = []
        self.ss = []
        self.ll = []


        self.gsmm = np.array([])


        global x1
        x1=[1]
        for i in range(0, len(lx1)):
            x1.append(lx1[i].text())


        global y1
        y1 = [1]
        for i in range(0, len(lx1)):
            y1.append(ly1[i].text())


        global x2
        x2=[1]
        for i in range(0, len(lx1)):
            x2.append(lx2[i].text())


        global y2
        y2 = [1]
        for i in range(0, len(lx1)):
            y2.append(ly2[i].text())












        n1=[0,1]
        n2=[0,2]
        x=2


        for i in range(2,len(x1)):

            if len(x1[i]) != 0  and   len(x2[i]) != 0 and   len(y2[i]) != 0  and len(y2[i]) != 0:

                n1.append(0)
                n2.append(0)


                for j in range(1, i):


                    if x1[j] == x1[i] and y1[j] == y1[i]:
                        n1[i] = n1[j]

                    elif x2[j] == x1[i] and y2[j] == y1[i]:
                        n1[i] = n2[j]

                    if x1[j] == x2[i] and y1[j] == y2[i]:
                        n2[i] = n1[j]

                    elif x2[j] == x2[i] and y2[j] == y2[i]:
                        n2[i] = n2[j]

                if n1[i] == 0:
                    x = x + 1
                    n1[i]=x

                if n2[i] == 0:
                    x = x + 1
                    n2[i]=x
       # print(x1)
       # print(n2)
       # print(n1)
        gsm = np.zeros(4 * x * x).reshape(2 * x, 2 * x)
        for i in range(1,len(x1)):

            if len(x1[i]) != 0  and   len(x2[i]) != 0 and   len(y2[i]) != 0  and len(y2[i]) != 0:

                L = sqrt((float(y2[i]) - float(y1[i])) ** 2 + (float(x2[i]) - float(x1[i])) ** 2)

                esm = np.zeros(4 * x * x).reshape(2 * x, 2 * x)
                if n2[i]>n1[i]:


                    c = (float(x2[i]) - float(x1[i])) / L
                    s = (float(y2[i]) - float(y1[i])) / L
            #column 1
                    esm[2 * n1[i] - 2][2 * n1[i] - 2]=c*c
                    esm[2 * n1[i] - 2][2 * n1[i] - 1]=c*s
                    esm[2 * n1[i] - 2][2 * n2[i] - 2]=-c*c
                    esm[2 * n1[i] - 2][2 * n2[i] - 1]=-c*s
            #column 2
                    esm[2 * n1[i] - 1][2 * n1[i] - 2]=c*s
                    esm[2 * n1[i] - 1][2 * n1[i] - 1]=s*s
                    esm[2 * n1[i] - 1][2 * n2[i] - 2]=-c*s
                    esm[2 * n1[i] - 1][2 * n2[i] - 1]=-s*s
            #column 3
                    esm[2 * n2[i] - 2][2 * n1[i] - 2]=-c*c
                    esm[2 * n2[i] - 2][2 * n1[i] - 1]=-c*s
                    esm[2 * n2[i] - 2][2 * n2[i] - 2]=c*c
                    esm[2 * n2[i] - 2][2 * n2[i] - 1]=c*s

            #column 4
                    esm[2 * n2[i] - 1][2 * n1[i] - 2]=-c*s
                    esm[2 * n2[i] - 1][2 * n1[i] - 1]=-s*s
                    esm[2 * n2[i] - 1][2 * n2[i] - 2]=c*s
                    esm[2 * n2[i] - 1][2 * n2[i] - 1]=s*s
                else:
                    c = (float(x1[i]) - float(x2[i])) / L
                    s = (float(y1[i]) - float(y2[i])) / L
                    # column 1
                    esm[2 * n2[i] - 2][2 * n2[i] - 2]=c*c
                    esm[2 * n2[i] - 2][2 * n2[i] - 1]=c*s
                    esm[2 * n2[i] - 2][2 * n1[i] - 2]=-c*c
                    esm[2 * n2[i] - 2][2 * n1[i] - 1]=-c*s
                    # column 2
                    esm[2 * n2[i] - 1][2 * n2[i] - 2]=c*s
                    esm[2 * n2[i] - 1][2 * n2[i] - 1]=s*s
                    esm[2 * n2[i] - 1][2 * n1[i] - 2]=-c*s
                    esm[2 * n2[i] - 1][2 * n1[i] - 1]=-s*s
                    # column 3
                    esm[2 * n1[i] - 2][2 * n2[i] - 2]=-c*c
                    esm[2 * n1[i] - 2][2 * n2[i] - 1]=-c*s
                    esm[2 * n1[i] - 2][2 * n1[i] - 2]=c*c
                    esm[2 * n1[i] - 2][2 * n1[i] - 1]=c*s

                    # column 4
                    esm[2 * n1[i] - 1][2 * n2[i] - 2]=-c*s
                    esm[2 * n1[i] - 1][2 * n2[i] - 1]=-s*s
                    esm[2 * n1[i] - 1][2 * n1[i] - 2]=c*s
                    esm[2 * n1[i] - 1][2 * n1[i] - 1]=s*s

                self.cc.append(c)
                self.ss.append(s)
                self.ll.append(L)

                gsm=gsm+esm*(self.ym*self.area/L)

                self.gsmm = gsm
                
            self.x1 = list(x1)
            self.x2 = list(x2)
            self.y1 = list(y1)
            self.y2 = list(y2)
            self.n1g = list(n1)
            self.n2g = list(n2)
            self.xx = x
            if len(x1[i]) != 0 and len(x2[i]) != 0 and len(y2[i]) != 0 and len(y2[i]) != 0:
                self.ui.b4.setDisabled(False)

    def add(self,p,lx1,ly1,lx2,ly2):

        spacerItem = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.ui.gridLayout.addItem(spacerItem, 0, 3, 1, 1)
        p =p + 1
#x1
        #self.l='l{}'.format(p)
        self.l = QtWidgets.QLineEdit(self.ui.scrollAreaWidgetContents)
        lx1.append(self.l)
        self.l.setObjectName(str(self.l))
        self.l.setValidator(QIntValidator(-5000, 5000, self))
        self.ui.gridLayout.addWidget(self.l, p-1, 1, 1, 1)



#y1
        #self.l2 = 'l{}'.format(p)
        self.l2 = QtWidgets.QLineEdit(self.ui.scrollAreaWidgetContents)
        ly1.append(self.l2)
        self.l2.setObjectName(str(self.l2))
        self.l2.setValidator(QIntValidator(-5000, 5000, self))
        self.ui.gridLayout.addWidget(self.l2, p - 1, 2, 1, 1)
#x2
        #self.l3 = 'l{}'.format(p)
        self.l3 = QtWidgets.QLineEdit(self.ui.scrollAreaWidgetContents)
        lx2.append(self.l3)
        self.l3.setObjectName(str(self.l3))
        self.l3.setValidator(QIntValidator(-5000, 5000, self))
        self.ui.gridLayout.addWidget(self.l3, p - 1, 4, 1, 1)

#y2
        #self.l4 = 'l{}'.format(p)
        self.l4 = QtWidgets.QLineEdit(self.ui.scrollAreaWidgetContents)
        ly2.append(self.l4)
        self.ui.gridLayout.addWidget(self.l4, p - 1, 5, 1, 1)

        self.l4.setObjectName(str(self.l4))

        self.l4.setValidator(QIntValidator(-5000, 5000, self))

#update button
        self.ui.b.deleteLater()
        self.ui.b = QtWidgets.QPushButton(self.ui.t2)
        self.ui.b.show()
        self.ui.b.setGeometry(650, 150, 50, 40)
        self.ui.b.clicked.connect(partial(self.add, p,lx1,ly1,lx2,ly2))
# create label
        #self.la='la{}'.format(p)
        self.la= QtWidgets.QLabel(self.ui.scrollAreaWidgetContents)
        self.la.setText('Element '+str(p) )
        self.ui.gridLayout.addWidget(self.la, p-1, 0, 1, 1)





#pressing enter on linedit
        self.l.returnPressed.connect(partial(self.element,lx1,ly1,lx2,ly2))
        self.l2.returnPressed.connect(partial(self.element,lx1,ly1,lx2,ly2))
        self.l3.returnPressed.connect(partial(self.element,lx1,ly1,lx2,ly2))
        self.l4.returnPressed.connect(partial(self.element,lx1,ly1,lx2,ly2))

    # material data
    def holdE(self):

        received1=self.ui.y_m1.text()
        if len(received1):
            self.ym = float(received1)


        if len(self.ui.cross_sec.text()) != 0:
            self.area = float(self.ui.cross_sec.text())
        if float(self.area) != -1 and self.ym != -1:
            self.ui.b.setDisabled(False)


    def holdN(self):
        received_n1=self.ui.m_n1.text()
        n1=str(received_n1)

    # material data


uygulama=QApplication([])
pencere=conversiz()
pencere.show()
uygulama.exec_()






