from sqlalchemy import create_engine, text
import os

# Ensure the environment variable is set correctly
db_connection_string = os.environ.get('DB_CONNECTION_STRING')

# Create the engine with the SSL configuration
engine = create_engine(db_connection_string,
                       connect_args={
                           "ssl": {
                               "ssl_ca": "C:/Users/user/Desktop/new-flask/isrgrootx1.pem"
                           }
                       })


def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs"))
        result_dicts = [dict(row._mapping) for row in result.all()]
        return result_dicts


def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs WHERE id = :id"), {"id": id})
        rows = [row._mapping for row in result.all()]
        if len(rows) == 0:
            return None
        else:
            return rows[0]  # returning the first (and only) row


def add_application_to_db(job_id, application):
    with engine.connect() as conn:
        query = text(
            "INSERT INTO application (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) "
            "VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)"
        )
        conn.execute(query, {
            'job_id': job_id,
            'full_name': application['full_name'],
            'email': application['email'],
            'linkedin_url': application['linkedin_url'],  
            'education': application['education'],
            'work_experience': application['work_experience'],
            'resume_url': application['resume_url']
        })
