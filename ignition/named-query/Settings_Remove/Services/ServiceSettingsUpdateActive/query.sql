UPDATE	interaction.Service 
SET	serviceName = :service_name,
 	serviceDescription = :service_desc,
 	serviceTypeId = :type_id, 
	timeCreated = :time_created,
	timeRetired = Null
WHERE id = :service_id;