from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy

from books.models import Book, Profile
from books.forms import SettingsForm


class BookListView(ListView):
    model = Book
    paginate_by = 10
    paginate_orphans = 2
    form_class = SettingsForm

    def get_queryset(self):
        fields = Profile.objects.filter(is_visible=True).values_list('column_name', flat=True)
        queryset = Book.objects.values_list('id', *fields)
        return queryset

    def get_context_data(self, **kwargs):
        initials = dict(Profile.objects.values_list('column_name', 'is_visible'))
        form = self.form_class(initial=initials)
        verbose_names = {
            'name': 'Название',
            'title': 'Заглавие',
            'author': 'Автор',
            'description': 'Описание',
            'price': 'Цена'
        }
        table_headers = [verbose_names[name] for name, visibility in initials.items() if visibility]
        return super().get_context_data(form=form, table_headers=table_headers, **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            settings = Profile.objects.exclude(column_name='name')
            for setting in settings:
                setting.is_visible = form.cleaned_data[setting.column_name]
                Profile.objects.bulk_update(settings, ['is_visible'])
        return redirect('book_list')


class BookDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy('book_list')


class BookUpdateView(UpdateView):
    model = Book
    fields = ['name', 'title', 'author', 'description', 'price']
    success_url = reverse_lazy('book_list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['description'].widget.attrs['cols'] = 100
        form.fields['description'].widget.attrs['rows'] = 7
        form.fields['price'].widget.attrs['max'] = 99999
        return form


class BookCreateView(CreateView):
    model = Book
    fields = ['name', 'title', 'author', 'description', 'price']
    success_url = reverse_lazy('book_list')


class BookDetailView(DetailView):
    model = Book
