CREATE TABLE Product
(
    maker INTEGER NOT NULL,
    model INTEGER NOT NULL,
    type  INTEGER NOT NULL,
    CONSTRAINT model PRIMARY KEY (model)
);

CREATE TABLE PC
(
    code  INTEGER NOT NULL,
    model INTEGER NOT NULL,
    speed INTEGER NOT NULL,
    ram   INTEGER NOT NULL,
    hd    INTEGER NOT NULL,
    cd    INTEGER NOT NULL,
    price INTEGER NOT NULL,
    CONSTRAINT model FOREIGN KEY (model) REFERENCES product (model)
);

CREATE TABLE Laptop
(
    code   INTEGER NOT NULL,
    model  INTEGER NOT NULL,
    speed  INTEGER NOT NULL,
    ram    INTEGER NOT NULL,
    hd     INTEGER NOT NULL,
    cd     INTEGER NOT NULL,
    price  INTEGER NOT NULL,
    screen INTEGER NOT NULL,
    CONSTRAINT model FOREIGN KEY (model) REFERENCES product (model)
);

CREATE TABLE Printer
(
    code  INTEGER NOT NULL,
    model INTEGER NOT NULL,
    color INTEGER NOT NULL,
    type  INTEGER NOT NULL,
    price INTEGER NOT NULL,
    CONSTRAINT model FOREIGN KEY (model) REFERENCES product (model)
);

INSERT INTO Product
    (maker, model, type)
SELECT floor(random() * 300) AS maker,
       i                     AS model,
       floor(random() * 3)   AS type
FROM generate_series(1, 3000) AS i;

INSERT INTO PC
    (code, model, speed, ram, hd, cd, price)
SELECT floor(random() * 1000)               AS code,
       i                                    AS model,
       floor(random() * 5)                  AS speed,
       16 * power(2, floor(random() * 5))   AS ram,
       256 * power(2, floor(random() * 10)) AS hd,
       4 * floor(random() * 5)              AS cd,
       floor(random() * 5000)               AS price
FROM generate_series(1, 1000) AS i;

INSERT INTO Laptop
    (code, model, speed, ram, hd, cd, price, screen)
SELECT floor(random() * 1000)               AS code,
       i                                    AS model,
       floor(random() * 5)                  AS speed,
       16 * power(2, floor(random() * 5))   AS ram,
       256 * power(2, floor(random() * 10)) AS hd,
       4 * floor(random() * 5)              AS cd,
       floor(random() * 3000)               AS price,
       floor(random() * 24)                 AS screen
FROM generate_series(1001, 2000) AS i;

INSERT INTO Printer
    (code, model, color, type, price)
SELECT floor(random() * 1000) AS code,
       i                      AS model,
       floor(random() * 16)   AS color,
       floor(random() * 3)    AS type,
       floor(random() * 2000) AS price
FROM generate_series(2001, 3000) AS i;

--TRUNCATE Laptop, Printer, PC, Product CASCADE;

--1
SELECT DISTINCT PC_1.model, PC_2.model, speed, ram
FROM PC AS PC_1
         INNER JOIN PC AS PC_2 USING (speed, ram)
WHERE PC_1.model > PC_2.model;

--2.1
WITH result AS (SELECT maker, pc.model
                FROM Product pc
                         RIGHT JOIN (SELECT model, speed, ram
                                     FROM PC
                                     WHERE ram = (SELECT min(ram) FROM PC)
                                     UNION
                                     (WiTH PC_and_Laptop AS (
                                         SELECT model, speed, ram
                                         FROM PC
                                         UNION
                                         SELECT model, speed, ram
                                         FROM Laptop
                                     )
                                      SELECT *
                                      FROM PC_and_Laptop
                                      WHERE (speed = (SELECT max(speed) FROM PC_and_Laptop)
                                          AND ram = (SELECT min(ram) FROM PC_and_Laptop)))) pc_lap ON pc.model = pc_lap.model
                         INNER JOIN (SELECT maker, pr.model
                                     FROM Product pr
                                              RIGHT JOIN
                                          (SELECT model
                                           FROM Printer) print ON pr.model = print.model) AS main USING (maker)
)
SELECT DISTINCT maker as print_makers
FROM result
ORDER BY print_makers;


--2.2
WITH result AS (SELECT maker, pc.model
                FROM Product pc
                         RIGHT JOIN (SELECT model, speed, ram
                                     FROM PC
                                     WHERE ram = (SELECT min(ram) FROM PC)
                                     UNION
                                     SELECT model, speed, ram
                                     FROM PC
                                     WHERE (speed = (SELECT max(speed) FROM PC)
                                         AND ram = (SELECT min(ram) FROM PC))
                ) pc_lap ON pc.model = pc_lap.model
                         INNER JOIN (SELECT maker, pr.model
                                     FROM Product pr
                                              RIGHT JOIN
                                          (SELECT model
                                           FROM Printer) print ON pr.model = print.model) AS main USING (maker)
)
SELECT DISTINCT maker as print_makers
FROM result
ORDER BY print_makers;