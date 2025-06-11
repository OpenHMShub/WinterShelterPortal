INSERT INTO HMSOps.staff.VolunteerEvents
(eventId, volunteerId, timeCreated)
VALUES(:eventId, :volunteerId, GETDATE());
