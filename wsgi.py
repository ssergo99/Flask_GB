from blog.app import app, db
from blog.models.user import Role
import os

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        debug=True,
    )


@app.cli.command("create-admin")
def create_admin():
    from blog.models import User

    admin = User(username="admin", is_staff=True)
    admin.password = os.environ.get("ADMIN_PASSWORD") or "adminpass"

    db.session.add(admin)
    db.session.commit()

    print("created admin:", admin)


@app.cli.command("create-tags")
def create_tags():
    from blog.models import Tag
    for name in [
        "flask",
        "django",
        "python",
        "sqlalchemy",
        "news",
    ]:
        tag = Tag(name=name)
        db.session.add(tag)
    db.session.commit()
    print("created tags")
