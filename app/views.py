from flask_appbuilder import ModelView
from flask_appbuilder.fieldwidgets import Select2Widget
from flask_appbuilder.models.sqla.interface import SQLAInterface
from .models import Employee,Department, Function, EmployeeHistory, Benefit, MenuItem, MenuCategory, News, NewsCategory, GetStarted, LearningMaterials, TypesofLearningcenter, PopularLearningMaterials, AllLearningMaterials, LearnXamarin
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from app import appbuilder, db
from flask_appbuilder.baseviews import expose, BaseView


def department_query():
    return db.session.query(Department)


class EmployeeHistoryView(ModelView):
    datamodel = SQLAInterface(EmployeeHistory)
    #base_permissions = ['can_add', 'can_show']
    list_columns = ['department', 'begin_date', 'end_date']


class EmployeeView(ModelView):
    datamodel = SQLAInterface(Employee)

    list_columns = ['full_name', 'department.name', 'employee_number']
    edit_form_extra_fields = {'department':  QuerySelectField('Department',
                                query_factory=department_query,
                                widget=Select2Widget(extra_classes="readonly"))}


    related_views = [EmployeeHistoryView]
    show_template = 'appbuilder/general/model/show_cascade.html'


class FunctionView(ModelView):
    datamodel = SQLAInterface(Function)
    related_views = [EmployeeView]


class DepartmentView(ModelView):
    datamodel = SQLAInterface(Department)
    related_views = [EmployeeView]


class BenefitView(ModelView):
    datamodel = SQLAInterface(Benefit)
    add_columns = ['name']
    edit_columns = ['name']
    show_columns = ['name']
    list_columns = ['name']

class MenuItemView(ModelView):
    datamodel = SQLAInterface(MenuItem)
    list_columns = ['id', 'name', 'link', 'menu_category_id']

class MenuCategoryView(ModelView):
    datamodel = SQLAInterface(MenuCategory)
    list_columns = ['id', 'name']

class NewsView(ModelView):
    datamodel = SQLAInterface(News)
    list_columns = ['id', 'title', 'content', 'date', 'newsCat_id']

class NewsCategoryView(ModelView):
    datamodel = SQLAInterface(NewsCategory)
    list_columns = ['id', 'name']
    
class GetStartedView(ModelView):
    datamodel = SQLAInterface(GetStarted)
    list_columns = ['id', 'title', 'content', 'Types_of_Learning_center_id']

class LearningMaterialsView(ModelView):
    datamodel = SQLAInterface(LearningMaterials)
    list_columns = ['id', 'title', "Types_of_Learning_center_id"]

class TypesofLearningcenterView(ModelView):
    datamodel = SQLAInterface(TypesofLearningcenter)
    list_columns = ['id', 'title']
    
class PopularLearningMaterialsView(ModelView):
    datamodel = SQLAInterface(PopularLearningMaterials)
    list_columns = ["id", "title", "content", "Learn_Xamarin_id"]

class AllLearningMaterialsView(ModelView):
    datamodel = SQLAInterface(AllLearningMaterials)
    list_columns = ["id", "title", "content", "Learn_Xamarin_id"]

class LearnXamarinView(ModelView):
    datamodel = SQLAInterface(LearnXamarin)
    list_columns = ['id', 'title']
    
class NewsPageView(BaseView):
    default_view = 'local_news'

    @expose('/local_news/')
    def local_news(self):
        param1 = 'Local News'
        self.update_redirect()
        return self.render_template('news.html', param1 = param1)

    @expose('/global_news/')
    def global_news(self):
        param1 = 'Global News'
        self.update_redirect()
        return self.render_template('news.html', param1=param1)

class MicrosoftView(BaseView):
    default_view = "learning_center"
    
    @expose("/learning_center/")
    def learning_center(self):
        param1 = "learning center"
        self.update_redirect()
        return self.render_template("learning center.html", param1=param1)

    @expose("/Xamarin/")
    def Xamarin(self):
        param1 = "Xamarin"
        self.update_redirect()
        return self.render_template("Xamarin.html", param1=param1)
    
    
        


db.create_all()

""" Page View """
appbuilder.add_view(NewsPageView, 'Local News', category="News")
appbuilder.add_link("Global News", href="/newspageview/global_news/", category="News")

appbuilder.add_view(MicrosoftView, "learning center", category="Learning center")
appbuilder.add_link("Xamarin", href="/microsoftview/Xamarin/", category="Learning center")

""" Custom Views """
appbuilder.add_view(MenuItemView, "MenuItem", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(MenuCategoryView, "MenuCategory", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(NewsView, "News", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(NewsCategoryView, "NewsCategory", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(GetStartedView, "GetStarted", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(LearningMaterialsView, "LearningMaterials", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(TypesofLearningcenterView, "TypesofLearningcenter", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(PopularLearningMaterialsView, "PopularLearningMaterials", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(AllLearningMaterialsView, "AllLearningMaterials", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(LearnXamarinView, "LearnXamarin", icon="fa-folder-open-o", category="Admin")
