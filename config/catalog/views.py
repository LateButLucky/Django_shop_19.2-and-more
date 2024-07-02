from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.text import slugify
from .models import Product, Contact, BlogPost, Version
from .forms import ContactForm, ProductForm, BlogPostForm, VersionForm
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for product in context['products']:
            product.current_version = Version.objects.filter(product=product, is_current=True).first()
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


class ContactView(FormView):
    template_name = 'catalog/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class CreateProductView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/create_product.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['version_form'] = VersionForm()
        context['versions'] = Version.objects.filter(product=self.object)
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        version_form = VersionForm(self.request.POST)
        if version_form.is_valid():
            version = version_form.save(commit=False)
            version.product = self.object
            version.save()
        return response


class UpdateProductView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['version_form'] = VersionForm()
        context['product'] = self.object
        context['versions'] = Version.objects.filter(product=self.object)
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        version_form = VersionForm(self.request.POST)
        if version_form.is_valid():
            version = version_form.save(commit=False)
            version.product = self.object
            version.save()
        return response


class VersionDeleteView(DeleteView):
    model = Version

    def get_success_url(self):
        product_id = self.kwargs['product_id']
        return reverse_lazy('update_product', kwargs={'pk': product_id})

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        return redirect(success_url)


class DeleteProductView(DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('home')


class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'catalog/blog_list.html'
    context_object_name = 'blogposts'
    queryset = BlogPost.objects.filter(published=True)


class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'catalog/blog_detail.html'
    context_object_name = 'blogpost'

    def get_object(self, queryset=None):
        blogpost = super().get_object(queryset)
        blogpost.views += 1
        blogpost.save()
        return blogpost


class BlogPostCreateView(CreateView):
    model = BlogPost
    template_name = 'catalog/blog_form.html'
    form_class = BlogPostForm

    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.slug = slugify(self.object.title)
        self.object.save()
        return response


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    template_name = 'catalog/blog_form.html'
    form_class = BlogPostForm

    def get_success_url(self):
        return reverse_lazy('blog_detail', args=[self.object.slug])


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'catalog/blog_confirm_delete.html'
    success_url = reverse_lazy('blog_list')


class CreateVersionView(CreateView):
    model = Version
    form_class = VersionForm
    template_name = 'catalog/version_form.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.product_id = self.request.GET.get('product_id')
        return super().form_valid(form)


class DeleteVersionView(DeleteView):
    model = Version
    template_name = 'catalog/version_confirm_delete.html'
    success_url = reverse_lazy('home')
