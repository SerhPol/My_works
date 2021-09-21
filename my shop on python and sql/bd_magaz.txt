# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 11:01:22 2021

@author: polya
"""

print('hi')

import sqlite3
bd = sqlite3.connect('orders.db')

cur = bd.cursor()


cur.execute("""CREATE TABLE IF NOT EXISTS nouts(
   id TEXT PRIMARY KEY,
   code_product TEXT,
   name TEXT,
   id_fabricator TEXT,
   price INT,
   id_screen TEXT,
   id_proc TEXT,
   id_ram TEXT,
   id_memory TEXT,
   id_graphic TEXT,
   id_color TEXT );
""")
            
cur.execute("""CREATE TABLE IF NOT EXISTS processors(
   id TEXT PRIMARY KEY,
   name TEXT,
   id_fabricator TEXT,
   count_core INT,
   frequence INT );
""")

cur.execute("""CREATE TABLE IF NOT EXISTS graphic(
   id TEXT PRIMARY KEY,
   name TEXT,
   id_fabricator TEXT,
   count_gb INT );
""")

cur.execute("""CREATE TABLE IF NOT EXISTS ram(
   id TEXT PRIMARY KEY,
   id_fabricator TEXT,
   count_gb INT );
""")

cur.execute("""CREATE TABLE IF NOT EXISTS screen(
   id TEXT PRIMARY KEY,
   diagonal INT,
   matrix INT );
""")

cur.execute("""CREATE TABLE IF NOT EXISTS fabricator(
   id TEXT PRIMARY KEY,
   name TEXT );
""")

cur.execute("""CREATE TABLE IF NOT EXISTS color(
   id TEXT PRIMARY KEY,
   name_color TEXT );
""")

cur.execute("""CREATE TABLE IF NOT EXISTS memory(
   id TEXT PRIMARY KEY,
   count_gb INT,
   id_type TEXT,
   id_fabricator TEXT );
""")

cur.execute("""CREATE TABLE IF NOT EXISTS type_memory(
   id TEXT PRIMARY KEY,
   type TEXT );
