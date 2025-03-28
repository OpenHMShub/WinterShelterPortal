UPDATE	participant.CaseNotes
SET participantId = :participant_id,
	employeeId = :employee_id, 
	Note = :note,
	CaseNoteTypeID = :note_type_id, 
	HMIS = :hmis, 
    userName = :user_name 
WHERE id = :row_id;
