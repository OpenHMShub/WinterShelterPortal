IF NOT EXISTS (
	SELECT 
		[participant].[Enrollments].programId, 
		[participant].[Enrollments].particpantId
	FROM 
		[participant].[Enrollments] 
	WHERE 
		[participant].[Enrollments].programId =:programId AND [participant].[Enrollments].particpantId =:participantId
		)






INSERT INTO [participant].[Enrollments] (
	particpantID, 
	programId
	)
VALUES(
	:participantId, 
	:programId
	);