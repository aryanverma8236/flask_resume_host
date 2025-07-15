from flask import Flask, request, render_template_string, send_from_directory
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # ✅ Create folder if it doesn't exist

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['htmlfile']
        if file:
            file_path = os.path.join(UPLOAD_FOLDER, "profile.html")
            file.save(file_path)
            return "<p>Uploaded! <a href='/view'>View Profile</a></p>"
    return '''
        <!DOCTYPE html>
        <html>
        <head><title>Upload Profile</title></head>
        <body>
        <h2>Upload Your Profile HTML</h2>
        <form method="post" enctype="multipart/form-data">
            <input type="file" name="htmlfile" accept=".html" required>
            <button type="submit">Upload & Host</button>
        </form>
        </body>
        </html>
    '''

@app.route('/view')
def view_profile():
    return send_from_directory(UPLOAD_FOLDER, "profile.html")

if __name__ == '__main__':
    app.run(debug=True)
