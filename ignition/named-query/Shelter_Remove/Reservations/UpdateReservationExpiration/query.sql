UPDATE R
SET R.Status_Id = 10 
FROM participant.referral R
JOIN lodging.Reservation res
ON res.participantId = R.participantId and res.programId = R.programId and res.providerId = R.providerId
and res.timeRetired is null and (res.reservationExpiration is null or res.reservationExpiration = '') and res.reservationEnd < CURRENT_TIMESTAMP

Update lodging.Reservation 
set reservationExpiration = reservationEnd, referralStatus = 'No-Show'
where timeRetired is null and (reservationExpiration is null or reservationExpiration = '') and reservationEnd < CURRENT_TIMESTAMP