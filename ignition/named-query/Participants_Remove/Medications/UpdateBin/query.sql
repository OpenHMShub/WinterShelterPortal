UPDATE
	participant.StorageBinsLog

SET
	createdOn = GETDATE(),
	startOn = :startOn,
	expireOn = :expireOn
	
WHERE
	Id = :id