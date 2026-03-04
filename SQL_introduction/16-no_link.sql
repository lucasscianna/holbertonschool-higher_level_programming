-- Liste les enregistrements ayant un nom, triés par score décroissant
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;