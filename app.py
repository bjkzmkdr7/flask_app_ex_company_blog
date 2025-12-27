from company_blog import app
import os
from flask_migrate import upgrade

# Render の本番環境でのみ実行
if os.environ.get("RUN_MIGRATIONS") == "true":
    with app.app_context():
        upgrade()

if __name__=='__main__':
    app.run()
    # app.run(debug=True)