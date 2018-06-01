CREATE TABLE permisos (id_tarjeta BIGINT NOT NULL PRIMARY KEY, usuario VARCHAR(100), permiso BOOL NOT NULL);

INSERT INTO permisos VALUES (441294522346, 'Tarjeta Blanca', 1);


USE datos_iot;

SELECT * FROM permisos;

SELECT permiso FROM permisos WHERE id_tarjeta=



DELETE FROM permisos WHERE id_tarjeta=990154079132

DROP TABLE permisos;







CREATE TABLE registro (id_tarjeta BIGINT NOT NULL, usuario VARCHAR(100), fecha DATETIME);


INSERT INTO registro VALUES ()