---Participants/Reinstatement/SuspensionDetailSelect---

SELECT
	s.id,
	s.incidentLogID,
	i.incidentDescription,
	s.suspensionTypeIdRevised,
	s.suspensionTypeNameRevised,
	s.DurationRevised,
	CASE
	    WHEN DurationRevised = 1 THEN '1 Day'
    	WHEN DurationRevised = 7  THEN '1 Week'
    	WHEN DurationRevised = 14 THEN '2 Weeks'
    	WHEN DurationRevised = 30 THEN '30 Days'
    	WHEN DurationRevised = 60 THEN '60 Days'
    	WHEN DurationRevised = 90 THEN '90 Days'
    	WHEN DurationRevised = 365  THEN '1 Year'
    	WHEN DurationRevised = 3650  THEN 'Indefinite'
    	ELSE 'Other'
	END AS durationText,
	--FORMAT(s.dateBegin, 'MMM dd yyyy', 'us') AS 'dateBegin',
	--FORMAT(s.dateEndRevised, 'MMM dd yyyy', 'us') AS 'dateEndRevised',
	s.dateBegin,
	s.dateEndRevised,
	s.reinstateRequired,
	FORMAT(s.dateReinstated, 'MMM dd yyyy', 'us') AS 'dateReinstated',
	s.suspensionNotes,
	CASE
		WHEN s.dateReinstated is not Null THEN CAST (0 as bit)
		ELSE CAST (1 as bit)
	END AS 'suspensionActive'
FROM
	[participant].[SuspensionDashboard] s
	LEFT JOIN [participant].[IncidentLog] i
	ON i.id = s.incidentLogID

WHERE
	s.participantId =  :participant_id 
	AND {active}
ORDER BY s.dateEndRevised
