INSERT INTO	participant.services 
	(
	participantId,
	employeeId,
	Serviceid, 
	programid,
	userName,
	HMIS,
	quantity,
	comment,  
    timeCreated
	)
VALUES
	(
 	:participant_id, 
  	:employee_id, 
   	:service_id, 
    :enrollment_id,
    :user_name,
    :HMIS,
    :quantity,
    :comment,
    :time_created 
	)