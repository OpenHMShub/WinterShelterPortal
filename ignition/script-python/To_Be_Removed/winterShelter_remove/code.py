import traceback
project = "RITI"

def deleteScheduleDates(locationId,dayOfYearList):
	if len(dayOfYearList) > 0:
		#convert the list into a Query String
		dayOfYearString = "("
		for date in range(0,len(dayOfYearList)):
			dayOfYearString += str(dayOfYearList[date]) + ","
		#Remove the last comma and add paranthesis
		dayOfYearString = dayOfYearString[:-1] + ")"
		system.perspective.print(dayOfYearString)
		path = 'WinterShelter/Registration/deleteLocationScheduleDates'
		parameters = {
					"locationId":locationId,
					"dayOfYearString":dayOfYearString
					}
		result = system.db.runNamedQuery(project=project,path=path,parameters=parameters)
	return 
	
def insertScheduleDates(locationId,dayOfYearToAddList,genderId,totalBeds,noteList):
	path = 'WinterShelter/Registration/insertLocationSchedule'
	for day in range(0,len(dayOfYearToAddList)):
		dayOfYear = dayOfYearToAddList[day]
		notes = noteList[day]
		parameters = {
					"locationId":locationId,
					"dayOfYear":dayOfYear,
					"genderId":genderId,
					"totalBeds":totalBeds,
					"notes":notes
					}
		result = system.db.runNamedQuery(project=project,path=path,parameters=parameters)
	return
	
def updateScheduleDate():
	return
	
#def getCurrentSeasonId():
	#Get the current season ID
#	path = 'WinterShelter/getCurrentSeason'
#	parameters = {}
#	dataset = system.db.runNamedQuery(project=project,path=path,parameters=parameters)
#	currentSeasonId = dataset.getValueAt(0,'id')
#	return currentSeasonId
	
def getLocationCurrentSchedule(locationId,seasonId):
	#Get the current schedule
	path = 'WinterShelter/getCurrentSchedule'
	parameters = {
				"locationId":locationId,
				"seasonId":seasonId
				}
	currentSchedule = system.db.runNamedQuery(project=project,path=path,parameters=parameters)
	#system.perspective.print(str(currentSchedule.getRowCount()))
	return currentSchedule

def editRegistrationSchedule(locationId,newSchedule,genderId,totalBeds):
	#Input is an edited schedule
	#Query the exisiting schedule and make deletions, insertions,
	#and updates as required 
	system.perspective.print("Editing the registration schedule for location ID " + str(locationId))
	# Get the current season
	seasonId = calendar.getCurrentSeasonId()
	system.perspective.print("Current Season ID is " + str(seasonId))
	currentDayOfSeason = calendar.dayOfSeason(system.date.getDayOfYear(system.date.now()))
	system.perspective.print("Current day of season is " + str(currentDayOfSeason))
	#Get the current schedule
	currentSavedSchedule = getLocationCurrentSchedule(locationId,seasonId)
	#convert to array
	oldSchedule = []
	for item in range(0,currentSavedSchedule.getRowCount()):
		oldDate = currentSavedSchedule.getValueAt(item,'dayOfYear')
		oldSchedule.append(oldDate)
	system.perspective.print('Days in old schedule: ' + str(oldSchedule))
	system.perspective.print('Days in new schedule: ' + str(newSchedule))
	#Remove dates that are not on the new schedule
	#Be sure there are no reservations before removing
	dayOfYearToDeleteList = []
	for date in range(0,len(oldSchedule)):
		#Convert dayOfYear to dayOfSeason
		dayOfSeason = calendar.dayOfSeason(oldSchedule[date])
		#system.perspective.print(str(oldSchedule[date]))
		#Only remove dates in the future
		if dayOfSeason >= currentDayOfSeason:
			if oldSchedule[date] not in newSchedule:
				dayOfYearToDeleteList.append(oldSchedule[date])
	#Remove the last comma and close the paranthesis
	if len(dayOfYearToDeleteList) > 0:
		system.perspective.print('Days to remove: ' + str(dayOfYearToDeleteList))
		deleteScheduleDates(locationId,dayOfYearToDeleteList)
	else: 
		system.perspective.print('No dates to remove.')
	#
	#Insert new dates
	newScheduleDateCount = len(newSchedule)
	system.perspective.print(str(newScheduleDateCount) + " nights found in the new schedule.")
	dayOfYearToAddList = []
	noteList = []
	for newDate in range(0,newScheduleDateCount):
		dayOfSeason = calendar.dayOfSeason(newSchedule[newDate])
		dayOfYear = newSchedule[newDate]
		#Only add dates in the future
		if dayOfSeason >= currentDayOfSeason:
			if newSchedule[newDate] not in oldSchedule:
				dayOfYearToAddList.append(newSchedule[newDate])
				noteList.append('')
	if len(dayOfYearToAddList) > 0:
		system.perspective.print('Days to add: ' + str(dayOfYearToAddList))
		insertScheduleDates(locationId,dayOfYearToAddList,genderId,totalBeds,noteList)
	else: 
		system.perspective.print('No dates to add.')
	#
	#Update exisiting dates
	#
	#
	#
	return
