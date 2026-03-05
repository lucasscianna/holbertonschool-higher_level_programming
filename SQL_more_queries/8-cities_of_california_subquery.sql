-- Lists all cities of California found in the database hbtn_0d_usa
-- Results are sorted by cities.id in ascending order
-- The JOIN keyword is not used
SELECT id, name FROM cities
WHERE state_id = (
    SELECT id FROM states
    WHERE name = 'California'
)
ORDER BY id ASC;