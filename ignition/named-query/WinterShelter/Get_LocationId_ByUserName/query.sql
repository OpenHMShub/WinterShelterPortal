SELECT 
	l.id 
FROM 
	organization.Provider p
LEFT JOIN
	shelter.Location l ON l.locationName = p.providerName
WHERE
	p.providerName = :providerName

--SELECT id FROM shelter.Location 
--where congregationId = (SELECT id FROM organization.Congregation 
--where providerId = (SELECT id FROM organization.Provider where providername = 'Belmont University'))