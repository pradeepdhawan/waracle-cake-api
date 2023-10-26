insert into cake (name, comment, imageurl, yumfactor)
 values ('Vanilla cake bad', 'Popular. size 18x18 inch', 'file://vanilla18by18.jpg', 6)

--CREATE DOMAIN rating AS smallint check (value in (1,2,3,4,5));

--ALTER TABLE cake ADD constraint yumfactor_check CHECK (yumfactor > 0 AND yumfactor <=5)

--describe cake

--select column_name, data_type, character_maximum_length, column_default, is_nullable
--from INFORMATION_SCHEMA.COLUMNS where table_name = 'cake'

