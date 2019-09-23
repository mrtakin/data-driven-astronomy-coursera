SELECT radius, t_eff
FROM star
WHERE radius > 1;

SELECT kepler_id, t_eff
FROM star
WHERE t_eff BETWEEN 5000 AND 6000;

SELECT kepler_name, radius
FROM planet
WHERE kepler_name IS NOT NULL AND
      radius BETWEEN 1 AND 3;

SELECT MIN(radius), MAX(RADIUS), AVG(RADIUS), STDDEV(RADIUS)
FROM planet
WHERE kepler_name IS NULL

-- find out how many planets in the Planet database are in a multi-planet system.
SELECT kepler_id, COUNT(*)
FROM planet
GROUP BY kepler_id
HAVING COUNT(*) > 1
ORDER BY COUNT(*) DESC;

-- a query that returns the radius of each star and planet pair whose radii have a ratio greater than the Sun-to-Earth radius ratio. 
SELECT s.radius AS sun_radius, p.radius AS planet_radius
FROM star AS s, planet AS p
WHERE s.kepler_id = p.kepler_id AND
      s.radius > p.radius
ORDER BY s.radius DESC;

-- a query which counts the number of planets in each solar system where the corresponding stars are larger than our sun 
SELECT s.radius, COUNT(*) AS count
FROM star AS s, planet AS p
WHERE s.kepler_id = p.kepler_id AND s.radius >= 1
GROUP BY s.kepler_id
HAVING COUNT(*)  > 1
ORDER BY s.radius DESC;

-- a query which returns the kepler_id, t_eff and radius for all stars in the Star table which haven't got a planet as join partner. 
SELECT s.kepler_id, s.t_eff, s.radius 
FROM star s LEFT OUTER JOIN planet p ON (s.kepler_id = p.kepler_id)
WHERE p.koi_name IS NULL
ORDER BY t_eff DESC;

SELECT ROUND(AVG(p.t_eq), 1), MIN(s.t_eff), MAX(s.t_eff)
FROM star AS s, planet AS p
WHERE s.kepler_id = p.kepler_id AND
      s.t_eff > (SELECT AVG(t_eff) FROM star)

-- finds the radii of those planets in the Planet table which orbit the five largest stars in the Star table.
SELECT p.koi_name, p.radius, t2.radius
FROM planet AS p, (SELECT * FROM star AS s ORDER BY s.radius DESC LIMIT 5) AS t2
WHERE p.kepler_id = t2.kepler_id;



