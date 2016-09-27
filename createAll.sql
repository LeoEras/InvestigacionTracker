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

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/depurado22.csv' INTO TABLE datos
FIELDS TERMINATED BY '|' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
(actividad, dia_inicio, hora_inicio, dia_final, hora_final, tiempo, responsable, clase, importancia, usuario)
set id = null;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/depurado23.csv' INTO TABLE datos
FIELDS TERMINATED BY '|' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
(actividad, dia_inicio, hora_inicio, dia_final, hora_final, tiempo, responsable, clase, importancia, usuario)
set id = null;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/depurado24.csv' INTO TABLE datos
FIELDS TERMINATED BY '|' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
(actividad, dia_inicio, hora_inicio, dia_final, hora_final, tiempo, responsable, clase, importancia, usuario)
set id = null;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/depurado25.csv' INTO TABLE datos
FIELDS TERMINATED BY '|' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
(actividad, dia_inicio, hora_inicio, dia_final, hora_final, tiempo, responsable, clase, importancia, usuario)
set id = null;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/depurado26.csv' INTO TABLE datos
FIELDS TERMINATED BY '|' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
(actividad, dia_inicio, hora_inicio, dia_final, hora_final, tiempo, responsable, clase, importancia, usuario)
set id = null;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/depurado27.csv' INTO TABLE datos
FIELDS TERMINATED BY '|' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
(actividad, dia_inicio, hora_inicio, dia_final, hora_final, tiempo, responsable, clase, importancia, usuario)
set id = null;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/depurado28.csv' INTO TABLE datos
FIELDS TERMINATED BY '|' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
(actividad, dia_inicio, hora_inicio, dia_final, hora_final, tiempo, responsable, clase, importancia, usuario)
set id = null;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/depurado29.csv' INTO TABLE datos
FIELDS TERMINATED BY '|' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
(actividad, dia_inicio, hora_inicio, dia_final, hora_final, tiempo, responsable, clase, importancia, usuario)
set id = null;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/depurado30.csv' INTO TABLE datos
FIELDS TERMINATED BY '|' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
(actividad, dia_inicio, hora_inicio, dia_final, hora_final, tiempo, responsable, clase, importancia, usuario)
set id = null;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/depurado31.csv' INTO TABLE datos
FIELDS TERMINATED BY '|' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
(actividad, dia_inicio, hora_inicio, dia_final, hora_final, tiempo, responsable, clase, importancia, usuario)
set id = null;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/depurado32.csv' INTO TABLE datos
FIELDS TERMINATED BY '|' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
(actividad, dia_inicio, hora_inicio, dia_final, hora_final, tiempo, responsable, clase, importancia, usuario)
set id = null;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/depurado33.csv' INTO TABLE datos
FIELDS TERMINATED BY '|' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
(actividad, dia_inicio, hora_inicio, dia_final, hora_final, tiempo, responsable, clase, importancia, usuario)
set id = null;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/depurado34.csv' INTO TABLE datos
FIELDS TERMINATED BY '|' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
(actividad, dia_inicio, hora_inicio, dia_final, hora_final, tiempo, responsable, clase, importancia, usuario)
set id = null;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/depurado35.csv' INTO TABLE datos
FIELDS TERMINATED BY '|' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
(actividad, dia_inicio, hora_inicio, dia_final, hora_final, tiempo, responsable, clase, importancia, usuario)
set id = null;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/depurado36.csv' INTO TABLE datos
FIELDS TERMINATED BY '|' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
(actividad, dia_inicio, hora_inicio, dia_final, hora_final, tiempo, responsable, clase, importancia, usuario)
set id = null;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/depurado37.csv' INTO TABLE datos
FIELDS TERMINATED BY '|' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
(actividad, dia_inicio, hora_inicio, dia_final, hora_final, tiempo, responsable, clase, importancia, usuario)
set id = null;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/depurado38.csv' INTO TABLE datos
FIELDS TERMINATED BY '|' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
(actividad, dia_inicio, hora_inicio, dia_final, hora_final, tiempo, responsable, clase, importancia, usuario)
set id = null;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/depurado39.csv' INTO TABLE datos
FIELDS TERMINATED BY '|' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
(actividad, dia_inicio, hora_inicio, dia_final, hora_final, tiempo, responsable, clase, importancia, usuario)
set id = null;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/depurado40.csv' INTO TABLE datos
FIELDS TERMINATED BY '|' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
(actividad, dia_inicio, hora_inicio, dia_final, hora_final, tiempo, responsable, clase, importancia, usuario)
set id = null;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/depurado41.csv' INTO TABLE datos
FIELDS TERMINATED BY '|' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
(actividad, dia_inicio, hora_inicio, dia_final, hora_final, tiempo, responsable, clase, importancia, usuario)
set id = null;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/depurado42.csv' INTO TABLE datos
FIELDS TERMINATED BY '|' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
(actividad, dia_inicio, hora_inicio, dia_final, hora_final, tiempo, responsable, clase, importancia, usuario)
set id = null;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/depurado43.csv' INTO TABLE datos
FIELDS TERMINATED BY '|' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
(actividad, dia_inicio, hora_inicio, dia_final, hora_final, tiempo, responsable, clase, importancia, usuario)
set id = null;