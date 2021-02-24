from flask import Flask
from flask import request
from flask_cors import CORS
import os
import subprocess

# users project file path
project_path = "C:/Users/NodeMcu"

app = Flask(__name__)
CORS(app)
@app.route('/', methods=['GET', 'POST'])
def main():
	""" Get the users code from blockly """

	json_content = request.json
	
	if json_content['project']:
		save_code(json_content['project'])
		compile_upload_code()
		
	return json_content


def save_code(script: str):
	""" Save the code content in a .ino file """

	file = open(project_path + '/project.ino','w') 
	file.write(script[0]) 
	file.close() 

	
def compile_upload_code():
	""" Run the upload exe file """

	# Change the python directory to where the exe file is located
	os.chdir(project_path)
	print("\n\nRunning the nodemcu exe file ...\n")
	process = subprocess.Popen('nodemcu', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	
	
if __name__ == '__main__':
	app.run(host= '0.0.0.0',debug=True)
