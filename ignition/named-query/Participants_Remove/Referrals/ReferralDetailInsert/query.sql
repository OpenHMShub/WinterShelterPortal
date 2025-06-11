INSERT INTO [participant].[Referral]
	(
	  ParticipantId,
	  ProviderId,
	  Status_Id,
	  Type_Id,
	  ProgramId,
	  timeCreated 
	 )
VALUES
	(
	 :participant_id,  
	 :provider_id,  
	 :status_id,  
	 :type_id,
	 :program_id,
	 GetDate()
	) 