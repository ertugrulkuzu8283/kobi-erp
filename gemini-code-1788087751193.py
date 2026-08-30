import json
import logging
from sqlalchemy.orm import Session
from app.models.audit_model import AuditLog

audit_file_logger = logging.getLogger("erp.audit")


class AuditLogger:
    @staticmethod
    def log(
        db: Session,
        user_id: int,
        entity_name: str,
        entity_id: int,
        action: str,
        old_value: dict | None = None,
        new_value: dict | None = None
    ) -> None:
        """SQLAlchemy 2.0 ORM modeli üzerinden veritabanına ve log dosyasına yazar."""
        audit_entry = AuditLog(
            user_id=user_id,
            entity_name=entity_name,
            entity_id=entity_id,
            action=action,
            old_value=old_value,
            new_value=new_value
        )
        db.add(audit_entry)
        db.flush()

        audit_payload = {
            "user_id": user_id,
            "entity_name": entity_name,
            "entity_id": entity_id,
            "action": action,
            "old_value": old_value,
            "new_value": new_value
        }
        audit_file_logger.info(json.dumps(audit_payload, ensure_ascii=False))