
INSERT INTO lodging.Reservation (bedId, participantId, reservationStart, reservationEnd, timeCreated, notes, providerTypeId, providerId, programId, waitingListName, reservationType, referralStatus)
VALUES ( :bedId, :participantId, :reservationStart, :reservationEnd, current_timestamp, :notes, :providerTypeId, :providerId, :programId, :waitingListName, :reservationType, :referralStatus)

-- Delete from waiting List if Participant exists in any of the waiting lists
UPDATE shelter.WaitList 
SET dateremoved = current_timestamp
WHERE participantid = :participantId

-- also update the referral status
IF NOT EXISTS(SELECT id from participant.referral where participantId = :participantId and programId = :programId and providerId = :providerId)
BEGIN
	INSERT INTO participant.referral (participantId, programId, ProviderId, Status_Id, Type_Id, timeCreated)
	VALUES (:participantId, :programId, :providerId, 5, 2, current_timestamp)
END
ELSE
BEGIN
	UPDATE participant.referral
	SET Status_Id = 5 
	where participantId = :participantId and programId = :programId and providerId = :providerId
END
-- Get the new reservation Id
SELECT id 
from lodging.Reservation
where bedId = :bedId and participantId = :participantId and reservationStart = :reservationStart and reservationEnd=  :reservationEnd
and notes = :notes