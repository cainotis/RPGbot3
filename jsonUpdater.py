import json

arquivo ='newUser.json'

data = {
	"N": "unknow",
	"GM": False,
	"personagens": 
	{
		"N": 0
	},
	"id" : None
}

file = open(arquivo,'w')
file.write(json.dumps(data))
file.close()
