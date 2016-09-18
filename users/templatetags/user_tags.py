from django import template
from datetime import date
from users.utils import is_eligible, get_bizzfuzz

register = template.Library()

@register.simple_tag
def display_eligible(born):
	return 'allowed' if is_eligible(born) else 'blocked'


@register.simple_tag
def display_bizzfuzz(value):
	return get_bizzfuzz(value)