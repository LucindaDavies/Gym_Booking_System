from flask import Flask, render_template

from controllers.members_controller import members_blueprint
from controllers.instructors_controller import instructors_blueprint

app = Flask(__name__)

app.register_blueprint(members_blueprint)
app.register_blueprint(instructors_blueprint)

@app.route("/")
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()