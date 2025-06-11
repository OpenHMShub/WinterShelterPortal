INSERT INTO	interaction.Service 
	(
 	serviceName,
 	serviceDescription,
 	serviceTypeId,
 	timeCreated 
	)
VALUES
	( 
	:service_name,
	:service_desc,
	:type_id,
	:time_created
	)