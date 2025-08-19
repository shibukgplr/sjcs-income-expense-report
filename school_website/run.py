from app import create_app, db
from app.models import Admin
from werkzeug.security import generate_password_hash

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Admin': Admin}

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        if not Admin.query.first():
            hashed_password = generate_password_hash('admin', method='pbkdf2:sha256')
            admin = Admin(username='admin', password=hashed_password)
            db.session.add(admin)
            db.session.commit()
    app.run(debug=True)
