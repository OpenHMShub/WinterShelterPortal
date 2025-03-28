---Participants/Enrollments/ParticipantEnrollments---

SELECT 
	programName, id
FROM 
	[interaction].[Program]
WHERE 
	{SearchQuery} 
ORDER BY 
	programName