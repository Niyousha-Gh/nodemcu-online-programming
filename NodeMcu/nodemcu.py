
import os
import subprocess
import shutil

# Directories
# The .ino file path 
project_path = 'Downloads/NodeMcu'

# The espota file path
espota_path = 'Downloads/NodeMcu'

# The arduino-cli path 
arduino_cli_path = 'Downloads/NodeMcu'

# The online connection file path
connectionfile_path = 'Downloads/NodeMcu/online_connection.txt'


def get_ip() -> str:
	""" Get ip address of NodeMcu """

	result, error_code = run_cmd('ipconfig')	
	result = (result.decode('UTF-8').replace('\n', ''))
	result = result.translate({ord(i): None for i in '\r'})
	isOk, error_massage = check_connection_process(result)

	if isOk:
		# Get out the ip address from the command
		start = 'Default Gateway . . . . . . . . . : '
		end = 'Ethernet adapter'
		ip_address = result[result.find(start)+len(start):result.rfind(end)]
		return ip_address
	else:
		print(error_massage)
		return None

	
def check_connection_process(result: str) -> (bool, str):
	""" Look for errors while getting the IP """

	if 'Default Gateway' in result:
		# Pc is connected to an Ap
		return True, None
	else:
		# There was an error while getting the ip
		massage = '\nCheck if you are connected to ESP8266 Access Point\n'
		return False, massage

	
def compile_code() -> bool:
	""" Compile the code and get the projects output files (bin,elf,map) """

	# Add the online connection code to the users code
	add_connection_code()

	# Change the python directory to where espota is located
	os.chdir(arduino_cli_path)

	result, error_code = run_cmd('arduino-cli compile --fqbn esp8266:esp8266:nodemcuv2' + ' "' +
					 project_path + '/project" --output-dir "' + project_path + '/project"')

	isOk, massage = check_compile_process(error_code, result)

	if isOk:
		print('\nCode was compiled successfully\n')
		print(massage)
		return True
	else:
		print('\nThere was an error while compiling\n')
		print(massage)
		return False

	
def check_compile_process(error_code: str, result: str) -> (bool, str):
	""" Check if the runned process has any errors """

	error_code = (error_code.decode('UTF-8').replace('\n', ''))
	result = (result.decode('UTF-8').replace('\n', ''))

	if (not result == '' and
		result.find('Error')== -1 and
		result.find('error')== -1):
		
		if not error_code == '':
			error_code = error_code.translate({ord(i): None for i in '\r'})
			massage = result + '\n\n' + error_code
			return True, massage
		else:
			return True, result
	else:
		return False, error_code

	
def upload_code(ip_address: str) -> bool:
	""" Upload the code and decides about the output files """

	if compile_code():
		# Change the python directory to where the espota is located
		os.chdir(espota_path)

		result, error_code = run_cmd('python espota.py -d -i ' + ip_address +
					 	' -f "' + project_path + '/project/project.ino.bin"')		

		isOk, error_massage = check_upload_process(error_code)
		
		if isOk:
			print('\nSuccessfully uploaded\n')
			delete_files()
			return True
		else:
			print('\nThere was an error while uploading\n')
			print(error_massage)
			delete_files()
			return False

		
def check_upload_process(error_code: str) -> (bool, str):
	""" Check if the uploade process has any errors """

	error_code = (error_code.decode('UTF-8').replace('\n', ''))
	
	if (('Result: OK' in error_code) and
		error_code.find('ERROR')== -1 and
		error_code.find('No Answer')== -1):

		return True, None
	else:
		# There was an error while uploading
		error_code = error_code.translate({ord(i): None for i in '\r'})
		massage = error_code + '\n\n' + 'Check your network and power connection of your wi-fi module and PC'
		return False, massage

	
def add_connection_code():
	""" 
	Add the OTA and Access Point functions to the 
	users code from online_connection.txt file
	"""

	# Make a new folder for the .ino file with the same name
	move_file()

	# Read the online_connection.txt 
	with open(connectionfile_path, 'r') as in_file:
		connection_buf = in_file.readlines()	

	# Read the users code file
	with open(project_path + '/project/project.ino', 'r') as in_file:
		buf = in_file.readlines()	

	# Add connection lines to the users code
	with open(project_path + '/project/project.ino', 'w') as out_file:
		out_file.write(connection_buf[0])
		out_file.write(connection_buf[1])
		out_file.write(connection_buf[3])
		out_file.write(connection_buf[4])
		
		for i in range(len(buf)):
		
			out_file.write(buf[i])
	
			if ('{' in buf[i]) and ('void setup()' in buf[i-1]):
				out_file.write(connection_buf[8])
				out_file.write(connection_buf[10] + '\n')

			if ('{' in buf[i]) and ('void loop()' in buf[i-1]):	
				out_file.write(connection_buf[16] + '\n')

		out_file.write('\n')

		for j in range(21, 79):
			out_file.write(connection_buf[j])
			
			
def delete_files():
	""" Delete the project folder (project.ino and output files) after uploading """

	try:
		shutil.rmtree(project_path + '/project')
	except OSError as e:
    		print('Error: %s : %s' % (project_path, e.strerror))


def move_file():
	""" 
	Creates a folder with the same name as the .ino file 
	and tranfer the .ino file to it.
	"""
	path = os.path.join(project_path, 'project')

	try:  
    		os.mkdir(path)  
	except OSError as error:  
    		print(error)

	# Move the .ino file in it
	source_path = project_path + '/project.ino'
	des_path = project_path + '/project/project.ino'
	shutil.move(source_path, des_path)


def run_cmd(win_cmd: str) -> str:
	""" Run the commands """

	process = subprocess.Popen(win_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	result, error_code = process.communicate()
	return result, error_code


def main():
	
	ip_address = get_ip()

	# If an AP connection was found
	if ip_address is not None:
		upload_code(ip_address)


if __name__ == '__main__':
    main()
