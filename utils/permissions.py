from rest_framework.permissions import IsAuthenticated


class IsCompany(IsAuthenticated):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_company)


class IsCompanyOwner(IsCompany):
    def has_permission(self, request, view):
        return request.user.company.get().id == request.data.get('company_id')
