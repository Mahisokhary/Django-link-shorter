import sqlite3

from django.http import HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import render, redirect
from django.forms import Form

connection = sqlite3.connect("links.sqlite3")
cursor= connection.cursor()

cursor.execute("""
create table if not exists links (
	name varchar(255),
	link varchar(255)
)
""")

def index(request: HttpRequest):
	if request.method == "POST":
		#from django.forms import Form
		#form = Form(request.POST)
		return HttpResponse(request.POST)
	try:
		connection = sqlite3.connect("links.sqlite3")
		cursor= connection.cursor()
		data = Form(request.GET).data.dict()
		if "url" in data and "name" in  data:
			if len(cursor.execute(f"""select * from links where name="{data["name"]}" """).fetchall()) != 0:
				return JsonResponse({"eror": "this name was used"})
			cursor.execute(f"""insert into links values ("{data["name"]}", "{data["url"]}")""")
			connection.commit()
			return redirect("/")
		shortlink = []
		for i in cursor.execute("select * from links").fetchall():
			shortlink += [{"name": i[0], "url": i[1]}]
		return render(request,"index.html",{"web_adress": request.get_host(),"short_link": shortlink})
	except Exception as e:
		return JsonResponse({"eror": str(e)})
	
def short_link(request: HttpRequest, name: str):
	try:
		connection = sqlite3.connect("links.sqlite3")
		cursor= connection.cursor()
		return redirect(
			cursor.execute(
				f"""select link from links where name="{name}" """
			).fetchall()[0][0]
		)
	except:
		return JsonResponse({"eror": "404 not found"})
