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
	[interaction].[program].timeRetired AS 'timeRetired'

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