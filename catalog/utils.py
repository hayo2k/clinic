
menu = [{'title': 'Панель управления', 'url_name': 'index'},
        {'title': 'Специалисты', 'url_name': 'about'},
        {'title': 'Регистрация', 'url_name': 'users:register'},
        {'title': 'Авторизация', 'url_name': 'users:login'},
        {'title': 'Анализы', 'url_name': 'analysis'},



]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        return context
