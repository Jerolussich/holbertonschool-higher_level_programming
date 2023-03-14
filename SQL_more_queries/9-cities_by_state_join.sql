-- lists all cities containes in db

SELECT cities.id, cities.name, states.name FROM cities
JOIN states ON cities.state_id = states.id;