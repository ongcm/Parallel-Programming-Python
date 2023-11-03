# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
import base64
from io import BytesIO
from flask import Flask, render_template, request
import math
import numpy as np
from multiprocessing import Pool
import services.parallel as parallel
import numpy as np

app = Flask(__name__)

@app.route('/', methods =["GET", "POST"])
def main_functionality():
	if request.method == "POST":
		runtimes = []
		num_process = request.form.get("field1")
		num_numbers = request.form.get("field2")
		num_processes = [i for i in range(1, 21)]
		prog = parallel.runProgram(int(num_process), int(num_numbers))
		for process in range(1, 21):
			runtimes.append(parallel.runProgram(int(process), int(num_numbers))[-1])
			print(process)
		
		labels = num_processes
		values = runtimes
		

		return render_template("mainpage.html", value = prog[1], length = len(prog[1]), random_nums = prog[0], random_nums_length = len(prog[0]), labels=labels, values=values, num_process = num_process)
	else:
			return render_template("mainpage.html", value = parallel.output_list, length = len(parallel.output_list), random_nums = parallel.random_numbers, random_nums_length = len(parallel.random_numbers), use_reloader = True)

if __name__ == '__main__':
	app.run()
