/*---Settings/Humans/HumanSelect---*/
--SELECT TOP 100
SELECT
	h.human_id as 'human_id',
	h.first_name as 'first_name',
	ISNULL(h.middle_name,'') as 'middle_name',
	h.last_name as 'last_name',
	ISNULL(h.suffix,'') as 'suffix',
	ISNULL(h.nick_name,'') as 'nick_name',
	h.ssn as 'ssn',
	h.gender_id as 'gender_id',
	h.gender as 'gender',
	CAST(FORMAT (h.dob, 'MM/dd/yyyy') as varchar) as 'dob',
	--LEFT(CAST(FORMAT(h.dob,'MM/dd/yyyy') as varchar),2) as 'dob',
	--RIGHT(CAST(FORMAT(h.dob,'MM/dd/yyyy') as varchar),4) as 'dob',
	h.race_id as 'race_id',
	h.race as 'race',
	h.disability_id as 'disability_id',
	h.disability as 'disability',
	h.veteran_id as 'veteran_id',
	h.veteran as 'veteran',
	h.participant_id as 'participant_id',
	h.participant_retired as 'participant',
	h.employee_id as 'employee_id',
	--h.employee_retired as 'employee',
	1 as 'employee',
	h.volunteer_id as 'volunteer_id',
	--h.volunteer_retired as 'volunteer'
	2 as 'volunteer'

FROM
	humans.GroupMembership h
WHERE

 	{firstname} AND
 	{middlename} AND
 	{lastname} AND
 	{nickname} AND
 	{ssn} AND
 	{dobyear} AND
 	{raceid} AND
 	{search}


ORDER BY
	human_id
