def getTagID(tagName):
	tagValue =system.tag.readBlocking(["[default]RITI/Volunteers/Breeze/Tags"])[0].value
	
	return system.util.jsonDecode(tagValue).get(tagName,None)

def getTagFolderID(name):
	tagValue =system.tag.readBlocking(["[default]RITI/Volunteers/Breeze/TagFolders"])[0].value	
	return system.util.jsonDecode(tagValue).get(name,None)

def findOptionValue(valueToFind,options):
	for o in options:
		if o["name"] == valueToFind:
			return o["id"]
		else:
			return None

# this will help with building the construct used for updatePerson and addPerson
# fieldKV is a dictionary of properties: {"Gender":"Male", "Address":{"city":"Folsom", "state":}}
def constructPersonField(fieldKV):
	fieldsDict = system.util.jsonDecode(system.tag.readBlocking(["[default]RITI/Volunteers/Breeze/ProfileFields"])[0].value)
	fieldObj = []
	for k,v in fieldKV.iteritems():
		fieldConfig = fieldsDict.get(k)
		fieldEntry = {}
		
		if fieldConfig is None:
			break
			
		if fieldConfig.get("field_type") in ["multiple_choice", "radio", "checkbox"]:
			val = findOptionValue(v, fieldConfig.get("options",[]))
			if val is not None:
				fieldEntry = {"field_id":fieldConfig.get("field_id"), "field_type":fieldConfig.get("field_type"), "response":val}
			else:
				break
			
		# Unsupported fields
		elif fieldConfig.get(k) in ["family_role"]:
			break		
		# complex types
		elif k in ["Address", "Email", "Phone"]:
			fieldEntry = {"field_id":fieldConfig.get("field_id"), "field_type":fieldConfig.get("field_type"), "response":"true", "details":v}
		elif fieldConfig.get("field_type") is not None:
			fieldEntry = {"field_id":fieldConfig.get("field_id"), "field_type":fieldConfig.get("field_type"), "response":v}
		
		fieldObj.append(fieldEntry)
	
	return fieldObj

# Helper function for front end to add a human and tag them
def addHumanToBreeze(humanID, tags = []):
	breezeID = createBreezePerson(humanID)
	if breezeID > 0:
		for tag in tags:
			tagID = getTagID(tag)
			if tagID is not None:
				applyTagChanges("add", breezeID, tagID)
	

# Query DB for all volunteers that have participated in an event
def getParticipatedVolunteers():
	return [v["id"] for v in system.db.runQuery("select distinct h.breezeId id from humans.human h JOIN staff.volunteer v on v.humanid = h.id JOIN calendar.EventAttendance ea on ea.humanid = h.id")]
	
def isVolunteer(breezeId):
	return True if len(system.db.runPrepQuery("select h.id from humans.human h JOIN staff.volunteer v on v.humanid = h.id where h.BreezeId = ?", [breezeId]))>0 else False
	

# Pass in the humans.human.id and we'll retrieve from DB and push the person to Breeze	
def createBreezePerson(humanId):
	query = """select firstname, lastname, dob, phone, email, street, city, state, zipcode from humans.human where id = ? """
	ds = system.db.runPrepQuery(query, [humanId])
	if len(ds) == 1:
		row = ds[0]
		firstName = row["firstname"]
		lastName = row["lastname"]
		xProp = {}
		xProp["Age"] = row["dob"] 
		xProp["Phone"]= {"phone_mobile":row["phone"]}
		xProp["Email"] = {"address":row["email"]}
		xProp["Address"] = {"street_address":row["street"], "city":row["city"], "state":row["state"], "zip":row["zipcode"]}
		
		urlProps = constructPersonField(xProp)
#		print "urlProps", urlProps
		_addRes = Integrations.breeze.api.SETTER.addPerson(firstName, lastName, urlProps)
#		print "result",  _addRes
		newBreezeID = _addRes["Data"]["id"] 
		# log this new ID to humans.human
		system.db.runPrepUpdate("Update humans.human set breezeId = ? where id = ?", [newBreezeID, humanId])
		return newBreezeID
	else:
		return -1

# One stop add/remove tags from a breeze person
def applyTagChanges(action, breezeID, tagID):
	if action == "remove":
		Integrations.breeze.api.SETTER.unassignTag(breezeID, tagID)
	elif action == "add":
		Integrations.breeze.api.SETTER.assignTag(breezeID, tagID)



# Pass in first name, last name, dob, or other fields to see if we can match up a volunteer
def getHumanByName(firstname,lastname, **kwargs):

	if kwargs == {}:
		query = """SELECT h.id humanID, h.firstname, h.lastname, h.dob, v.id volunteerID, v.volunteerIdentifier
			 			FROM humans.Human h LEFT JOIN  staff.Volunteer v on h.id = v.humanId
			 			WHERE h.firstname=? and h.lastname = ? """
		return system.db.runPrepQuery(query, [firstname,lastname])
	# if kwargs isn't empty, we'll dynamically build our query based on available data fields.
	else:
		query = """SELECT h.id humanID, h.firstname, h.lastname, h.dob, v.id volunteerID, v.volunteerIdentifier
		 			FROM humans.Human h LEFT JOIN  staff.Volunteer v on h.id = v.humanId
		 			WHERE h.firstname=? and h.lastname = ? %s """
		args = [firstname,lastname]
		strArg = ""
		for k,v in kwargs.iteritems():
			strArg+= " and %s= ? "%k
			args.append(v)
		return system.db.runPrepQuery(query%strArg, args)	

# all in one, if foldername doesn't exist, we'll create it in the All Tags root directory
# Ex Call: Integrations.breeze.helper.addNewTag("All Tags", "Dummy1")
def addNewTag(folderName, tagName):
	folderID = getTagFolderID(folderName)
	if folderID is None:
		root = getTagFolderID("All Tags")
		resp = Integrations.breeze.api.SETTER.createNewTagFolder(folderName, root)["Data"]
		Integrations.breeze.timer.person.getTagFolders()
		folderID = resp[0].get("id", None)
	
	Integrations.breeze.api.SETTER.createNewTag(tagName, folderID)
	
	
	
