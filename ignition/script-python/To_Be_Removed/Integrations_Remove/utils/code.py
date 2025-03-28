### standardize output of API calls
### url string used in request
### headers = additional headers
### urlParams is a dictionary of params
def callGet(url, headers, urlParams):
	returnData = {"Success":False, "Data":None}
	startTime = system.date.now()
	client = system.net.httpClient()

	response = client.get(url = url, headers = headers, params = urlParams)
	endTime = system.date.now()
	if response.good:
		returnData["Success"] = True
		returnData["Data"] = response.json
	returnData["StartTime"] = startTime
	returnData["EndTime"] = endTime
	
	return returnData
