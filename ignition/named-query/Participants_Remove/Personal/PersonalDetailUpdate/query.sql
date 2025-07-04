UPDATE	humans.Human 
SET
	fullRegistration = :full_register  ,
	firstName = :first_name  ,
	middleName =  :middle_name ,
	lastName =   :last_name ,
	suffix =   :suffix_name ,
	nickname =   :nick_name , 
	genderId =  :gender_id ,
	SSN =  :ssn ,
	ssnQualityId =  :ssn_quality_id ,
	dob = :dob , 
	dobQualityId =  :dob_quality_id ,
	raceId =  :race_id ,
	ethnicityId =  :ethnicity_id ,
	veteranStatusId = :veteran_id ,
	disabilityTypeId =  :disability_id ,
	timeDeceased =  :time_deceased ,
	trimorbid = :tri_morbid,
	chronicHomeless  = :chronic_homeless ,
	sexOffendRegistry  = :so_registry ,
	mailService  = :mail_service ,
	street =  :street ,
	city =  :city ,
	state =  :state ,
	zipCode =  :zip_code ,
	phone =  :phone ,
	altPhone =  :alt_phone ,
	email =  :email ,
	communicationTypeId =  :communication_type_id ,
	InsuranceTypeID =  :insurance_type_id,
	emergencyContactName =  :emergency_contact_name ,
	emergencyContactPhone =  :emergency_contact_phone ,
	emergencyContactEmail =  :emergency_contact_email ,
	emergencyContactTypeId =  :emergency_contact_type_id ,
	familyId =  :family_id ,
	hohRelationshipId =  :hoh_relationship_id ,
	employer =  :employer ,
	school =  :school ,
	congregation =  :congregation , 
    timeCreated = GetDate()  
WHERE id = :human_id;