""")

bd.commit()




nouts = [('1',	'NH.Q5AEU.05J',	  'Acer Nitro 5 AN515-54 Shale Black',	    '1',	'20000',	'1',	'1',	'1',	'1',	'1',	'1'),
         ('2',	'NX.HYSEU.00C',	  'Ноутбук Acer Swift 1 SF114-33',	        '1',	'15000',	'2',	'2',	'1',	'2',	'2',	'3'),
         ('3',	'81YQ008PRA',	  'Ноутбук Lenovo IdeaPad 5 15ARE',	        '4',	'17000',	'1',	'3',	'1',	'2',	'3',	'2'),
         ('4',	'NX.HF9EU.07Q',	  'Ноутбук Acer Aspire 3 A315-42',	        '1',	'19000',	'3',	'4',	'3',	'3',	'4',	'1'),
         ('5',	'82C600DERA',	  'Ноутбук Lenovo V14-ADA',	                '4',	'9800',	    '4',	'5',	'2',	'1',	'2',	'1'),
         ('6',	'82ES000KRA',	  'Ноутбук Lenovo Ducati 5',	            '4',	'30000',	'2',	'6',	'1',	'4',	'2',	'3'),
         ('7',	'NH.Q7JEU.01D',	  'Ноутбук ігровий Acer Nitro 5 AN515-55',	'1',	'26000',	'1',	'7',	'2',	'3',	'1',	'1'),
         ('8',	'82C6005DRA',	   'Ноутбук Lenovo V14-ADA',	            '4',	'12500',	'4',	'1',	'1',	'2',	'3',	'3'),
         ('9',	'FX506LI-HN096',   'Ноутбук ігровий Asus TUF Gaming',	    '3',	'31000',	'1',	'7',	'1',	'3',	'1',	'2'),
         ('10',	'82C7000YRA',	   'Ноутбук Lenovo V15-ADA',	            '4',	'16000',	'5',	'1',	'1',	'3',	'3',	'2'),
         ('11',	'NX.HUSEU.00C',	   'Ноутбук Acer Aspire 5 A514-53',	        '1',	'16500',	'3',	'4',	'2',	'2',	'1',	'3'),
         ('12',	'NX.HZFEU.002',	   'Ноутбук Acer Aspire 5 A515-55G',	    '1',	'17000',	'1',	'5',	'1',	'2',	'2',	'1'),
         ('13',	'N306ZVN3591ERC_UBU',	'Ноутбук Dell Vostro 3591',	        '5',	'16500',	'3',	'1',	'1',	'2',	'4',	'2'),
         ('14',	'E410MA-EB268',	   'Ноутбук Asus Laptop E410MA Peacock',    '3',	'11500',	'2',	'1',	'2',	'2',	'2',	'3'),
         ('15',	'X515MA-EJ013',	   'Ноутбук Asus X515MA-EJ013',	            '3',	'14000',	'5',	'2',	'1',	'1',	'2',	'1'),
         ('16',	'82C6005ERA',	   'Ноутбук Lenovo V14-ADA',	            '4',	'14000',	'4',	'4',	'1',	'3',	'3',	'2'),
         ('17',	'X515MA-EJ135',	   'Ноутбук Asus X515MA-EJ135',	            '3',	'15000',	'5',	'2',	'2',	'1',	'4',	'1'),
         ('18',	'X509UB-BQ084',	   'Ноутбук Asus X509UB-BQ084',	            '3',	'16000',	'1',	'5',	'1',	'3',	'2',	'3'),
         ('19',	'I3538S2NIW-80B',	   'Ноутбук Dell Inspiron 3501',	    '5',	'17500',	'5',	'1',	'1',	'2',	'4',	'2'),
         ('20',	'N6504VN3501ERC_UBU',  'Ноутбук Dell Vostro 3501',	        '5',	'20000',	'1',	'1',	'3',	'1',	'2',	'3')

        ]

processors = [('1',	'Ryzen 5 3550H',	'5',	'2',	'2.1'),
              ('2',	'Pentium N5030',	'7',	'4',	'1.1'),
              ('3',	'Ryzen 5 4500U',	'5',	'6',	'2.1'),
              ('4',	'Ryzen 7 3700U',	'5',	'4',	'2.2'),
              ('5',	'Athlon 3150U',     '4',    '2',    '2.2'),
              ('6',	'Core i5-1035G1',	'7',	'4',	'1'),
              ('7',	'Core i5-10300H',	'7',	'4',	'2.5')
          ]

graphic = [('1', 'GeForce GTX 1650','2', '4'),
           ('2', 'GeForce MX350',	'2', '2'),
           ('3', 'Radeon Vega 8',	'6', '3'),
           ('4', 'UHD Graphics',	'7', '4')
         ]

ram = [('1', '6', '8'),
       ('2', '2', '4'),
       ('3', '6', '16')
      ]

screen = [('1',	'15,6',	'IPS'),
          ('2',	'14',	'IPS'),
          ('3',	'15,6',	'LCD'),
          ('4',	'14',	'TN'),
          ('5',	'15,6',	'TN')
        ]

fabricator = [('1',	'Acer'), 
              ('2',	'Nvidia'), 
              ('3',	'Asus'), 
              ('4',	'Lenovo'), 
              ('5',	'Dell'), 
              ('6',	'Sumsung'), 
              ('7',	'Intel')
          ]

color = [('1',	'Черный'),
         ('2',	'Белый'),
         ('3',	'Серебристый')
        ]

memory = [('1',	'1024',	'1',	'3'),
          ('2',	'256',	'2',	'5'),
          ('3',	'512',	'2',	'6'),
          ('4',	'1024',	'2',	'6')
         ]
 
type_memory = [('1',	'HDD'), 
               ('2',	'SSD')
              ]


"""
cur.executemany("INSERT INTO nouts VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", nouts)

cur.executemany("INSERT INTO processors VALUES(?, ?, ?, ?, ?);", processors)

cur.executemany("INSERT INTO graphic VALUES(?, ?, ?, ?);", graphic)
cur.executemany("INSERT INTO ram VALUES(?, ?, ?);", ram)
cur.executemany("INSERT INTO screen VALUES(?, ?, ?);", screen)
cur.executemany("INSERT INTO fabricator VALUES(?, ?);", fabricator)

cur.executemany("INSERT INTO color VALUES(?, ?);", color)
cur.executemany("INSERT INTO memory VALUES(?, ?, ?, ?);", memory)
cur.executemany("INSERT INTO type_memory VALUES(?, ?);", type_memory)
#"""
bd.commit()



cur.execute("SELECT * FROM nouts;")
all_results = cur.fetchall()
print("\n", all_results)

cur.execute("SELECT * FROM processors;")
all_results = cur.fetchall()
print("\n", all_results)

cur.execute("SELECT * FROM graphic;")
all_results = cur.fetchall()
print("\n", all_results)

cur.execute("SELECT * FROM ram;")
all_results = cur.fetchall()
print("\n", all_results)

cur.execute("SELECT * FROM screen;")
all_results = cur.fetchall()
print("\n", all_results)

cur.execute("SELECT * FROM fabricator;")
all_results = cur.fetchall()
print("\n", all_results)

cur.execute("SELECT * FROM color;")
all_results = cur.fetchall()
print("\n", all_results)

cur.execute("SELECT * FROM memory;")
all_results = cur.fetchall()
print("\n", all_results)

cur.execute("SELECT * FROM type_memory;")
all_results = cur.fetchall()
print("\n", all_results)
