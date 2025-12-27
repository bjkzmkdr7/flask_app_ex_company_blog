from company_blog import app
from company_blog import db
from company_blog.models import User

def init_db_if_needed(app):
    with app.app_context():
        db.create_all()

        # 管理ユーザーがいなければ作成
        if not User.query.filter_by(email="admin_user@test.com").first():
            admin = User(
                email="admin_user@test.com",
                username="Admin User",
                password="123",
                administrator="1"
            )
            db.session.add(admin)
            db.session.commit()

if __name__=='__main__':
    app.run()

init_db_if_needed(app)