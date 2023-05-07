-- ranks country origin of bands, ordered by the number of (non -unique) fans

SELECT band_name, (IFNULL(split, '2020') - formed) as lifespan
FROM `metal_bands`
WHERE style like '%Glam rock%'
ORDER BY lifespan DESC
