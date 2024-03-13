from app.models.mail_config import mail_config
from sqlalchemy.exc import NoResultFound


class MailConfig:


    def get_config(self):
        try:
            mail_configuration = mail_config.query.one()
        except NoResultFound:
            mail_configuration = None
        return mail_configuration