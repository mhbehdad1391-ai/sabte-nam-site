
from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Registration Website</title>
<style>
body {
    font-family: sans-serif;
    background: linear-gradient(135deg, #101b40, #3457a5);
    margin: 0;
    padding: 30px 15px;
}
.box {
    max-width: 430px;
    margin: 30px auto;
    background: white;
    padding: 25px;
    border-radius: 22px;
}
h1 {
    text-align: center;
    color: #20366d;
}
label {
    display: block;
    margin-top: 18px;
    font-weight: bold;
}
input {
    width: 100%;
    box-sizing: border-box;
    padding: 13px;
    margin-top: 8px;
    border: 1px solid #ccd3e0;
    border-radius: 10px;
    font-size: 16px;
}
button {
    width: 100%;
    margin-top: 22px;
    padding: 14px;
    background: #315ee7;
    color: white;
    border: 0;
    border-radius: 10px;
    font-size: 17px;
}
</style>
</head>
<body>
<div class="box">
<h1>Registration Form</h1>
<p>Welcome to our website!</p>
<form method="POST">
<label>Name</label>
<input name="name" required>
<label>Age</label>
<input name="age" type="number" min="1" max="120" required>
<label>Interest</label>
<input name="interest" required>
<button type="submit">Register</button>
</form>
{% if message %}
<p>{{ message }}</p>
{% endif %}
</div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def register():
    message = ""
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        message = f"Registration successful: {name}"
    return render_template_string(HTML, message=message)

if __name__ == "__main__":
    app.run()
