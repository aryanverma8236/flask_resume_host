import os
from flask import Flask, request, redirect, url_for, render_template, send_from_directory

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Allow only .html uploads
ALLOWED_EXTENSIONS = {'html'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Home: Upload page
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'htmlfile' not in request.files:
            return "No file part"

        file = request.files['htmlfile']

        if file.filename == '':
            return "No file selected"

        if file and allowed_file(file.filename):
            filename = "profile.html"  # Overwrite every time
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            return redirect(url_for('view_uploaded'))

    return render_template('upload.html')

# View hosted HTML
@app.route('/view')
def view_uploaded():
    return send_from_directory(app.config['UPLOAD_FOLDER'], 'profile.html')

if __name__ == '__main__':
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(debug=True)
