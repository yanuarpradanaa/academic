{
	"name": "Academic Module",
	"version": "1.0", 
	"depends": [
		"base",
		"account",
		"sale",
	],
	"author": "Yanuar", 
	"category": "Education", 
	'website': '',
	"description": """\
Academic Module

""",
	"data": [
		"views/menu.xml",
		"views/course.xml",
		"views/session.xml",
		"views/attendee.xml",
		"views/partner.xml",
		"views/workflow.xml",
		"security/groups.xml",
		"security/ir.model.access.csv",
		"wizard/create_attendee_view.xml",
		"report/session.xml",
	],
	"installable": True,
	"auto_install": False,
    "application": True,
}
