---Participants/Personal/PersonalDetailSelect---
SELECT 
	h.id as 'human_id'
	,h.fullRegistration 
	,p.timeRetired  as 'time_retired'
	,p.timeRegistered   as 'time_registered'
	,p.suspensionActive as 'suspension_active'
	,p.caseManagerId as 'case_manager_id'
	,CONCAT_WS(' ',cmh.firstName, cmh.middleName, cmh.lastName) as 'employee_name'
	,h.SSN  as 'ssn'
	,h.ssnQualityId as 'ssn_quality_id'
	,hs.ssnQualityName as 'ssn_quality'
	,h.firstName as 'first_name'
	,h.middleName as 'middle_name'
	,h.lastName as 'last_name'
	,h.suffix as 'suffix_name'
	,h.nickname as 'nick_name'
	,h.dob as 'dob'
	,h.dobQualityId as 'dob_quality_id'
	,hdob.dobQualityName as 'dob_quality'
	,CAST((DATEDIFF(day, h.dob, GetDate()))/365.25 as INT) as 'Age'
	,h.genderId as 'gender_id'
	,hg.genderName as 'gender'
	,h.raceId as 'race_id'
	,hr.raceName as 'race'
	,h.ethnicityId as 'ethnicity_id'
	,he.ethnicityName as 'ethnicity'
	,h.timeDeceased as 'time_deceased'
	,h.veteranStatusId as 'veteran_id'
	,hv.veteranStatusName as 'veteran'
	,h.disabilityTypeId as 'disability_id'
	,hd.disabilityTypeName as 'disability'
	,h.trimorbid as 'tri_morbid'
	,h.chronicHomeless as 'chronic_homeless'
	,h.sexOffendRegistry as 'so_registry'
	,h.mailService as 'mail_service'
	,h.familyId  as 'family_id'
	,hf.surname as 'family'
	,h.hohRelationshipId as 'hoh_relationship_id'
	,hh.hohRelationshipName as 'hoh_relationship'
	,h.street as 'street'
	,h.city as 'city'
	,h.state as 'state'
	,h.zipCode as 'zip_code'
	,h.phone as 'phone'
	,h.altPhone as 'alt_phone'
	,h.email as 'email'
	,h.communicationTypeId as 'communication_type_id'
	,h.InsuranceTypeID as 'insurance_type_id'
	,hc.communicationTypeName as 'communication_type'
	,h.emergencyContactName as 'emergency_contact_name'
	,h.emergencyContactTypeId as 'emergency_contact_type_id'
	,h.emergencyContactPhone as 'emergency_contact_phone'
	,h.emergencyContactEmail as 'emergency_contact_email'
	,h.employer as 'employer'
	,h.school as 'school' 
	,h.congregation as 'congregation'
	
FROM
	[humans].[Human] h
	INNER JOIN [participant].[Participant] p ON	p.humanId = h.id
	
	LEFT JOIN [participant].[CaseManager] ON p.caseManagerId = [participant].[CaseManager].id
	
	LEFT JOIN [staff].[Employee] ON [participant].[CaseManager].EmployeeId = [staff].[Employee].id
	
	LEFT JOIN [humans].[Human] cmh ON [staff].[Employee].humanId = cmh.id

	LEFT JOIN [humans].[SSNQuality] hs ON h.ssnQualityId = hs.id
	
	LEFT JOIN [humans].[DobQuality] hdob ON h.dobQualityId = hdob.id
	
	LEFT JOIN [humans].[Gender] hg ON h.genderId = hg.id

	LEFT JOIN [humans].[Race] hr ON h.raceId = hr.id
	
	LEFT JOIN [humans].[Ethnicity] he ON h.ethnicityId = he.id

	LEFT JOIN [humans].[VeteranStatus] hv ON h.veteranStatusId = hv.id

	LEFT JOIN [humans].[DisabilityType] hd ON h.disabilityTypeId = hd.id

	LEFT JOIN [humans].[Family] hf ON h.familyId = hf.id
	
	LEFT JOIN [humans].[HohRelationship] hh ON h.hohRelationshipId = hh.id
	
	LEFT JOIN [humans].[CommunicationType] hc ON h.communicationTypeId = hc.id

WHERE
	p.id = :participant_id