from app.database import engine
from app.models import Base


def create_database():
    try:
        Base.metadata.create_all(bind=engine)
        print("✅ Database created successfully!")
    except Exception as e:
        print("❌ Error creating database:", str(e))


if __name__ == "__main__":
    create_database()