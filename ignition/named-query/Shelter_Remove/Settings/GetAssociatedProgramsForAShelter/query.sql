SELECT p.id, p.programName
FROM interaction.program p, lodging.FacilityAssociatedPrograms f
WHERE f.facilityId = :facilityId 
AND f.associatedProgramId = p.id
ORDER by p.id