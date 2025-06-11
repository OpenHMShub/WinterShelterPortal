---Participants/CaseNotes/CaseNotesDetailSelect---
DECLARE @activity_range AS INT = :activity_range
--Calculate the begin and end activity dates
DECLARE	@activity_start AS DATE = DATEADD(day, (-1 * @activity_range), getdate())
	,@activity_end AS DATE = DATEADD(day,1,getdate());
SELECT
	[participant].[CaseNotes].id AS 'id',
	[participant].[CaseNotes].employeeId AS 'employee_id',
	CONCAT([humans].[Human].firstName,' ',[humans].[Human].middleName,' ',[humans].[Human].lastName) as 'employee_name',
	[participant].[CaseNotes].HMIS AS 'hmis',
	[participant].[CaseNotes].CaseNoteTypeID as 'note_type_id',
	[participant].[CaseNoteType].CaseNoteTypeName as 'note_type',
	[participant].[CaseNotes].Note as 'note',
	[participant].[CaseNotes].timeCreated AS 'time_created'
FROM
	[participant].[CaseNotes]
	LEFT JOIN [participant].[CaseNoteType]
	ON [participant].[CaseNotes].CaseNoteTypeID = [participant].[CaseNoteType].Id
	LEFT JOIN staff.Employee
	ON [participant].[CaseNotes].employeeId = [staff].[Employee].Id
	LEFT JOIN [humans].[Human] 
	ON [staff].[Employee].humanId = [humans].[Human].id
WHERE 	
	[participant].[CaseNotes]. participantId =  :participant_id AND
	[participant].[CaseNotes].timeCreated between @activity_start and @activity_end AND
	{notedate} AND
 	{notetype} AND
 	{hmis} AND
 	{enteredby} AND
 	{search}
ORDER BY time_created DESC