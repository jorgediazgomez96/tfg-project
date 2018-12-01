# tfg-project
This is the repo for the TFG made at University Carlos III of Madrid.

How to correctly set up the project:

The clients side of the application was runned in WIndows 10 using Jupyter notebook.
The server side of the aplication was runned in a raspberian VM with Python installed.
First clone the repository in two OS, one with Linux program (server.py and directorios) and the other (clients) in windows 10 incorporated with Jupyter notebook. 

git clone https://github.com/jorgediazgomez96/tfg-project

WHAT TO DO IN SERVER SIDE

Go to the following direction: ./tfg-project and start the server
python server.py 
On the screen you must see a message like "Server is running at the following direction "http://IPaddress:port" and will also displayed 
a code which is not interesting for this propourse.

WHAT TO DO IN CLIENT SIDE
Here you need open first your Jupyter notebook. If you system doesn´t have it, check how to install Jupyter notebook on you computer.
Another important thing is to make sure your system has the required libraries installed in order to make the project run without errors

WHAT IF YOU WANT TO TRY ONLINE

Well recently I created a domain in heliohost.org 
They provided free domains to run small projects like mine.

So if you want to change from local to online, you just follow the following steps:
1-Open clients/newInteractiveTable.ipynb on your jupyternotebook.
2-Modify the variable Piserver to http://filesystem.heliohost.org/flask
3-Create a new variable, for example serviceServer and type the following address:
http://filesystem.heliohost.org/flask/services
4-Put the created variable at the line where you see: 
pd.read_csv( ) so the new sentence would be pd.read_csv(serviceSerer)
5-Execute normaly and if nothing strange happens it would work perfectly.

NEW CONTENT WOULD COME SOON!!!
