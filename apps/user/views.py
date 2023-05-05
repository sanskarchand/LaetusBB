import logging

from django.shortcuts import render
from django.template import loader
#from django.views.decorators.http import require_http_methods
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.generic import View

from core.validators import (
        validate_wholesale,
        ValidationValueMissingError
)
from core.errors import (
        ERR_SERVER_ERROR
)

logger = logging.getLogger(__name__)

class RegistrationView(View):
    template_name = "apps/user/register.html"

    @method_decorator(csrf_protect)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        pass

class LoginView(View):
    template_name = "apps/user/login.html"

    @method_decorator(csrf_protect)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        data = request.POST

        type_map = {"email": "email", "password": "password"}
        value_map  = {}
        for field in type_map:
            value_map[spec] = data.get(field)
        
        try:
            errors = validate_wholesale(type_map, value_map)
        except ValidationValueMissingError:
            logger.error(f"ValidationValueMissingError for {value_map}")
            return render(request, "core/error.html", {'error': ERR_SERVER_ERROR})
        
        # show errors, if any
        if errors:
            return render(request, self.template_name, {"errors": errors})
