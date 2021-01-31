import sqlite3
import sys
from db import Data


class Menu:
    def __init__(self):
        self.db = Data()

    def Menu(self):
        print('\n\n\n\n============================')
        print('Menu:')
        print('1. Mostrar datos')
        print('2. Ingresar datos')
        print('3. Actualizar datos')
        print('4. Eliminar datos')
        print('5. Salir')
        print('Ingrese su opcion: ')
        seleccion = input()
        if  seleccion == '1':
            self.menuShow()
        elif seleccion == '2':
            self.insertsMenu()
        elif seleccion == '3':
            self.updateMenu()
        elif seleccion == '4':
            self.DeleteMenu()
        elif seleccion == '5':
            print('Gracias por preferirnos')
            quit()
        else:
            print('Opcion no valida')
            self.Menu

    def insertsMenu(self):
        print('\n\n\n\n============================')
        print('Menu de inserciones:')
        print('1. Insertar computadoras')
        print('2. Insertar RAM')
        print('3. Insertar pantallas')
        print('4. Insertar marcas')
        print('5. regresar al menu')
        print('Ingrese su opcion: ')
        seleccion = input()
        if  seleccion == '1':
            data = {"id_brand":"",
                    "id_ram":"",
                    "id_storage":"",
                    "id_screen":"",
                    "model_name":"",
                    "price":"",
                    "link_manual":"",
                    "quantity":"",
                    "keyboard_lang":"s",
                    "launch_year":""
                    }
            
            self.db.setComputer(self.enterokayData(data))
            self.Menu
        elif seleccion == '2':
            data = {
                    "id_brand":"",
                    "model_name":"",
                    "frequency":"",
                    "capacity":"",
                    "type_tech":""
                    }
            self.db.setRam(self.enterokayData(data))
            self.Menu
        elif seleccion == '3':
            data = {
                    "id_brand":"",
                    "model_name":"",
                    "resolution":"",
                    "type_tech":"",
                    "dimension":""
                    }
            self.db.setScreen(self.enterokayData(data))
            self.Menu
        elif seleccion == '4':
            data = {
                    "nameM":"",
                    "locationM":"",
                    "link_page":"",
                    "email":"",
                    "tel_number":""
                    }
            self.db.setStorage(self.enterokayData(data))
            self.Menu
        elif seleccion == '5':
            self.Menu()
        else:
            print('Opcion no valida')
            self.menuShow

    def enterokayData(self, data):
        for value in data:
            print("Ingrese el ", value)
            data[value] = input()
        return data

    def menuShow(self):
        print('\n\n\n\n============================')
        print('Menu de mostrar datos:')
        print('1. Mostrar todas las  Computadoras')
        print('2. Mostrar todas las RAM')
        print('3. Mostrar todas las pantallas')
        print('4. Mostrar todas las marcas')
        print('5. regresar al menu')
        print('Ingrese su opcion: ')
        seleccion = input()
        if  seleccion == '1':
           query = self.db.getComputer()
        elif seleccion == '2':
           query = self.db.getRam()
        elif seleccion == '3':
           query = self.db.getScreen()
        elif seleccion == '4':
           query = self.db.getStorage()
        elif seleccion == '5':
            self.Menu
        else:
            print('Opcion no valida')
            self.menuShow
        self.Menu()

    def updateMenu(self):
        print('\n\n\n\n============================')
        print('Menu de Actualizaciones de datos:')
        print('1. Actualizar computadoras')
        print('2. Actualizar RAM')
        print('3. Actualizar pantallas')
        print('4. Actualizar marcas')
        print('5. regresar al menu')
        print('Ingrese su opcion: ')
        seleccion = input()   
        print('Ingrese el id del campo a editar: ')
        if  seleccion == '1':
            data = {"id":"",
                    "id_brand":"",
                    "id_ram":"",
                    "id_storage":"",
                    "id_screen":"",
                    "model_name":"",
                    "price":"",
                    "link_manual":"",
                    "quantity":"",
                    "keyboard_lang":"",
                    "launch_year":""
                    }
            
            query =  self.db.updateComputer(self.enterokayData(data))
        elif seleccion == '2':
            data = {"id":"",
                    "id_brand":"",
                    "model_name":"",
                    "frequency":"",
                    "capacity":"",
                    "type_tech":""
                    }
            query =  self.db.updateRAM(self.enterokayData(data))
        elif seleccion == '3':
            data = {"id":"",
                    "id_brand":"",
                    "model_name":"",
                    "resolution":"",
                    "type_tech":"",
                    "dimension":""
                    }
            query =  self.db.updateScreen(self.enterokayData(data))
        elif seleccion == '4':
            data = {
                    "nameM":"",
                    "locationM":"",
                    "link_page":"",
                    "email":"",
                    "tel_number":""
                    }
            query =  self.db.updateBrand(self.enterokayData(data))
        elif seleccion == '5':
            self.Menu()
        else:
            print('Opcion no valida')
            self.menuShow
        self.Menu

    def DeleteMenu(self):
        print('\n\n\n\n============================')
        print('Que desea eliminar?:')
        print('1. Eliminar computadoras')
        print('2. Eliminar RAM')
        print('3. Eliminar pantallas')
        print('4. Eliminar marcas')
        print('5. regresar al menu')
        print('Ingrese su opcion: ')
        seleccion = input()  
        print("Ingrese el id a eliminar: ")
        id = input() 
        if  seleccion == '1':
            query = self.db.deleteComputer(id)
        elif seleccion == '2':                    
                    
            query = self.db.deleteRam(id)
        elif seleccion == '3':                    
                    
            query = self.db.deleteScreen(id)
        elif seleccion == '4':                    
                    
            query = self.db.deleteBrand(id)
        elif seleccion == '5':
            self.Menu()
        else:
            print('Opcion no valida')
            self.menuShow   
        self.Menu              

