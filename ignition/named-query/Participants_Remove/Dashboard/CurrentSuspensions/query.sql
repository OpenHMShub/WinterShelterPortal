/*KPI4----Participants/Dashboard/CurrentSuspensions*/
SELECT 
	[participant].[Suspension].id
FROM 
	[participant].[Participant]
INNER JOIN
	[participant].[Suspension]
ON
	[participant].[Participant].id=[participant].[Suspension].participantId
WHERE 
	[participant].[Participant].id IN (SELECT convert(int, value) FROM string_split(:IdList, ','))
AND
	getDATE() BETWEEN [participant].[Suspension].dateBegin AND [participant].[Suspension].dateEnd;

