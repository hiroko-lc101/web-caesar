from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG']=True

form = """
<!doctype html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
            .error {{
                color: red;
            }}
        </style>
    </head>
    <body>
        <!-- create your form here -->
        <form method="post">
            <label>Rotate by:
                <input type="text" name="rot" value="0" />
            </label>
            <p class="error">{r_value}</p>
            <textarea name="text">{t_value}</textarea>
            <input type="submit" />
        </form>
    </body>
</html>
"""
def is_integer(num):
    try:
        int(num)
        return True
    except ValueError:
        return False   

@app.route("/")
def index():
#    return form
    return form.format(t_value="", r_value="")

@app.route("/", methods=["POST"])
def encrypt():
#    rot_value = int(request.form["rot"])
    rot_value = request.form["rot"]
    text_value = request.form["text"]

    rot_value_error = ""
    if not is_integer(rot_value):
        rot_value_error = "Not a valid integer"
        rot_value = 0
    if not rot_value_error:
        return form.format(t_value=rotate_string(text_value, int(rot_value)), r_value=rot_value_error)
    else:
        return form.format(t_value="", r_value=rot_value_error)        

##    return "<h1>" + rotate_string(text_value, rot_value) + "</h1>"
#    return form.format(rotate_string(text_value, rot_value))
app.run()