SELECT
	[participant].[Suspension].id as 'id',
	[participant].[Suspension].incidentLogID as 'incident_id',
	[participant].[Suspension].suspensionTypeId as 'suspension_type_id',
	[participant].[SuspensionType].suspensionTypeName as 'suspension_type_name',
	[participant].[Suspension].Duration as 'suspension_duration',
	[participant].[Suspension].timeBegin as 'suspension_time_begin',
	[participant].[Suspension].timeEnd as 'suspension_time_end'
FROM
	[participant].[Suspension]
	LEFT JOIN [participant].[SuspensionType]
	ON [participant].[Suspension].suspensionTypeID = [participant].[SuspensionType].id
WHERE
	[participant].[Suspension].participantId =  :participant_id 
