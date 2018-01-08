
CREATE TABLE singer (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fullname TEXT,
    age INTEGER,
    band TEXT);
  
INSERT INTO singer (fullname, age, band) 
    VALUES ("Kylo Ren", 43, "DownFall");
INSERT INTO singer (fullname, age, band)
    VALUES ("Darth Vader", 26, "Avenge");
INSERT INTO singer (fullname, age, band)
    VALUES ("Some Day", 48, "Full of myself");
INSERT INTO singer (fullname, age, band)
    VALUES ("SirSnipesLDR", 19, "Band of misfits");
INSERT INTO singer (fullname, age, band)
    VALUES ("Pringles", 15, "In over his head");
CREATE TABLE singers_o (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    singer_id INTEGER,
    song TEXT);

INSERT INTO singers_o (singer_id, song)
    VALUES (1, "Full of myself");
INSERT INTO singers_o (singer_id, song)
    VALUES (1, "Full of himself");
INSERT INTO singers_o (singer_id, song)
    VALUES (1, "Too confident");
INSERT INTO singers_o (singer_id, song)
    VALUES (2, "Downfall");
INSERT INTO singers_o (singer_id, song)
    VALUES (2, "The dead");
INSERT INTO singers_o (singer_id, song)
    VALUES (2, "Fiery vengeance");
INSERT INTO singers_o(singer_id, song)
    VALUES (3, "agressive");
INSERT INTO singers_o (singer_id, song)
    VALUES (3, "Unfriended");
INSERT INTO singers_o (singer_id, song)
    VALUES (3, "Time for failure");
INSERT INTO singers_o (singer_id, song)
    VALUES (4, "Underdog");
INSERT INTO singers_o (singer_id, song)
    VALUES (4, "Leviathan-Raid");
INSERT INTO singers_o (singer_id, song)
    VALUES (4, "Flawless");
INSERT INTO singers_o (singer_id, song)
    VALUES (5, "Victory");
INSERT INTO singers_o (singer_id, song)
    VALUES (5, "Lights out");
INSERT INTO singers_o (singer_id, song)
    VALUES (5, "Midnight Coop");
SELECT singer.fullname AS name, singer.band, singers_o.song 
    FROM singer
    JOIN singers_o
    ON singer.id = singers_o.singer_id
    ORDER BY singer.fullname;
SELECT singer.fullname, singer.age, singers_o.song AS name
    FROM singer
    LEFT OUTER JOIN singers_o
    ON singer.id = singers_o .singer_id
    ORDER BY singer.age


