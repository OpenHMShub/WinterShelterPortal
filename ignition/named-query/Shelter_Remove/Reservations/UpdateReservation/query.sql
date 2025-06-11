Update lodging.Reservation 
Set bedId = :bedId , participantId = :participantId, reservationStart = :reservationStart, reservationEnd = :reservationEnd, timeCreated = current_timestamp, notes = :notes, providerTypeId = :providerTypeId, providerId = :providerId, programId = :programId, waitingListName = :waitingListName, reservationType = :reservationType
Where id = :reservationID