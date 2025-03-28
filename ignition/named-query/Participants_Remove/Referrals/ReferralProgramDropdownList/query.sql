---Participants/Referrals/ReferralProgramDropdownList---
SELECT
	p.id
	,p.programName
FROM
	[interaction].[Program] p
	LEFT JOIN interaction.ProgramProviderTypes pt ON p.id=pt.programId 
WHERE
 	{provider} 
GROUP BY p.id
		,p.programName
ORDER BY programName