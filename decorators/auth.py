from functools import wraps

from django.http import HttpResponse
from django.utils.decorators import available_attrs

def require_login ( view_func ):
	@wraps(view_func, assigned=available_attrs(view_func))
	def inner ( req, *args, **kwargs ):
		if req.user.is_authenticated():
			return view_func( req, *args, **kwargs )

		msg = 'Only authenticated users may perform this action.'
		res = HttpResponse(msg, status=401) # 401 = unauthorized
		res['Content-Length'] = len( msg )
		return res
	return inner

