from flask import Flask, render_template_string, request

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html>
<head>
  <title>Demo Login</title>
  <style>
    body { font-family: Arial; background:#fafafa; display:flex; justify-content:center; margin-top:50px;}
    .box { background:white; border:1px solid #dbdbdb; padding:20px; width:300px; text-align:center;}
    input { width:100%; padding:10px; margin:5px 0; border:1px solid #dbdbdb; border-radius:5px;}
    button { background:#0095f6; color:white; padding:10px; width:100%; border:none; border-radius:5px;}
  </style>
</head>
<body>
  <div class="box">
    <h2>Demo Login Page</h2>
    <form method="post">
      <input name="username" placeholder="Username" required><br>
      <input name="password" type="password" placeholder="Password" required><br>
      <button type="submit">Log In</button>
    </form>
  </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        return f"<h3>Demo only!</h3><p>You typed: {username} / {password}</p>"
    return render_template_string(html)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)