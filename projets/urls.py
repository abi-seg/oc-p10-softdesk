from rest_framework_nested import routers
from .views import (
    ProjectViewSet, IssueViewSet, ContributorViewSet, CommentViewSet
)

# Base router for /projects/
router = routers.SimpleRouter()
router.register(r'projects', ProjectViewSet, basename='projects')

# Nested: /projects/<project_id>/issues/
projects_router = routers.NestedSimpleRouter(router, r'projects', lookup='project')
projects_router.register(r'issues', IssueViewSet, basename='project-issues')

# Nested: /projects/<project_id>/contributors/
projects_router.register(r'contributors', ContributorViewSet, basename='project-contributors')

# Nested: /projects/<project_id>/issues/<issue_id>/comments/
issues_router = routers.NestedSimpleRouter(projects_router, r'issues', lookup='issue')
issues_router.register(r'comments', CommentViewSet, basename='issue-comments')

urlpatterns = (
    router.urls +
    projects_router.urls +
    issues_router.urls
)