DECLARE @retired DATETIME;
DECLARE @type INT;
-- Set the active filter
IF :active != 1 BEGIN--Active Programs Only
	SET @retired = 1;
END
ELSE BEGIN
	SET @retired = 0;
END
-- service type
IF :type >= 0 BEGIN
	SET @type = :type;
END
ELSE BEGIN
	SET @type = NULL;	
END
SELECT
	[interaction].[service].id AS 'serviceId',
	[interaction].[service].serviceName AS 'serviceName',
	[interaction].[service].serviceTypeId AS 'serviceTypeId',
	[interaction].[servicetype].serviceTypeName AS 'serviceType',
	isNull([interaction].[service].serviceDescription,'') AS 'serviceDescription',
	[interaction].[service].timeRetired AS 'timeRetired',
	isNull((SELECT	STRING_AGG(p.programName,', ')
		FROM interaction.Program  p
		LEFT JOIN
			interaction.ProgramService  ps ON p.id = ps.programId 
		--LEFT JOIN
		--	interaction.Program prg ON ppt.programId  = prg.id
		WHERE ps.serviceId  = [interaction].[service].id
		GROUP BY ps.serviceId),'') AS 'programNames',
	CASE
		WHEN [interaction].[service].timeRetired is Null THEN CAST(1 AS BIT)
		ELSE CAST(0 AS BIT)
	END as 'active'

FROM
	[interaction].[service]
	LEFT JOIN [interaction].[servicetype]
	ON [interaction].[service].serviceTypeId = [interaction].[servicetype].id
WHERE
	(
	[interaction].[service].timeRetired is Null
	OR
	[interaction].[service].timeRetired >
		CASE 
			WHEN @retired = 1 THEN 0
		END
	)
AND
	[interaction].[service].serviceTypeId = ISNULL(@type,serviceTypeId)
ORDER BY serviceName ASC