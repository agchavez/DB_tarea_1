INSERT INTO Brand(nameM,locationM,link_page,email,tel_number) VALUES
("DELL","14.266565,-12.45666","https://example.com","example@example.com", 478895623),
("HP","14.266565,-12.45666","https://example.com","example@example.com", 478895623),
("KINGSTON","14.266565,-12.45666","https://example.com","example@example.com", 478895623),
("ADATA","14.266565,-12.45666","https://example.com","example@example.com", 478895623),
("ASUS","14.266565,-12.45666","https://example.com","example@example.com", 478895623),
("TOSHIBA","14.266565,-12.45666","https://example.com","example@example.com", 478895623),
("LG","14.266565,-12.45666","https://example.com","example@example.com", 478895623),
("MSI","14.266565,-12.45666","https://example.com","example@example.com", 478895623),
("ACER","14.266565,-12.45666","https://example.com","example@example.com", 478895623),
("SanDisk","14.266565,-12.45666","https://example.com","example@example.com", 478895623)
;

INSERT INTO Storage(id_brand, model_name, type_tech, capacity, reading, writing) VALUES
(3, "SSD1452369","SSD", 500, 3500, 3500),
(9, "SSD1ASDA369","SSD", 250, 3500, 3500),
(3, "SSD1ASDAS52369","SSD", 140, 3500, 3500),
(9, "HDD789562", "HDD", 1000, 1500, 1200)
;

INSERT INTO RAM(id_brand, model_name, frequency, capacity, type_tech) VALUES
(3, "KV4568",2666,8,"DDR4"),
(3, "KV4568",2666,16,"DDR4"),
(3, "KV4568",1666,8,"DDR4"),
(3, "KV4568",2666,32,"DDR4"),
(4, "AD4568",1600,8,"DDR3"),
(4, "AD4568",3600,16,"DDR4"),
(4, "AD4512",2666,32,"DDR4")
;

INSERT INTO Screen(id_brand, model_name, resolution, type_tech, dimension) VALUES
(6,"AZ4568","FULLHD","LED",17),
(6,"AZ4568","4K","LCD",17),
(7,"AE4568","HD","LCD",21),
(8,"AF4568","4K","LCD",15)
;

INSERT INTO Computer(id_brand, id_ram, id_storage, id_screen, model_name, price, link_manual, quantity, keyboard_lang, launch_year) VALUES
(1,2,1,1,"NITRO5H4",15000,"https://example.com",10,"ENG",2020),
(1,3,3,1,"HELIOS5H4",1600,"https://example.com",10,"ENG",2020),
(5,3,4,3,"MEDIOSS5H4",24000,"https://example.com",10,"ENG",2020),
(6,5,3,1,"AHERO5H4",2000,"https://example.com",10,"ENG",2020),
(7,4,2,1,"WEQEQEQ",1800,"https://example.com",10,"ENG",2020),
(8,3,2,1,"ADADAAS",1800,"https://example.com",10,"ENG",2020),
(9,4,3,3,"QQEWEQE",2000,"https://example.com",10,"ENG",2020),
(8,5,4,2,"QEQE",15000,"https://example.com",10,"ENG",2020)
;

SELECT * FROM Computer;

