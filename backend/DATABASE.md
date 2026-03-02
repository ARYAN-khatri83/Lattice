# Database Management Guide

## DBeaver Connection Settings

To connect to your PostgreSQL database using DBeaver:

### Connection Details:
- **Host:** `localhost`
- **Port:** `5432`
- **Database:** `openclaims`
- **Username:** `postgres`
- **Password:** `postgres`

### Steps to Connect:
1. Open DBeaver
2. Click "New Database Connection" (or press Ctrl+Shift+N / Cmd+Shift+N)
3. Select **PostgreSQL**
4. Enter the connection details above
5. Click "Test Connection" to verify
6. Click "Finish" to save

**Note:** Make sure your Docker containers are running (`docker-compose up`) before connecting.

---

## Alembic Migration Guide

Alembic is now set up for managing database schema changes.

### Initial Setup

1. **Rebuild your backend container** to install Alembic:
   ```bash
   docker-compose down
   docker-compose up --build
   ```

### Creating Models

Create your SQLAlchemy models in `backend/app/models/`:

```python
# Example: backend/app/models/user.py
from sqlalchemy import Column, Integer, String, DateTime, func
from app.database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False, index=True)
    username = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
```

Then import it in `backend/app/models/__init__.py`:
```python
from app.models.user import User

__all__ = ["Base", "User"]
```

### Creating Migrations

#### Auto-generate migration from model changes:
```bash
# Enter the backend container
docker exec -it openclaims-backend bash

# Generate migration
alembic revision --autogenerate -m "description of changes"
```

#### Create empty migration (for data migrations or manual changes):
```bash
alembic revision -m "description of changes"
```

### Applying Migrations

#### Upgrade to latest version:
```bash
docker exec -it openclaims-backend alembic upgrade head
```

#### Upgrade to specific revision:
```bash
docker exec -it openclaims-backend alembic upgrade <revision_id>
```

### Rolling Back Migrations

#### Downgrade one version:
```bash
docker exec -it openclaims-backend alembic downgrade -1
```

#### Downgrade to specific revision:
```bash
docker exec -it openclaims-backend alembic downgrade <revision_id>
```

### Checking Migration Status

#### Show current version:
```bash
docker exec -it openclaims-backend alembic current
```

#### Show migration history:
```bash
docker exec -it openclaims-backend alembic history
```

### Example Workflow

1. **Create a new model**:
   ```bash
   # Create backend/app/models/claim.py with your model
   ```

2. **Import it** in `backend/app/models/__init__.py`

3. **Generate migration**:
   ```bash
   docker exec -it openclaims-backend alembic revision --autogenerate -m "add claim model"
   ```

4. **Review the generated migration** in `backend/alembic/versions/`

5. **Apply the migration**:
   ```bash
   docker exec -it openclaims-backend alembic upgrade head
   ```

6. **Verify in DBeaver** that the table was created

### Tips

- **Always review auto-generated migrations** before applying them
- **Use descriptive migration messages** to make history readable
- **Test migrations** on development before production
- **Keep migrations in version control** (the files in `alembic/versions/`)
- **Never edit applied migrations** - create a new one instead

### Common Commands

```bash
# Create migration
docker exec -it openclaims-backend alembic revision --autogenerate -m "message"

# Apply all pending migrations
docker exec -it openclaims-backend alembic upgrade head

# Show current migration state
docker exec -it openclaims-backend alembic current

# Show history
docker exec -it openclaims-backend alembic history --verbose
```

### Directory Structure

```
backend/
├── alembic/
│   ├── versions/          # Migration files (auto-generated)
│   ├── env.py             # Alembic environment configuration
│   └── script.py.mako     # Template for new migrations
├── alembic.ini            # Alembic configuration
├── app/
│   ├── database.py        # Database engine and session
│   └── models/            # SQLAlchemy models
│       ├── __init__.py    # Import all models here
│       └── example.py     # Example model (can delete)
```

### Troubleshooting

**Issue:** "Can't locate revision identified by..."
- **Solution:** Make sure all migration files are present in `alembic/versions/`

**Issue:** "Target database is not up to date"
- **Solution:** Run `alembic upgrade head` to apply pending migrations

**Issue:** Changes not detected by autogenerate
- **Solution:** Ensure your model is imported in `app/models/__init__.py`
