from django.shortcuts import render
import subprocess
import os

# Create your views here.
def index(req):
    return render(req, 'webapp/index.html')

def run_script(req):
    script_path = os.path.join(os.path.dirname(__file__), "run.sh")
    result = subprocess.run(["bash", script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output = result.stdout
    error = result.stderr

    return render(req, 'webapp/index.html', context={ 'output': output, 'error': error })