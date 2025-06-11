/*Participants/Dashboard/ReferralsDetailSelect*/
SELECT 
	r.id as 'id',
	r.timeCreated as 'referral_date',
	r.providerId as 'provider_id',
	prov.providerName as 'provider_name',
	p_type.id as 'provider_type_id',
	r.Type_ID as 'type_id',
	r_type.ReferralTypeName as 'referral_type',
	r.Status_Id as 'status_id',
	r_status.ReferralStatusName as 'referral_status',
	r.ProgramId as 'program_id',
	p.programName as 'program_name'

FROM 
	[participant].[Referral] r
	LEFT JOIN [organization].[Provider] prov on r.providerId = prov.id
	LEFT JOIN [organization].[ProviderType] p_type on prov.providerTypeId = p_type.id
	LEFT JOIN [participant].[ReferralType] r_type on r.Type_id = r_type.id
	LEFT JOIN [participant].[ReferralStatus] r_status on r.Status_Id = r_status.id
	LEFT JOIN [interaction].[Program] p on p.id = r.programId 
WHERE
	r.ParticipantId =  :participant_id 
ORDER BY referral_date DESC;