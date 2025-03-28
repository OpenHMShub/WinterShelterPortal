/*---WinterShelter/FindVolunteers---*/

SELECT TOP 100
	'' as 'options',
	v.ID as 'volunteerId',
	h.ID as 'humanId',
	h.firstName  as 'firstName',
	ISNULL(h.middleName,'')  as 'middleName',
	h.lastName  as 'lastName',
	ISNULL(h.nickname,'')  as 'nickName',
	FORMAT(h.dob, 'd', 'us') AS 'dob',
	DATEPART(day,h.dob) as 'dobDay',
	DATEPART(month,h.dob) as 'dobMonth',
	ISNULL(h.email ,'')  as 'email'


FROM
	staff.Volunteer v
	INNER JOIN  humans.Human h on v.humanId = h.id
	LEFT JOIN  staff.VolunteerGroup vg ON v.volunteerGroupId = vg.id

WHERE
	v.timeRetired is null
	AND
	v.volunteerIdentifier is not null
	AND
	{firstName} 
	AND
	{middleName}
	AND
	{lastName}
	AND
	{nickName} 
	AND
	{dobYear} 
	AND
	{dobMonth} 
	AND
	{dobDay} 
	AND
	{search} 
	AND
	{email}

