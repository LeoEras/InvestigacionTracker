drop database if exists investigacion;

CREATE database if not exists investigacion;

use investigacion;

CREATE TABLE if not exists Datos  (
    id INT primary KEY auto_increment,
    actividad varchar(300),
    dia_inicio date,
    hora_inicio time,
    dia_final date,
    hora_final time,
    tiempo time,
    responsable VARCHAR(100),
    clase varchar(15),
    importancia int,
    usuario int
);

SET @@global.sql_mode= '';

SHOW VARIABLES LIKE 'secure_file_priv';

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/2016-2T/depurado1.csv' INTO TABLE datos
FIELDS TERMINATED BY '|' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
(actividad, dia_inicio, hora_inicio, dia_final, hora_final, tiempo, responsable, clase, importancia, usuario)
set id = null;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/2016-2T/depurado2.csv' INTO TABLE datos
FIELDS TERMINATED BY '|' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
(actividad, dia_inicio, hora_inicio, dia_final, hora_final, tiempo, responsable, clase, importancia, usuario)
set id = null;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/2016-2T/depurado3.csv' INTO TABLE datos
FIELDS TERMINATED BY '|' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
(actividad, dia_inicio, hora_inicio, dia_final, hora_final, tiempo, responsable, clase, importancia, usuario)
set id = null;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/2016-2T/depurado4.csv' INTO TABLE datos
FIELDS TERMINATED BY '|' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
(actividad, dia_inicio, hora_inicio, dia_final, hora_final, tiempo, responsable, clase, importancia, usuario)
set id = null;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/2016-2T/depurado5.csv' INTO TABLE datos
FIELDS TERMINATED BY '|' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
(actividad, dia_inicio, hora_inicio, dia_final, hora_final, tiempo, responsable, clase, importancia, usuario)
set id = null;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/2016-2T/depurado6.csv' INTO TABLE datos
FIELDS TERMINATED BY '|' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
(actividad, dia_inicio, hora_inicio, dia_final, hora_final, tiempo, responsable, clase, importancia, usuario)
set id = null;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/2016-2T/depurado7.csv' INTO TABLE datos
FIELDS TERMINATED BY '|' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
(actividad, dia_inicio, hora_inicio, dia_final, hora_final, tiempo, responsable, clase, importancia, usuario)
set id = null;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/2016-2T/depurado8.csv' INTO TABLE datos
FIELDS TERMINATED BY '|' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
(actividad, dia_inicio, hora_inicio, dia_final, hora_final, tiempo, responsable, clase, importancia, usuario)
set id = null;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/2016-2T/depurado9.csv' INTO TABLE datos
FIELDS TERMINATED BY '|' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
(actividad, dia_inicio, hora_inicio, dia_final, hora_final, tiempo, responsable, clase, importancia, usuario)
set id = null;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/2016-2T/depurado10.csv' INTO TABLE datos
FIELDS TERMINATED BY '|' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
(actividad, dia_inicio, hora_inicio, dia_final, hora_final, tiempo, responsable, clase, importancia, usuario)
set id = null;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/2016-2T/depurado13.csv' INTO TABLE datos
FIELDS TERMINATED BY '|' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
(actividad, dia_inicio, hora_inicio, dia_final, hora_final, tiempo, responsable, clase, importancia, usuario)
set id = null;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/2016-2T/depurado14.csv' INTO TABLE datos
FIELDS TERMINATED BY '|' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
(actividad, dia_inicio, hora_inicio, dia_final, hora_final, tiempo, responsable, clase, importancia, usuario)
set id = null;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/2016-2T/depurado15.csv' INTO TABLE datos
FIELDS TERMINATED BY '|' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
(actividad, dia_inicio, hora_inicio, dia_final, hora_final, tiempo, responsable, clase, importancia, usuario)
set id = null;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/2016-2T/depurado17.csv' INTO TABLE datos
FIELDS TERMINATED BY '|' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
(actividad, dia_inicio, hora_inicio, dia_final, hora_final, tiempo, responsable, clase, importancia, usuario)
set id = null;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/2016-2T/depurado18.csv' INTO TABLE datos
FIELDS TERMINATED BY '|' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
(actividad, dia_inicio, hora_inicio, dia_final, hora_final, tiempo, responsable, clase, importancia, usuario)
set id = null;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/2016-2T/depurado21.csv' INTO TABLE datos
FIELDS TERMINATED BY '|' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
(actividad, dia_inicio, hora_inicio, dia_final, hora_final, tiempo, responsable, clase, importancia, usuario)
set id = null;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/2016-2T/depurado22.csv' INTO TABLE datos
FIELDS TERMINATED BY '|' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
(actividad, dia_inicio, hora_inicio, dia_final, hora_final, tiempo, responsable, clase, importancia, usuario)
set id = null;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/2016-2T/depurado24.csv' INTO TABLE datos
FIELDS TERMINATED BY '|' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
(actividad, dia_inicio, hora_inicio, dia_final, hora_final, tiempo, responsable, clase, importancia, usuario)
set id = null;