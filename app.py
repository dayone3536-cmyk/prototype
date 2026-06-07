from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    # Flask looks inside the "templates" folder automatically
    return render_template('index.html')

@app.route('/submit-email', methods=['POST'])
def submit_email():
    data = request.get_json()
    email = data.get('email')
    
    if email:
        # 'a' means "append" - it adds the email to the end of the file without deleting old ones
        with open('emails.txt', 'a') as file:
            file.write(f"{email}\n")
            
        print(f"📦 SAVED TO FILE! Email stored permanently: {email}")
        return jsonify({"status": "success", "message": "You are on the list!"})
    
    return jsonify({"status": "error", "message": "Invalid email"}), 400

if __name__ == '__main__':
    app.run(debug=True)