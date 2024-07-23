from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity,unset_jwt_cookies
from werkzeug.security import generate_password_hash, check_password_hash
from application.database import db
import os
import subprocess

run_blueprint=Blueprint("run",__name__)

# Directory to store C++ files
cpp_files_dir = os.path.join(os.getcwd(), 'cpp_files')
os.makedirs(cpp_files_dir, exist_ok=True)

@run_blueprint.route('/runCPP', methods=['POST'])
def runCPP():
    data = request.get_json()
    code = data.get("code")
    cpp_filename = os.path.join(cpp_files_dir, 'user_code.cpp')

    # Write the received code to the file
    with open(cpp_filename, 'w') as f:
        f.write(code)

    # Compile the C++ code using cmd.exe to ensure it's in a Windows environment
    compile_command = f'g++ "{cpp_filename}" -o "{cpp_filename[:-4]}.exe"'
    compile_process = subprocess.Popen(compile_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    compile_output, compile_error = compile_process.communicate()

    if compile_process.returncode != 0:
        # Compilation failed
        return jsonify({
            'msg': 'Compilation error',
            'output': compile_output.decode('utf-8'),
            'error': compile_error.decode('utf-8')
        }), 202

    # Run the compiled executable using cmd.exe
    compiled_exe_path = os.path.join(cpp_files_dir, 'user_code.exe')
    run_command = f'cmd.exe /C "{compiled_exe_path}"'
    run_process = subprocess.Popen(run_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    run_output, run_error = run_process.communicate()

    if run_process.returncode != 0:
        # Execution failed
        return jsonify({
            'msg': 'Runtime error',
            'output': run_output.decode('utf-8'),
            'error': run_error.decode('utf-8')
        }), 201

    # Return the output of the executed code
    return jsonify({
        'msg': 'Compiled and Executed Properly',
        'output': run_output.decode('utf-8')
    }), 200
    
    


