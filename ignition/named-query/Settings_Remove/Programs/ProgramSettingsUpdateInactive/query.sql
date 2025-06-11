UPDATE	interaction.Program 
SET	programName = :program_name,
 	programDescription = :program_desc, 
	timeCreated = :time_created,
 	timeRetired =  :time_retired 
WHERE id = :program_id;