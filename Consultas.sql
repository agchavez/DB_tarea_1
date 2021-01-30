
-- Mostrar computadoras que cuentan con 8Gb de ram
SELECT 
    Computer.model_name AS "Modelo", 
    Brand.nameM AS "Marca", 
    Computer.price AS "Precio", 
    RAM.capacity AS "RAM"
    FROM Computer 
    JOIN Brand 
        ON Computer.id_brand = Brand.id
    JOIN RAM
        ON Computer.id_ram = RAM.id 
    WHERE 
        RAM.capacity = 8
;

-- Mostrar solo las computadoras con almacenamiento SSD
SELECT
    Computer.model_name AS "Modelo",
    Brand.nameM AS "Marca",
    Storage.capacity AS "Capacidad (Gb)"
    FROM Computer
    JOIN Brand
        ON Computer.id_brand = Brand.id
    JOIN Storage
        ON Storage.id = Computer.id_storage
    WHERE 
        type_tech = "SSD"
;

-- Mostrar computadras con un precio igual a 15000
SELECT 
    Computer.model_name AS "Modelo",
    Computer.price AS "Precio (L.)"
    FROM Computer
    WHERE
        Computer.price = 15000
;

-- 
-- Mostrar todas las marchas 
SELECT * FROM Brand;

-- Mostrar las memorias ram

SELECT * FROM RAM;

-- Mostrar las pantallas 

SELECT * FROM Screen;

-- Mostrar los discos de almacenamiento

SELECT * FROM Storage;

-- Mostrar todas las computadoras en el almacen

SELECT * FROM Computer;



