SELECT
	[participant].[Suspension].id as 'suspension_id',
	[participant].[Suspension].suspensionTypeId as 'suspension_type_id',
	[participant].[SuspensionType].suspensionTypeName as 'suspension_type_name',
	[participant].[Suspension].suspensionNotes as 'suspension_notes',
	[participant].[Suspension].Duration as 'suspension_duration',
	FORMAT([participant].[Suspension].dateBegin, 'MMM dd yyyy', 'us') as 'suspension_time_begin',
	FORMAT([participant].[Suspension].dateEnd, 'MMM dd yyyy', 'us')  as 'suspension_time_end',
	[participant].[Suspension].reinstateRequired 
FROM
	[participant].[Suspension]
	LEFT JOIN [participant].[SuspensionType]
	ON [participant].[Suspension].suspensionTypeID = [participant].[SuspensionType].id
WHERE 
	[participant].[Suspension].incidentLogId =  :incident_log_id 