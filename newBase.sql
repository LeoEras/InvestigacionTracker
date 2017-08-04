DROP DATABASE IF EXISTS Base;

DROP DATABASE IF EXISTS Base;

CREATE DATABASE IF NOT EXISTS Base CHARACTER SET utf8;

USE Base;

CREATE TABLE IF NOT EXISTS Application (
    id INT PRIMARY KEY AUTO_INCREMENT,
    application VARCHAR(100) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS Activity (
    id INT PRIMARY KEY AUTO_INCREMENT,
    activity VARCHAR(250) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS Term (
    id INT PRIMARY KEY AUTO_INCREMENT,
    term VARCHAR(7)
);

CREATE TABLE IF NOT EXISTS Class (
    id INT primary KEY auto_increment,
    class_name VARCHAR(12)
);

CREATE TABLE IF NOT EXISTS Users (
    id INT,
    termID INT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    PRIMARY KEY (id, termID),
    FOREIGN KEY (termID) REFERENCES Term(id)
);

CREATE TABLE IF NOT EXISTS Log (
    id INT PRIMARY KEY AUTO_INCREMENT,
    termID INT,
    activityID INT,
    start_date DATE,
    start_time TIME,
    end_date DATE,
    end_time TIME,
    elapsed_time TIME,
    applicationID INT,
    classID INT,
    relevance INT,
    userID INT,
    FOREIGN KEY (termID) REFERENCES Users(termID),
    FOREIGN KEY (activityID) REFERENCES Activity(id),
    FOREIGN KEY (applicationID) REFERENCES Application(id),
    FOREIGN KEY (classID) REFERENCES Class(id),
    FOREIGN KEY (userID) REFERENCES Users(id)
);

#DROP TABLE Activity;

INSERT INTO Term VALUES(null, "2016-1T");
INSERT INTO Term VALUES(null, "2016-2T");
INSERT INTO Term VALUES(null, "2017-1T");
INSERT INTO Term VALUES(null, "2017-2T");

INSERT INTO Class VALUES(null, "Applications");
INSERT INTO Class VALUES(null, "Documents");

#Primer término 2016
INSERT INTO Users VALUES(22, 1, "Julián Erick", "Adams Escobar");
INSERT INTO Users VALUES(23, 1, "Joyce Evelyn", "Benitez Pizarro");
INSERT INTO Users VALUES(37, 1, "Jorge Luis", "Cedeno Arteaga");
INSERT INTO Users VALUES(24, 1, "Branny Jamil", "Chito Chalan");
INSERT INTO Users VALUES(25, 1, "Guido Rubén", "Duchi Franco");
INSERT INTO Users VALUES(26, 1, "Kevin Ismael", "Filella Lok");
INSERT INTO Users VALUES(27, 1, "Juan José", "García Cedeno");
INSERT INTO Users VALUES(28, 1, "Stalyn Alfredo", "Gonzabay Yagual");
INSERT INTO Users VALUES(39, 1, "Angel Alexi", "Guerra Miketta");
INSERT INTO Users VALUES(40, 1, "Julio Cesar", "Guilindro Ordonez");
INSERT INTO Users VALUES(29, 1, "Carlos Luis", "Manosalvas Holst");
INSERT INTO Users VALUES(41, 1, "Wellington Andre", "Martinez Flores");
INSERT INTO Users VALUES(30, 1, "Edgar Daniel", "Moreira Apolo");
INSERT INTO Users VALUES(31, 1, "María Veronica", "Moreira Apolo");
INSERT INTO Users VALUES(38, 1, "Oscar Daniel", "Moreno Abad");
INSERT INTO Users VALUES(32, 1, "Ivan Marcelo", "Mosquera Carvajal");
INSERT INTO Users VALUES(42, 1, "Erick Alonso", "Perez Arguello");
INSERT INTO Users VALUES(36, 1, "Jorge Luis", "Rodríguez Castañeda");
INSERT INTO Users VALUES(35, 1, "Lenin Hochimi", "Tenecela Calderon");
INSERT INTO Users VALUES(33, 1, "Washington Jamil", "Velez Navarrete");
INSERT INTO Users VALUES(34, 1, "Ana Belén", "Yagual Meza");

#Segundo término 2016
INSERT INTO Users VALUES(1, 2, "Audra Tahis", "Atty Arteaga");
INSERT INTO Users VALUES(2, 2, "Carlos Manuel", "Leon Moran");
INSERT INTO Users VALUES(18, 2, "José Antonio", "Viteri Cuenca");
INSERT INTO Users VALUES(4, 2, "Karen Lilibeth", "Borbor Moreira");
INSERT INTO Users VALUES(10, 2, "Wilson Israel", "Plascencia Jordan");
INSERT INTO Users VALUES(12, 2, "Jorge Ernesto", "Garcia Garcia");
INSERT INTO Users VALUES(8, 2, "Xavier Fernando", "Idrovo Vallejo");
INSERT INTO Users VALUES(9, 2, "Joel Eduardo", "Rodriguez Llamuca");
INSERT INTO Users VALUES(7, 2, "Ivan Alejandro", "Mera Maldonado");
INSERT INTO Users VALUES(13, 2, "Madelyne Carolina", "Velasco Mite");
INSERT INTO Users VALUES(15, 2, "Leonardo Xavier", "Kuffo Rivero");
INSERT INTO Users VALUES(5, 2, "Jose Gabriel", "Cedeño Vargas");
INSERT INTO Users VALUES(17, 2, "Lucrecia Beatriz", "Vintimilla Cárdenas");
INSERT INTO Users VALUES(3, 2, "Juan Elías", "Alvarado Triana");
INSERT INTO Users VALUES(6, 2, "Ruddy Maricela", "Moncayo Rea");
INSERT INTO Users VALUES(21, 2, "Freddy Edmundo", "Samaniego Oyola");

#Primer término 2017
INSERT INTO Users VALUES(1, 3, "Guillermo Enrique", "Bernal Moreira");
INSERT INTO Users VALUES(2, 3, "John Aldo", "Cuesta Agila");
INSERT INTO Users VALUES(3, 3, "José Luis", "Masson Pinzón");
INSERT INTO Users VALUES(4, 3, "Fabricio Israel", "Layedra Montoya");
INSERT INTO Users VALUES(5, 3, "María Belén", "Guaranda Cabezas");
INSERT INTO Users VALUES(6, 3, "Jonathan Xavier", "Gorotiza Cornejo");
INSERT INTO Users VALUES(7, 3, "Galo Daniel", "Castillo López");
INSERT INTO Users VALUES(8, 3, "Julio Alexander", "Realpe Pineda");
INSERT INTO Users VALUES(9, 3, "Brenda Michelle", "Bermeo Burgos");
INSERT INTO Users VALUES(10, 3, "Renato Manuel", "Illescas Rodríguez");
INSERT INTO Users VALUES(11, 3, "Lenin Hochimin", "Tenecela Calderón");
INSERT INTO Users VALUES(12, 3, "Luis Fernando", "Zuñiga Rosado");
INSERT INTO Users VALUES(13, 3, "Anni Rosa", "Santacruz Hernandez");
INSERT INTO Users VALUES(14, 3, "Johan Alejandro", "Canales Reyes");
INSERT INTO Users VALUES(15, 3, "Daniel Josué", "Castro Peñafiel");
INSERT INTO Users VALUES(16, 3, "Paúl Domingo", "Estrada León");
INSERT INTO Users VALUES(17, 3, "Bryan Darío", "Tumbaco Moreira");
INSERT INTO Users VALUES(18, 3, "Elízabeth Meybol", "Sánchez Villamar");
INSERT INTO Users VALUES(19, 3, "Narcisa Fabiola", "Colcha Melendrez");
INSERT INTO Users VALUES(20, 3, "Arelys Mercedes", "Vintimilla Valencia");
INSERT INTO Users VALUES(21, 3, "Julio Alfredo", "Larrea Sánchez");
INSERT INTO Users VALUES(22, 3, "Alex Roberto", "Ferrín Alcívar");
INSERT INTO Users VALUES(23, 3, "Yu Chen", "Tai");
INSERT INTO Users VALUES(24, 3, "Robert Javier", "Loor Zambrano");

#UPDATE Users SET first_name = "Joel Eduardo" WHERE id = 9 AND termID = 2;
#use Base;
#SELECT * FROM Activity where activity = "Install MongoDB Community Edition on Windows — MongoDB Manual 3.2 - Google Chrome";
#SELECT applicationID FROM Log WHERE termID = 1 AND start_date >= "2016-07-21" AND end_date <= "2016-09-08" AND userID = 41 AND classID = 1;
#SELECT dates FROM Dates AS D, Log AS L where L.start_dateID = 273 and L.start_dateID = D.id;
#SELECT * FROM Application WHERE application = "untitled"
# count(applicationID)
#SELECT * FROM Application WHERE application LIKE "GitHub%" LIMIT 2000;
#select * from Users;