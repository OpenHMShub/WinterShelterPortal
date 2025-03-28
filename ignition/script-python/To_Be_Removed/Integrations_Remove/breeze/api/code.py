BASE_URL = "https://riti.breezechms.com"
ENDPOINTS={"people":"/api/people",
			"profile":"/api/profile",
			"tags":"/api/tags",
			"volunteers":"/api/volunteers/list",
			"families":"/api/families",
			"events":"/api/events",
			"attendance":"/api/events/attendance",
			"calendars": "/api/events/calendars/list",
			"addtagfolder": "/api/tags/add_tag_folder",
			"addtag": "/api/tags/add_tag"			
		}
AUTH_HEADER={'Api-Key': 'd03aad4cef083b478dd1c545aed06ecf'}		

# Every statioc method will expect a kwarg for function, indicating 
## all functions should support arguments: `method` string]
class GETTER():
	## ex filter: https://riti.breezechms.com/api/people?filter_json={"tag_contains":"y_4152036"} #4152036 was STAFF
	## ex call: Integrations.breeze.api.GETTER.people(method="list", params={"filters":{"tags":["4152034"], <"questionid">:<"valueid">}, "details":1})
	### NOTE: when filter is available, offset and limit are ignored.
	## INPUT params = {"filter":{"tags":[<tagid>,<tagid>}, "limit":100}
	## INPUT method = single (string)
	@staticmethod
	def people(**kwargs):
		url = "%s%s"%(BASE_URL,ENDPOINTS["people"])
		method = kwargs.get("method","")
		urlParams = {}
		paramArg = kwargs.get("params",{})


		if "filters" in paramArg.keys():
			urlParams["filter_json"] = system.util.jsonEncode(formatTagFilter(paramArg["filters"]))
		urlParams["limit"] = paramArg.get("limit",0)
		urlParams["offset"] = paramArg.get("offset",0)
		urlParams["details"] = paramArg.get("detail",0)				
				
		
		if method == "single":
			url += "/%s" % (paramArg.get("person_id"))
			urlParams["details"] = paramArg.get("details",1)
			 	
		return Integrations.utils.callGet(url, AUTH_HEADER, urlParams)
		
	### CALL Integrations.breeze.api.GETTER.profile()
	### retrieves profile data from Breeze
	@staticmethod
	def profile(**kwargs):
		url = "%s%s"%(BASE_URL,ENDPOINTS["profile"])
		method = kwargs.get("method","")
		
		return Integrations.utils.callGet(url, AUTH_HEADER, {})
	
	### CALL Integrations.breeze.api.GETTER.calendars()
	@staticmethod
	def calendars(**kwargs):
		url = "%s%s"%(BASE_URL,ENDPOINTS["calendars"])
		method = kwargs.get("method","")		
		paramArg = kwargs.get("params",{})
		urlParam = {}				

		return Integrations.utils.callGet(url, AUTH_HEADER, {})
		
		
	### CALL Integrations.breeze.api.GETTER.events(params= {"start":<startDate>, "end":<endDate>)
	### retrieves event data from Breeze	
	@staticmethod
	def events(**kwargs):
		url = "%s%s"%(BASE_URL,ENDPOINTS["events"])
		method = kwargs.get("method","")		
		paramArg = kwargs.get("params",{})
		urlParam = {}		
		
		urlParam["start"] = paramArg.get("startDate", None)
		urlParam["end"] = paramArg.get("endDate", None)
		
		return Integrations.utils.callGet(url, AUTH_HEADER, urlParam)

	### CALL Integrations.breeze.api.GETTER.attendance(method= <"list","eligible">, params= {"instance_id":<id>, "details":0, "type":"person")
	### retrieves event data from Breeze	
	@staticmethod
	def attendance(**kwargs):
		url = "%s%s"%(BASE_URL,ENDPOINTS["attendance"])
		method = kwargs.get("method","")
		paramArg = kwargs.get("params",{})
		urlParam = {}
		
		urlParam["instance_id"] = paramArg.get("eventid", None)
		urlParam["details"] = paramArg.get("details", 0)
		urlParam["type"] = paramArg.get("type", "person")
		
		if method == "list":
			url += "/list"
		elif method == "eligible":
			url += "/eligible"
		print "URL",urlParam
		return Integrations.utils.callGet(url, AUTH_HEADER, urlParam)		

	## sample call: Integrations.breeze.wrapperGET.tags(method="list")
	@staticmethod
	def tags(**kwargs):
		url = "%s%s"%(BASE_URL, ENDPOINTS["tags"])
		method = kwargs.get("method","")
		paramArg = kwargs.get("params",[])
		urlParam = []
		if  method == "list" :
			url+= "/list_tags"
		elif method == "ListFolders":
			url+= "/list_folders"
			
		return Integrations.utils.callGet(url, AUTH_HEADER, {})

class SETTER():
	@staticmethod
	# Create a matching user
	def addPerson(firstName, lastName, extraProps = None):
		url = "%s%s/add"%(BASE_URL,ENDPOINTS["people"])
		urlParam = {}
		
		urlParam["first"] = firstName
		urlParam["last"] = lastName
		if extraProps is not None:
			urlParam["fields_json"] = system.util.jsonEncode(extraProps)
		
		return Integrations.utils.callGet(url, AUTH_HEADER, urlParam)
	@staticmethod
	def assignTag(breezeId, tagId):
		url = "%s%s/assign"%(BASE_URL, ENDPOINTS["tags"])
		urlParam = {}
		
		urlParam["person_id"] = breezeId
		urlParam["tag_id"] = tagId
		
		return Integrations.utils.callGet(url, AUTH_HEADER, urlParam)
	
	@staticmethod
	def unassignTag(breezeId, tagId):
		url = "%s%s/unassign"%(BASE_URL, ENDPOINTS["tags"])
		urlParam = {}
		
		urlParam["person_id"] = breezeId
		urlParam["tag_id"] = tagId
		
		return Integrations.utils.callGet(url, AUTH_HEADER, urlParam)	

	@staticmethod
	def createNewTag(tagname,folderID):
		url = "%s%s"%(BASE_URL, ENDPOINTS["addtag"])
		urlParam = {}
		
		urlParam["name"] = tagname
		if folderID is not None:
			urlParam["folder_id"] = folderID
		
		return Integrations.utils.callGet(url, AUTH_HEADER, urlParam)	

	
	@staticmethod
	def createNewTagFolder(folderName, folderID):
		url = "%s%s"%(BASE_URL, ENDPOINTS["addtagfolder"])
		urlParam = {}
		
		urlParam["name"] = tagname
		if folderID is not None:
			urlParam["parent_id"] = folderID
		
		return Integrations.utils.callGet(url, AUTH_HEADER, urlParam)	

def formatTagFilter(filterArgs):
	filterDict = {}
	for k,v in filterArgs.iteritems():
		if k == "tags":
			filterDict["tag_contains"] = "-".join(["y_"+f for f in v])
		else:
			filterDict[k] = v
	return filterDict
