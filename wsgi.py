from blog.app import app, db
from blog.models.user import Role

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        debug=True,
    )


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print("done!")


@app.cli.command("create-users")
def create_users():
    from blog.models import User
    admin_role = Role(name='Admin')
    admin = User(username="admin", is_staff=True)
    james = User(username="james")
    newadmin1 = User(username='new_admin', is_staff=True)
    newadmin1.roles = [admin_role, ]
    db.session.add(admin)
    db.session.add(james)
    db.session.add(newadmin1)
    db.session.commit()
    print("done! created users:", admin, james)
