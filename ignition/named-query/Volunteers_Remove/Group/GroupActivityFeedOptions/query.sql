---Volunteers/Details/ActivityFeedQuery--
----Participants/Activities/ActivityFeed----
Declare @groupId as int = :groupId ;

with Activities as (
SELECT
	0 AS ID,
	'GroupAdded' as CardType,
	V.timeCreated as Date
FROM staff.VolunteerGroup V
Where V.id = @groupId
union
SELECT
	VN.id AS ID,
	'Note' as CardType,	
	VN.timeCreated as Date
FROM staff.VolunteerNotes VN
Where VN.groupId = @groupId
union
SELECT
	I.instanceID AS ID,
	'NoShow' as CardType,	
	I.startDate as Date
FROM calendar.eventInstanceVolunteers V
LEFT JOIN calendar.eventInstances I on I.instanceID = V.instanceID
WHERE V.groupID = @groupId and I.endDate < GETDATE() and V.validation = 0
union
--SELECT
--	l.id AS ID,	
--	'MembersAdded' as CardType,	
--	l.timestamp as Date
--FROM staff.VolunteerUpdateLog l
--Where l.volunteerId = @volunteerId
--union
SELECT
	I.instanceID AS ID,
	'EventCompleted' as CardType,	
	I.startDate as Date
FROM calendar.eventInstanceVolunteers V
LEFT JOIN calendar.eventInstances I on I.instanceID = V.instanceID
WHERE V.groupID = @groupId and I.endDate < GETDATE() and V.validation = 1
)
Select DISTINCT CardType from Activities