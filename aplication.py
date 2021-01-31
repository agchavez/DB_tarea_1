import sqlite3
import sys

class Data:

    def __init__(self):
        self.data = sqlite3.connect('mydatabase.db')
        self.cursor = self.data.cursor()

    def setBrand(self, data):
        self.cursor.execute('''
                INSERT INTO 
                    Brand(nameM,locationM,link_page,email,tel_number) VALUES
                ('%s','%s','%s','%s',%d)
        ''' % (data['nameM'],
                data['locationM'],
                data['link_page'],
                data['email'],
                int(data['tel_number']),
                ))
        self.data.commit()
        print('---- Marca ingresada con exito ---')
        Menu().Menu()

    def setComputer(self, data):
        self.cursor.execute('''
                INSERT INTO 
                Computer
                (id_brand, id_ram, id_storage, id_screen, model_name, price, link_manual, quantity, keyboard_lang, launch_year)
                VALUES
                (%d,%d,%d,%d,'%s',%d,'%s',%d,'%s',%d)
        ''' % (int(data['id_brand']),
                int(data['id_ram']),
                int(data['id_storage']),
                int(data['id_screen']),
                data['model_name'],
                int(data['price']),
                data['link_manual'],
                int(data['quantity']),
                data['keyboard_lang'],
                int(data['launch_year']),
                ))
        self.data.commit()
        print('---- Computadira ingresada con exito ---')
        Menu().Menu()
        
    
    def setScreen(self, data):
        self.cursor.execute('''
                INSERT INTO 
                    Screen(id_brand, model_name, resolution, type_tech, dimension) VALUES
                (%d,'%s','%s','%s',%d)
        ''' % (int(data['id_brand']),
                data['model_name'],
                data['resolution'],
                data['resolution'],
                int(data['dimension']),
                ))
        self.data.commit()
        print('---- Pantalla ingresada con exito ---')
        Menu().Menu()
    
    def setStorage(self, data):
        self.cursor.execute('''
                INSERT INTO Storage(id_brand, model_name, type_tech, capacity, reading, writing) 
                VALUES
                (%d,'%s',%s,'%d',%d,%d)
        ''' % (int(data['id_brand']),
                data['model_name'],
                data['type_tech'],
                int(data['capacity']),
                int(data['reading']),
                int(data['writing'])
                ))
        self.data.commit()
        print('---- Disco ingresada con exito ---')
        Menu().Menu()

    def setRam(self, data):
        self.cursor.execute('''
                INSERT INTO 
                RAM(id_brand, model_name, frequency, capacity, type_tech) 
                VALUES
                (%d,'%s',%d,%d,'%s')
        ''' % (int(data['id_brand']),data['model_name'],int(data['frequency']),int(data['capacity']),data['type_tech']))
        self.data.commit()
        print('---- RAMM ingresada con exito ---')
        Menu().Menu()
    
    def getComputer(self):
        print('-----------COMPUTADORAS---------------')
        print('Ingreso')
        query = self.cursor.execute('SELECT * FROM Computer')
        self.showRow(query)

    def getBrand(self):
        print('-----------MARCAS---------------')
        query = self.cursor.execute('SELECT * FROM Brand')
        self.showRow(query)
    
    def getScreen(self):
        print('-----------PANTALLAS---------------')
        query = self.cursor.execute('SELECT * FROM Screen')
        self.showRow(query)
    
    def getStorage(self):
        print('-----------DISCOS DUROS---------------')
        query = self.cursor.execute('SELECT * FROM Storage')
        self.showRow(query)
    
    def getRam(self):
        print('-----------MEMORIAS RAM---------------')
        query = self.cursor.execute('SELECT * FROM RAM')
        self.showRow(query)

    def showRow(self, query):   
        for row in query:
            print(row)
        Menu().Menu()

    def updateComputer(self, data):
        print('-----------ACTUALIZAR COMPUTADORA---------------')
        self.cursor.execute('''
                UPDATE 
                Computer SET
                id_brand = %d , id_ram = %d, id_storage = %d, id_screen = %d, model_name = '%s', price = %d, link_manual = '%s', quantity = %d, keyboard_lang = '%s', launch_year = %d
                WHERE Computer.id = %d
        ''' % (int(data['id_brand']),
                int(data['id_ram']),
                int(data['id_storage']),
                int(data['id_screen']),
                data['model_name'],
                int(data['price']),
                data['link_manual'],
                int(data['quantity']),
                data['keyboard_lang'],
                int(data['launch_year']),
                int(data['id'])
                ))
        self.data.commit()
        print('------Computadora Actualizada con exito---------')
        Menu().Menu()  

    def updateRAM(self, data):
        print('---------------ACTUALIZAR RAM------------------')
        self.cursor.execute(
        '''UPDATE  
            RAM SET
                id_brand = %d, model_name = '%s', frequency = %d, capacity = %d, type_tech = '%s' 
            WHERE
                RAM.id = %d ''' 
                    % (int(data['id_brand']),data['model_name'],int(data['frequency']),int(data['capacity']),data['type_tech'],int(data['id'])))
        self.data.commit()
        print('-----------RAM Actualizada con exito-----------')
        Menu().Menu()   

    def updateScreen(self, data):
        print('---------------ACTUALIZAR PANTALLA------------------')
        self.cursor.execute('''
                UPDATE 
                    Screen SET 
                        id_brand = %d, model_name = '%s', resolution = '%s', type_tech = '%s', dimension = %d 
                    WHERE 
                        id = %d
        ''' % (int(data['id_brand']),
                data['model_name'],
                data['resolution'],
                data['resolution'],
                int(data['dimension']),
                int(data['id'])
                ))
        self.data.commit()
        print('-----------Pantalla Actualizada con exito-----------')
        Menu().Menu() 
        
    def updateBrand(self, data):
        print('---------------ACTUALIZAR MARCA------------------')
        self.cursor.execute('''
                UPDATE  
                    Brand SET
                    nameM='%s',locationM='%s',link_page='%s',email='%s',tel_number = %d
                WHERE
                    id = %d
        ''' % (data['nameM'],
                data['locationM'],
                data['link_page'],
                data['email'],
                int(data['tel_number']),
                int(data['id'])
                ))
        self.data.commit()
        print('-----------Marca Actualizada con exito-----------')
        Menu().Menu()                     

    def deleteComputer(self, id): 
        print('---------------ELIMINAR COMPUTADORA------------------')
        self.cursor.execute("DELETE FROM Computer WHERE id = %d"%int(id))
        print('-----------Computadora eliminada con exito-----------')
        self.data.commit()
        Menu().Menu()

    def deleteRam(self, id): 
        print('---------------ELIMINAR RAM------------------')
        self.cursor.execute("DELETE FROM RAM WHERE id = %d"%int(id))
        print('-----------RAM eliminada con exito-----------')
        self.data.commit()
        Menu().Menu()

    def deleteScreen(self, id): 
        print('---------------ELIMINAR PANTALLA------------------')
        self.cursor.execute("DELETE FROM Screen WHERE id = %d"%int(id))
        print('-----------Pantalla eliminada con exito-----------')
        self.data.commit()
        Menu().Menu()

    def deleteBrand(self, id): 
        print('---------------ELIMINAR MARCA------------------')
        self.cursor.execute("DELETE FROM Brand WHERE id = %d"%int(id))
        print('-----------Marca eliminada con exito-----------')
        self.data.commit()
        Menu().Menu()            



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
        elif seleccion == '2':
            data = {
                    "id_brand":"",
                    "model_name":"",
                    "frequency":"",
                    "capacity":"",
                    "type_tech":""
                    }
            self.db.setRam(self.enterokayData(data))
        elif seleccion == '3':
            data = {
                    "id_brand":"",
                    "model_name":"",
                    "resolution":"",
                    "type_tech":"",
                    "dimension":""
                    }
            self.db.setScreen(self.enterokayData(data))
        elif seleccion == '4':
            data = {
                    "nameM":"",
                    "locationM":"",
                    "link_page":"",
                    "email":"",
                    "tel_number":""
                    }
            self.db.setStorage(self.enterokayData(data))
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
           self.db.getComputer()
        elif seleccion == '2':
           self.db.getRam()
        elif seleccion == '3':
           self.db.getScreen()
        elif seleccion == '4':
           self.db.getStorage()
        elif seleccion == '5':
            self.Menu
        else:
            print('Opcion no valida')
            self.menuShow

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
            
            self.db.updateComputer(self.enterokayData(data))
        elif seleccion == '2':
            data = {"id":"",
                    "id_brand":"",
                    "model_name":"",
                    "frequency":"",
                    "capacity":"",
                    "type_tech":""
                    }
            self.db.updateRAM(self.enterokayData(data))
        elif seleccion == '3':
            data = {"id":"",
                    "id_brand":"",
                    "model_name":"",
                    "resolution":"",
                    "type_tech":"",
                    "dimension":""
                    }
            self.db.updateScreen(self.enterokayData(data))
        elif seleccion == '4':
            data = {
                    "nameM":"",
                    "locationM":"",
                    "link_page":"",
                    "email":"",
                    "tel_number":""
                    }
            self.db.updateBrand(self.enterokayData(data))
        elif seleccion == '5':
            self.Menu()
        else:
            print('Opcion no valida')
            self.menuShow

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
            self.db.deleteComputer(id)
        elif seleccion == '2':                    
                    
            self.db.deleteRam(id)
        elif seleccion == '3':                    
                    
            self.db.deleteScreen(id)
        elif seleccion == '4':                    
                    
            self.db.deleteBrand(id)
        elif seleccion == '5':
            self.Menu()
        else:
            print('Opcion no valida')
            self.menuShow                 
        

    


Menu().Menu()