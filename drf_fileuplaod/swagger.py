from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

# ✅ Configure Swagger to Use Bearer Authentication
schema_view = get_schema_view(
    openapi.Info(
        title="My API",
        default_version='v1',
        description="API documentation with JWT authentication",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
    authentication_classes=[],  # ✅ Allows public access to Swagger
)

# ✅ Add Security Definitions (JWT)
schema_view.generator.security_definitions = {
    "Bearer": openapi.SecurityScheme(
        type=openapi.TYPE_APIKEY,
        in_=openapi.IN_HEADER,
        name="Authorization",
        description="Enter your JWT token in the format **Bearer <your_token>**",
    )
}
