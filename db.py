import sqlite3
import sys
class Data:

    def __init__(self):
        self.data = sqlite3.connect('mydatabase.db')
        self.cursor = self.data.cursor()

    #---------------- Ingresar datos --------------------

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
        return True

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
        print('---- Computadora ingresada con exito ---')
        return True
    
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
        return True
    
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
        return True

    def setRam(self, data):
        self.cursor.execute('''
                INSERT INTO 
                RAM(id_brand, model_name, frequency, capacity, type_tech) 
                VALUES
                (%d,'%s',%d,%d,'%s')
        ''' % (int(data['id_brand']),data['model_name'],int(data['frequency']),int(data['capacity']),data['type_tech']))
        self.data.commit()
        print('---- RAMM ingresada con exito ---')
    
    #---------------- Mostrar datos --------------------

    def getComputer(self):
        print('-----------COMPUTADORAS---------------')
        query = self.cursor.execute('SELECT * FROM Computer')
        self.showRow(query)
        return True
        
    def getBrand(self):
        print('-----------MARCAS---------------')
        query = self.cursor.execute('SELECT * FROM Brand')
        self.showRow(query)
        return True
    
    def getScreen(self):
        print('-----------PANTALLAS---------------')
        query = self.cursor.execute('SELECT * FROM Screen')
        self.showRow(query)
        return True
    
    def getStorage(self):
        print('-----------DISCOS DUROS---------------')
        query = self.cursor.execute('SELECT * FROM Storage')
        self.showRow(query)
        return True
    
    def getRam(self):
        print('-----------MEMORIAS RAM---------------')
        query = self.cursor.execute('SELECT * FROM RAM')
        self.showRow(query)
        return True

    def showRow(self, query):   
        for row in query:
            print(row)

    #---------------- Actualizar datos --------------------   

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
        return True

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
        return True 

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
        return True
     
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
        return True                    

    #---------------- Eliminar datos --------------------

    def deleteComputer(self, id): 
        print('---------------ELIMINAR COMPUTADORA------------------')
        self.cursor.execute("DELETE FROM Computer WHERE id = %d"%int(id))
        print('-----------Computadora eliminada con exito-----------')
        self.data.commit()
        return True

    def deleteRam(self, id): 
        print('---------------ELIMINAR RAM------------------')
        self.cursor.execute("DELETE FROM RAM WHERE id = %d"%int(id))
        print('-----------RAM eliminada con exito-----------')
        self.data.commit()
        return True

    def deleteScreen(self, id): 
        print('---------------ELIMINAR PANTALLA------------------')
        self.cursor.execute("DELETE FROM Screen WHERE id = %d"%int(id))
        print('-----------Pantalla eliminada con exito-----------')
        self.data.commit()
        return True

    def deleteBrand(self, id): 
        print('---------------ELIMINAR MARCA------------------')
        self.cursor.execute("DELETE FROM Brand WHERE id = %d"%int(id))
        print('-----------Marca eliminada con exito-----------')
        self.data.commit()
        return True            

