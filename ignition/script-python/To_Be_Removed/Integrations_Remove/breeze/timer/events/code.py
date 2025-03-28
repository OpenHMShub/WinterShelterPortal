def syncCalendars():
	_res = Integrations.breeze.api.GETTER.calendars()["Data"]
	calendarIDs = [c["BreezeId"] for c in system.db.runQuery("select BreezeId, name from calendar.calendars")]
	insQuery = "INSERT into calendar.calendars (BreezeId, name) values "
	insValues = []
	for bCal in _res:
		if bCal["id"] not in calendarIDs:
			insQuery += "(?,?),"
			insValues.extend([bCal["id"], bCal["name"]])
	
	if len(insValues) > 0:
		system.db.runPrepUpdate(insQuery[:-1], insValues)
	

def syncEvents(startDate, endDate):
	_res = Integrations.breeze.api.GETTER.events(params= {"startDate":startDate, "endDate":endDate})["Data"]

	breezeEvents = []
	insQuery = "INSERT into calendar.CalendarEvents (calendarId, breezeId, name, startDate, endDate) values "
	insValues = []
	for calEvent in _res:
		# CHECK IF THE EVENT HAS ALREADY BEEN CREATED BEFORE ADDING
		if system.db.runScalarPrepQuery("select id from calendar.CalendarEvents where breezeId = ?", [calEvent["id"]]) is None:
			insQuery += "((select id from calendar.calendars where breezeId = ?),?,?,?,?),"
			insValues.extend([calEvent["category_id"],calEvent["id"],calEvent["name"], calEvent["start_datetime"], calEvent["end_datetime"]])
		
		breezeEvents.append(calEvent["id"])
		
		
	if len(insValues) > 0:
		system.db.runPrepUpdate(insQuery[:-1], insValues)
	return breezeEvents	


def isEventAttendeeExist(eventBreezeID, personBreezeID):
	query = """SELECT ea.id
				  FROM calendar.EventAttendance ea
				  JOIN calendar.CalendarEvents ce on ce.id = ea.eventId
				  JOIN humans.human h on h.id = ea.humanid
				where h.breezeId = ? and ce.breezeId = ?"""
	return len(system.db.runPrepQuery(query, [personBreezeID, eventBreezeID]))

def getEventAttendees(eventBreezeId, isYesterday):
	_res = Integrations.breeze.api.GETTER.attendance(method= "list", params= {"eventid":eventBreezeId, "details":0, "type":"person"})["Data"]
	note = None

	system.db.runPrepUpdate("DELETE from calendar.eventAttendance where eventId = (select id from calendar.CalendarEvents where breezeId = ?)", [eventBreezeId])
	
	insQuery = "INSERT into calendar.eventAttendance (eventId, humanId, checkin, checkout, autonote) values "
	insValues = []
	
	hasVolunteeredTagId = Integrations.breeze.helper.getTagID("Has Volunteered")
	
	for attendee in _res:
		note = None
		insQuery += """((select id from calendar.CalendarEvents where breezeId = ?),
						(select id from humans.human where breezeId = ?),?,?,?),"""
		# do some logic for the checkout time
		checkOutTime = attendee["check_out"]
		isAttendeeVolunteer= Integrations.breeze.helper.isVolunteer(attendee["person_id"])	
		
		if isEventAttendeeExist(eventBreezeId, attendee["person_id"]) == 0: # The event and human combination does not exist 
			# If checkout time wasn't provided
			if (isAttendeeVolunteer and isYesterday) :
				if checkOutTime == "0000-00-00 00:00:00":
					# we'll use the event's end time if it's less than 8 hours
					eventData = system.db.runPrepQuery("select startDate,endDate from calendar.CalendarEvents where breezeId = ?", [eventBreezeId])
					eventDur = system.date.hoursBetween(eventData[0]["startDate"], eventData[0]["endDate"])
					
					if eventDur > 8.0:
						checkOutTime = system.date.addHours(system.date.parse(attendee["created_on"], "yyyy-MM-dd HH:mm:ss"), 8)
						note = "Missing Checkout, Auto-capped at 8 hours for event greater than 8 hours"
					else:
						checkOutTime = eventData[0]["endDate"]
						note = "Missing Checkout, using event endtime for checkout"
				
			if not isAttendeeVolunteer or (isAttendeeVolunteer and isYesterday):
				insValues.extend([eventBreezeId, attendee["person_id"], attendee["created_on"], checkOutTime, note])
			
		# while we're doing this let's add the "Has Volunteered" tag if the person is a volunteer
		if isAttendeeVolunteer:
			Integrations.breeze.helper.applyTagChanges("add", attendee["person_id"], hasVolunteeredTagId)
	
	if len(insValues) > 0:
		system.db.runPrepUpdate(insQuery[:-1], insValues)
#		print "****", insQuery, insValues				


def syncEventAttendance(eventDate):
	fEventDate = system.date.format(eventDate, "yyyy-MM-dd")
	events = syncEvents(fEventDate,fEventDate)
	for eventId in events:
		getEventAttendees(eventId, system.date.getDayOfMonth(eventDate) != system.date.getDayOfMonth(system.date.now()))
	
	
