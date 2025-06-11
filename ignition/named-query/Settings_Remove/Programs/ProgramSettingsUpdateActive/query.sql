UPDATE	interaction.Program 
SET	programName = :program_name,
 	programDescription = :program_desc, 
	timeCreated = :time_created,
	timeRetired = Null
WHERE id = :program_id;