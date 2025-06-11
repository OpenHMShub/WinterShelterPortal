---Participants/ServiceDropdownListAll
SELECT
	[interaction].[Service].id,[interaction].[Service].serviceName as 'service_name'
FROM
	[interaction].[Service]

ORDER BY service_name