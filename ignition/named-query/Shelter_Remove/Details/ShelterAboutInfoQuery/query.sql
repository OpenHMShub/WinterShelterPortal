SELECT a.facilityName as ShelterName, b.facilityTypeName as ShelterType, concat (a.street, ' ', a.city, ' ', a.state) as address,
a.zipCode as zipCode, a.beds as beds, a.rooms as rooms, a.phone as phone, case when a.allResidential = 0 
then 
COALESCE(TableAssociatedPrograms.AssociatedPrograms , '')
else 'All Residential Programs'
end as associatedPrograms, 'None' as attributes
FROM lodging.Facility a, lodging.FacilityType b, (SELECT c.facilityId as facilityId, STRING_AGG(d.ProgramName, ', ') AS AssociatedPrograms
FROM lodging.FacilityAssociatedPrograms c LEFT JOIN interaction.Program d
ON c.associatedProgramId = d.id and c.facilityId = :shelterID
GROUP BY c.facilityId) as TableAssociatedPrograms
where a.timeRetired is null and a.id = :shelterID and a.facilityTypeId = b.id
and TableAssociatedPrograms.facilityId = a.id
   