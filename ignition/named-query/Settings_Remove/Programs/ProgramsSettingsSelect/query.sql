DECLARE @retired DATETIME;
-- Set the active filter
IF :active != 1 BEGIN--Active Programs Only
	SET @retired = 1;
END
ELSE BEGIN
	SET @retired = 0;
END
SELECT
	[interaction].[program].id AS 'programId',
	[interaction].[program].programName AS 'programName',
	[interaction].[program].programDescription AS 'programDescription',
	[interaction].[program].timeRetired AS 'timeRetired',
	isNull((SELECT	STRING_AGG(pt.providerTypeName ,', ')
		FROM organization.ProviderType pt
		LEFT JOIN
			interaction.ProgramProviderTypes  ppt ON pt.id = ppt.providerTypeId
		LEFT JOIN
			interaction.Program prg ON ppt.programId  = prg.id
		WHERE prg.id = [interaction].[program].id 
		GROUP BY prg.id),'') AS 'providerTypes',
	CASE
		WHEN timeRetired is Null THEN CAST(1 AS BIT)
		ELSE CAST(0 AS BIT)
	END as 'active'
FROM
	[interaction].[program]
WHERE
	[interaction].[program].timeRetired is Null
OR
	[interaction].[program].timeRetired >
		CASE 
			WHEN @retired = 1 THEN 0
		END
ORDER BY programName ASC