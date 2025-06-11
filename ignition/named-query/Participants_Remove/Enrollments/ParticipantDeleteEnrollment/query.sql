IF EXISTS(
	SELECT 
		id 
	FROM 
		[participant].[Enrollments] 
	WHERE 
		id = :enrollmentId)
DELETE FROM 
		[participant].[Enrollments] 
	WHERE 
		id = :enrollmentId