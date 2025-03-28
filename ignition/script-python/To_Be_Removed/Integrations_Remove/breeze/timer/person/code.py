import traceback
def getTagInfo():
	res= Integrations.breeze.api.GETTER.tags(method="list")
	resDict =  {row["name"]:row["id"] for row in res["Data"]}
	system.tag.writeBlocking(["[default]RITI/Volunteers/Breeze/Tags"], [system.util.jsonEncode(resDict)])

def getFieldInfo():
	res = Integrations.breeze.api.GETTER.profile()
	resDict= {}
	for i, section in enumerate(res["Data"]):
		for field in res["Data"][i].get("fields", []):
#			print field.get("name")
			resDict[field.get("name")] = field
	system.tag.writeBlocking(["[default]RITI/Volunteers/Breeze/ProfileFields"], [system.util.jsonEncode(resDict)])
	
def getTagFolders():
	res= Integrations.breeze.api.GETTER.tags(method="ListFolders")
	resDict =  {row["name"]:row["id"] for row in res["Data"]}
	system.tag.writeBlocking(["[default]RITI/Volunteers/Breeze/TagFolders"], [system.util.jsonEncode(resDict)])

# Add the "Has Volunteered" tag to all participating volunteers 
def UpdateAllHasVolunteered():
	tagId = Integrations.breeze.helper.getTagID("Has Volunteered")
	for v in Integrations.breeze.helper.getParticipatedVolunteers():
		Integrations.breeze.helper.applyTagChanges("add", v, tagId)
	
def getVolunteers(tagNames=["Volunteer"]):
	try:
		LOGGER = system.util.getLogger("Integration.breeze.timer.getVolunteers")
		
		tagIDs = [Integrations.breeze.helper.getTagID(name) for name in tagNames]
		
		volunteers = Integrations.breeze.api.GETTER.people(method="list", params={"filters":{"tags":tagIDs}, "details":0}).get("Data",[])	
		LOGGER.info(str(len(volunteers)) + " volunteers found.")
		paths = ["[default]RITI/Volunteers/Breeze/progressTotal"]
		values = [len(volunteers)]
		system.tag.writeAsync(paths, values)
		#curDate = system.date.now()
		curDate = system.date.format(system.date.now(),'YYYY-MM-dd hh:mm:ss')
		progress = 0
		for volunteer in volunteers:
			progress += 1
			paths = ["[default]RITI/Volunteers/Breeze/progressCount"]
			values = [progress]
			system.tag.writeAsync(paths, values)
			volunteerFirstName = volunteer["first_name"]
			volunteerLastName = volunteer["last_name"]
			breezeID = volunteer["id"]
			pyDS = Integrations.breeze.helper.getHumanByName(volunteerFirstName,volunteerLastName)

			found = False
			if len(pyDS) > 0: # we found potential matches
				# first let's try to determine they already are marked in the volunteer table
				for human in pyDS:
					if breezeID == human["volunteerIdentifier"]:
						found = True
						break
	
			# this person already exists as a human and staff, move onto the next
			if found:
				#break
				#Continue, dont break
				continue
	
			# if we didn't find them by breeze let's compare the DOB on file
			if not found:
				LOGGER.info("No matching Discovery App human for %s, %s, Breeze ID %s"%(volunteerLastName, volunteerFirstName, breezeID))
				volunteerDetail = Integrations.breeze.api.GETTER.people(method="single", params= {"details":1, "person_id":volunteer["id"]})["Data"]
	#			print volunteerDetail
				dob = volunteerDetail.get("details",{}).get("birthdate",None)
				email = volunteerDetail.get("details",{}).get("993865434",[{}])[0].get("address", None)
				street = volunteerDetail.get("street_address")
				city = volunteerDetail.get("city")
				state = volunteerDetail.get("state")
				zipCodeString = volunteerDetail.get("zip")
				try:
					zip = int(zipCodeString[0:5])
				except:
					zip = 12345
				
	#			print dob, email, street,city,state, zip
				
				pyDSDetail = Integrations.breeze.helper.getHumanByName(volunteerFirstName,volunteerLastName, dob=dob, email=email)
				
				
				insHuman = """Insert into humans.Human (firstname,middlename, lastname, dob, street, city, state, zipCode, email, timeCreated, breezeId,
														veteranStatusId, SSN, ssnQualityId, genderId, ethnicityId, raceId, dobQualityId) 
								values (?,?,?,?,?,?,?,?,?, ?,?,
								0, '123456789',6, 5, 4, 8, 6)"""
				insVolunteer = "Insert into staff.Volunteer (humanId,volunteerIdentifier, timeCreated, status) values (?,?,?, 'Active')"
				
				
				
				# good only one entry found, just add to staff.volunteer
				if len(pyDSDetail) == 1:
					LOGGER.info("Human already exists. Updating human.humans and staff.volunteer")
					# Try and update staff with breezeID otherwise make a new entry
					#Py Data Set indices must be integers??
					humanID = pyDSDetail[0]["humanID"]
					system.db.runPrepUpdate("Update humans.human set breezeId =? where id = ?", [breezeID, humanID])
					if system.db.runPrepUpdate("UPDATE staff.Volunteer set volunteerIdentifier=? where humanId = ?", [breezeID, humanID]) == 0:
						LOGGER.info("Updated failed, Inserting new volunteer")
						system.db.runPrepUpdate(insVolunteer, [humanID, breezeID, curDate])
						
					
				# we found more than one entry, we'll make a new human and staff
				# # or Human isn't found, so new human + new volunteer
				elif len(pyDSDetail) > 1 or len(pyDSDetail) == 0:
					humanID = system.db.runPrepUpdate(insHuman, [volunteerFirstName, volunteer.get("middle_name"),volunteerLastName, dob, street, city, state, zip, email, curDate, breezeID], getKey = 1)
					LOGGER.trace("New human created, ID: %s"%humanID)
					system.db.runPrepUpdate(insVolunteer, [humanID, breezeID, curDate])
	
	except:				
		msg = traceback.format_exc()
		LOGGER.error(msg)
