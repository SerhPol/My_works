# -*- coding: utf-8 -*-
"""
Created on Mon May 10 00:31:21 2021

@author: polya
"""

import sys

from PyQt5 import QtWidgets#, QtGui#, QTableWidget#, QtCore
from interface import Ui_MainWindow

import sqlite3
bd = sqlite3.connect('orders.db')
cur = bd.cursor()

#обработка кнопки
def check ():
    
    #сбор всех выборов
    Sd = [0, 0]
    if ui.chBox_diag15.checkState():
        Sd[0] = 1
    
    if ui.chBox_diag14.checkState():
        Sd[1] = 1
    
    Sm = [0,0,0]
    if ui.chBox_matr_ips.checkState():
        Sm[0] = 1
    
    if ui.chBox_matr_lcd.checkState():
        Sm[1] = 1
    
    if ui.chBox_matr_tn.checkState():
        Sm[2] = 1
    
    Sp = [0,0,0]
    if ui.chBox_core2.checkState():
        Sp[0] = 1
        
    if ui.chBox_core4.checkState():
        Sp[1] = 1
        
    if ui.chBox_core6.checkState():
        Sp[2] = 1
        
    Sf = [0,0,0]
    if ui.chBox_freq1.checkState():
        Sf[0] = 1
        
    if ui.chBox_freq2.checkState():
        Sf[1] = 1
        
    if ui.chBox_freq25.checkState():
        Sf[2] = 1
    
    Sgb = [0,0,0]    
    if ui.chBox_gb1024.checkState():
        Sgb[0] = 1
        
    if ui.chBox_gb512.checkState():
        Sgb[1] = 1
        
    if ui.chBox_gb256.checkState():
        Sgb[2] = 1
    
    Smem = [0,0]
    if ui.chBox_hdd.checkState():
        Smem[0] = 1
        
    if ui.chBox_ssd.checkState():
        Smem[1] = 1
        
    Sram = [0,0,0]
    if ui.chBox_ram4.checkState():
        Sram[0] = 1
        
    if ui.chBox_ram8.checkState():
        Sram[1] = 1
        
    if ui.chBox_ram16.checkState():
        Sram[2] = 1
        
    Sg = [0,0,0]
    if ui.chBox_graphic2.checkState():
        Sg[0] = 1
        
    if ui.chBox_graphic3.checkState():
        Sg[1] = 1
        
    if ui.chBox_graphic4.checkState():
        Sg[2] = 1
    
    Sc = [0,0,0]
    if ui.chBox_col_black.checkState():
        Sc[0] = 1
        
    if ui.chBox_col_white.checkState():
        Sc[1] = 1
        
    if ui.chBox_col_serebr.checkState():
        Sc[2] = 1
        
    #построение скрипта
    script = '''SELECT n.code_product, n.name, 
                    f.name,
                    n.price,
                    s.diagonal, s.matrix, 
                    p.name, p.count_core, p.frequence,
                    m.count_gb, m.type,
                    r.count_gb,
                    g.name, g.count_gb,
                    c.name_color
                    
                    FROM nouts n
                    
                    join 
                    (select * from fabricator) f
                    on n.id_fabricator = f.id
                    
                    
                    '''
    
    #фильтры на экран
    script = script + ''' join 
                    (select id, diagonal, matrix from screen
                     '''
                     
    if (Sm[0] or Sm[1] or Sm[2] or Sd[0] or Sd[1]):
        script = script + ''' where ( '''
        f = 0  #флаг первого (для добавки or)
        if (Sm[0]):
            script = script + ''' matrix = "IPS" '''
            f = 1
        
        if (Sm[1]):
            if (f > 0):
                script = script + ''' or '''
            script = script + ''' matrix = "LCD" '''
            f = 1
            
        if (Sm[2]):
            if (f > 0):
                script = script + ''' or '''
            script = script + ''' matrix = "TN" '''
            f = 1
        
        if (f > 0):
            script = script + ''' ) '''
        
        f2 = 0  #флаг первого (для добавки and)
        if (Sd[0]):
            if (f > 0):
                script = script + ''' and ( '''
            script = script + ''' diagonal = "15,6" '''
            f = 1
            f2 = 1
            
        if (Sd[1]):
            if (f > 0):
                if (f2 == 0):
                    script = script + ''' and ( '''
                    f2 = 1
                else:
                    script = script + ''' or '''
            script = script + ''' diagonal = "14" '''
            f = 1
            f2 = 1
            
        if (f2 > 0):
            script = script + ''' ) '''
            
    script = script +  ''') s
                    on n.id_screen = s.id
                    '''
       
        
    #фильтры на процессор
    script = script + '''join 
                    (select * from processors
                     '''
                     
    if (Sp[0] or Sp[1] or Sp[2] or Sf[0] or Sf[1] or Sf[2]):
        script = script + ''' where ( '''
        f = 0  #флаг первого (для добавки or)
        if (Sp[0]):
            script = script + ''' count_core = 2 '''
            f = 1
        
        if (Sp[1]):
            if (f > 0):
                script = script + ''' or '''
            script = script + ''' count_core = 4 '''
            f = 1
            
        if (Sp[2]):
            if (f > 0):
                script = script + ''' or '''
            script = script + ''' count_core = 6 '''
            f = 1
        
        if (f > 0):
            script = script + ''' ) '''
        
        f2 = 0  #флаг первого (для добавки and)
        if (Sf[0]):
            if (f > 0):
                script = script + ''' and ( '''
            script = script + ''' (frequence >= 1 and frequence < 2) '''
            f = 1
            f2 = 1
            
        if (Sf[1]):
            if (f > 0):
                if (f2 == 0):
                    script = script + ''' and ( '''
                    f2 = 1
                else:
                    script = script + ''' or '''
            script = script + ''' (frequence >= 2 and frequence < 2.5) '''
            f = 1
            f2 = 1
                
        if (Sf[2]):
            if (f > 0):
                if (f2 == 0):
                    script = script + ''' and ( '''
                    f2 = 1
                else:
                    script = script + ''' or '''
            script = script + ''' (frequence >= 2.5) '''
            f = 1
            f2 = 1
        
        if (f2 > 0):
            script = script + ''' ) '''
            
    script = script +  ''' ) p
                    on n.id_proc = p.id
                    '''
     
                    
    #фильтры на память
    script = script + '''join 
                    (select me.id, me.count_gb, t.type from 
                     (select * from memory
                     '''
    if (Sgb[0] or Sgb[1] or Sgb[2]):
        script = script + ''' where ( '''
        
        f = 0  #флаг первого (для добавки or)
        if (Sgb[0]):
            script = script + ''' count_gb = 1024 '''
            f = 1
        
        if (Sgb[1]):
            if (f > 0):
                script = script + ''' or '''
            script = script + ''' count_gb = 512 '''
            f = 1
            
        if (Sgb[2]):
            if (f > 0):
                script = script + ''' or '''
            script = script + ''' count_gb = 256 '''
            f = 1
        
        script = script + ''' ) '''
        
    script = script + ''' ) me 
                        join 
                       (select * from type_memory
                    '''
        
    #тип памяти 
    if (Smem[0] or Smem[1]):
        script = script + ''' where ( '''
        
        
        f = 0  #флаг первого (для добавки and)
        if (Smem[0]):
            script = script + ''' type = 'HDD' '''
            f = 1
            
        if (Smem[1]):
            if (f > 0):
                script = script + ''' or '''
            script = script + ''' type = 'SSD' '''
            f = 1
            f2 = 1
                
        script = script + ''' ) '''
            
    script = script +  ''' ) t
                       on me.id_type = t.id
                     ) m
                    on n.id_memory = m.id
                    '''
    
        
    #фильтры на оперативку
    script = script + '''join 
                    (select * from ram
                     '''
        
    if (Sram[0] or Sram[1] or Sram[2]):
        script = script + ''' where ( '''
        
        f = 0  #флаг первого (для добавки or)
        if (Sram[0]):
            script = script + ''' count_gb = 4 '''
            f = 1
        
        if (Sram[1]):
            if (f > 0):
                script = script + ''' or '''
            script = script + ''' count_gb = 8 '''
            f = 1
            
        if (Sram[2]):
            if (f > 0):
                script = script + ''' or '''
            script = script + ''' count_gb = 16 '''
            f = 1
        
        script = script + ''' ) '''
        
    script = script + ''' ) r
                    on n.id_ram = r.id
                    '''
    
    #фильтры на графику
    script = script + '''join 
                    (select * from graphic
                     '''
                     
    if (Sg[0] or Sg[1] or Sg[2]):
        script = script + ''' where ( '''
        
        f = 0  #флаг первого (для добавки or)
        if (Sg[0]):
            script = script + ''' count_gb = 2 '''
            f = 1
        
        if (Sg[1]):
            if (f > 0):
                script = script + ''' or '''
            script = script + ''' count_gb = 3 '''
            f = 1
            
        if (Sg[2]):
            if (f > 0):
                script = script + ''' or '''
            script = script + ''' count_gb = 4 '''
            f = 1
        
        script = script + ''' ) '''
        
    script = script + ''' ) g
                    on n.id_graphic = g.id
                    '''
       
        
    #фильтры на цвет
    script = script + '''join 
                    (select * from color
                     '''
                     
    if (Sc[0] or Sc[1] or Sc[2]):
        script = script + ''' where ( '''
        
        f = 0  #флаг первого (для добавки or)
        if (Sc[0]):
            script = script + ''' name_color = 'Черный' '''
            f = 1
        
        if (Sc[1]):
            if (f > 0):
                script = script + ''' or '''
            script = script + ''' name_color = 'Белый' '''
            f = 1
            
        if (Sc[2]):
            if (f > 0):
                script = script + ''' or '''
            script = script + ''' name_color = 'Серебристый' '''
            f = 1
        
        script = script + ''' ) '''
        
    script = script + ''' ) c
                    on n.id_color = c.id
                    '''
    
    #конец скрипта
    script = script + ''' ; '''
    
    print(script)
    
    cur.execute(script)
    all_results = cur.fetchall()
    ui.insertTable(all_results)



app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

header = ["Код товара", "Название", "Производитель", "цена", 
          "диагональ", "матрица",
          "назв процес", "кол-во ядер", "частота",  
          "память", "тип памяти", "оперативка",
          "видеокарта", "Гб, видеокарта", "цвет"]

ui.headerTable(header)

ui.pushButton.clicked.connect(check)

sys.exit(app.exec_())