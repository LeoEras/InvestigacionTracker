drop database if exists investigacion;

CREATE database if not exists investigacion;

use investigacion;

CREATE TABLE if not exists Datos  (
    id INT primary KEY auto_increment,
    periodo smallint,
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

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/2016-1T/depurado22.csv' INTO TABLE datos
FIELDS TERMINATED BY '|' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
(actividad, dia_inicio, hora_inicio, dia_final, hora_final, tiempo, responsable, clase, importancia, usuario)
set id = null, periodo = 1;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/2016-1T/depurado23.csv' INTO TABLE datos
FIELDS TERMINATED BY '|' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
(actividad, dia_inicio, hora_inicio, dia_final, hora_final, tiempo, responsable, clase, importancia, usuario)
set id = null, periodo = 1;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/2016-1T/depurado24.csv' INTO TABLE datos
FIELDS TERMINATED BY '|' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
(actividad, dia_inicio, hora_inicio, dia_final, hora_final, tiempo, responsable, clase, importancia, usuario)
set id = null, periodo = 1;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/2016-1T/depurado25.csv' INTO TABLE datos
FIELDS TERMINATED BY '|' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
(actividad, dia_inicio, hora_inicio, dia_final, hora_final, tiempo, responsable, clase, importancia, usuario)
set id = null, periodo = 1;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/2016-1T/depurado26.csv' INTO TABLE datos
FIELDS TERMINATED BY '|' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
(actividad, dia_inicio, hora_inicio, dia_final, hora_final, tiempo, responsable, clase, importancia, usuario)
set id = null, periodo = 1;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/2016-1T/depurado27.csv' INTO TABLE datos
FIELDS TERMINATED BY '|' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
(actividad, dia_inicio, hora_inicio, dia_final, hora_final, tiempo, responsable, clase, importancia, usuario)
set id = null, periodo = 1;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/2016-1T/depurado28.csv' INTO TABLE datos
FIELDS TERMINATED BY '|' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
(actividad, dia_inicio, hora_inicio, dia_final, hora_final, tiempo, responsable, clase, importancia, usuario)
set id = null, periodo = 1;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/2016-1T/depurado29.csv' INTO TABLE datos
FIELDS TERMINATED BY '|' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
(actividad, dia_inicio, hora_inicio, dia_final, hora_final, tiempo, responsable, clase, importancia, usuario)
set id = null, periodo = 1;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/2016-1T/depurado30.csv' INTO TABLE datos
FIELDS TERMINATED BY '|' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
(actividad, dia_inicio, hora_inicio, dia_final, hora_final, tiempo, responsable, clase, importancia, usuario)
set id = null, periodo = 1;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/2016-1T/depurado31.csv' INTO TABLE datos
FIELDS TERMINATED BY '|' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
(actividad, dia_inicio, hora_inicio, dia_final, hora_final, tiempo, responsable, clase, importancia, usuario)
set id = null, periodo = 1;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/2016-1T/depurado32.csv' INTO TABLE datos
FIELDS TERMINATED BY '|' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
(actividad, dia_inicio, hora_inicio, dia_final, hora_final, tiempo, responsable, clase, importancia, usuario)
set id = null, periodo = 1;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/2016-1T/depurado33.csv' INTO TABLE datos
FIELDS TERMINATED BY '|' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
(actividad, dia_inicio, hora_inicio, dia_final, hora_final, tiempo, responsable, clase, importancia, usuario)
set id = null, periodo = 1;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/2016-1T/depurado34.csv' INTO TABLE datos
FIELDS TERMINATED BY '|' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
(actividad, dia_inicio, hora_inicio, dia_final, hora_final, tiempo, responsable, clase, importancia, usuario)
set id = null, periodo = 1;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/2016-1T/depurado35.csv' INTO TABLE datos
FIELDS TERMINATED BY '|' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
(actividad, dia_inicio, hora_inicio, dia_final, hora_final, tiempo, responsable, clase, importancia, usuario)
set id = null, periodo = 1;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/2016-1T/depurado36.csv' INTO TABLE datos
FIELDS TERMINATED BY '|' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
(actividad, dia_inicio, hora_inicio, dia_final, hora_final, tiempo, responsable, clase, importancia, usuario)
set id = null, periodo = 1;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/2016-1T/depurado37.csv' INTO TABLE datos
FIELDS TERMINATED BY '|' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
(actividad, dia_inicio, hora_inicio, dia_final, hora_final, tiempo, responsable, clase, importancia, usuario)
set id = null, periodo = 1;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/2016-1T/depurado38.csv' INTO TABLE datos
FIELDS TERMINATED BY '|' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
(actividad, dia_inicio, hora_inicio, dia_final, hora_final, tiempo, responsable, clase, importancia, usuario)
set id = null, periodo = 1;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/2016-1T/depurado39.csv' INTO TABLE datos
FIELDS TERMINATED BY '|' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
(actividad, dia_inicio, hora_inicio, dia_final, hora_final, tiempo, responsable, clase, importancia, usuario)
set id = null, periodo = 1;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/2016-1T/depurado40.csv' INTO TABLE datos
FIELDS TERMINATED BY '|' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
(actividad, dia_inicio, hora_inicio, dia_final, hora_final, tiempo, responsable, clase, importancia, usuario)
set id = null, periodo = 1;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/2016-1T/depurado41.csv' INTO TABLE datos
FIELDS TERMINATED BY '|' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
(actividad, dia_inicio, hora_inicio, dia_final, hora_final, tiempo, responsable, clase, importancia, usuario)
set id = null, periodo = 1;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/2016-1T/depurado42.csv' INTO TABLE datos
FIELDS TERMINATED BY '|' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
(actividad, dia_inicio, hora_inicio, dia_final, hora_final, tiempo, responsable, clase, importancia, usuario)
set id = null, periodo = 1;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/2016-1T/depurado43.csv' INTO TABLE datos
FIELDS TERMINATED BY '|' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
(actividad, dia_inicio, hora_inicio, dia_final, hora_final, tiempo, responsable, clase, importancia, usuario)
set id = null, periodo = 1;