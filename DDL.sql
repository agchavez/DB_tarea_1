DROP TABLE Brand;
-- Tabla de las marcas
CREATE TABLE Brand(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nameM VARCHAR(30) NOT NULL,
    locationM text NOT NULL,
    link_page text NOT NULL,
    email text NOT NULL, 
    tel_number INT NOT NULL
);

DROP TABLE Storage;
-- Tabla de los discos de almacenamientos
CREATE TABLE IF NOT EXISTS Storage(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_brand INT NOT NULL,
    model_name TEXT NOT NULL, 
    type_tech VARCHAR(3) NOT NULL DEFAULT 'HDD', 
    capacity SMALLINT NOT NULL,
    reading SMALLINT NOT NULL, 
    writing SMALLINT NOT NULL,
    FOREIGN KEY (id_brand) REFERENCES Brand(id) ON UPDATE CASCADE
);

DROP TABLE RAM;
-- Tabla de las memorias RAM 
CREATE TABLE IF NOT EXISTS RAM(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    id_brand INT NOT NULL, 
    model_name TEXT NOT NULL,
    frequency SMALLINT NOT NULL, 
    capacity SMALLINT NOT NULL, 
    type_tech VARCHAR(4) NOT NULL, 
    FOREIGN KEY (id_brand) REFERENCES Brand(id) ON UPDATE CASCADE
);

DROP TABLE Screen;
-- Tabla de las pantallas 
CREATE TABLE IF NOT EXISTS Screen(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_brand INT NOT NULL,
    model_name TEXT NOT NULL,
    resolution VARCHAR(6) NOT NULL,
    type_tech VARCHAR(10) NOT NULL, 
    dimension TINYINT NOT NULL,
    FOREIGN KEY (id_brand) REFERENCES Brand(id) ON UPDATE CASCADE
);

DROP TABLE Computer;
-- Tabla de las computadoras
CREATE TABLE IF NOT EXISTS Computer(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    id_brand INT NOT NULL, 
    id_ram INT NOT NULL, 
    id_storage INT NOT NULL, 
    id_screen INT NOT NULL, 
    model_name TEXT NOT NULL,
    price INT NOT NULL, 
    link_manual TEXT NOT NULL,
    quantity SMALLINT NOT NULL, 
    keyboard_lang VARCHAR(6) NOT NULL,
    launch_year YEAR NOT NULL,
    FOREIGN KEY (id_ram) REFERENCES RAM(id) ON UPDATE CASCADE,
    FOREIGN KEY (id_storage) REFERENCES Storage(id) ON UPDATE CASCADE,
    FOREIGN KEY (id_screen) REFERENCES Screen(id) ON UPDATE CASCADE,
    FOREIGN KEY (id_brand) REFERENCES Brand(id) ON UPDATE CASCADE
);


-- Transacciones SQLite
SELECT * FROM Brand;

