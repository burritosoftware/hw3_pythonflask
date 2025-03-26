from flask_login import LoginManager
import app

login_manager = LoginManager()

login_manager.init_app(app.myapp_obj)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return app.models.User.query.get({"id": user_id})

app.myapp_obj.run(debug=True)


