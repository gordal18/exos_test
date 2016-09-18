from datetime import date
from users.config import ELIGIBLE_AGE, BIZZ, FUZZ


def is_eligible(born):
	today = date.today()
	age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
	return age >= ELIGIBLE_AGE


def get_bizzfuzz(value):
    if not (value % BIZZ or value % FUZZ): return 'BizzFuzz'
    if not (value % BIZZ): return 'Bizz'
    if not (value % FUZZ): return 'Fuzz'
    return value