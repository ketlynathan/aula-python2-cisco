from datetime import datetime, timezone


def now_utc_iso() -> str:

"""Retorna a data/hora atual em UTC no formato ISO (timezone-aware)."""
return datetime.now(timezone.utc).isoformat()
